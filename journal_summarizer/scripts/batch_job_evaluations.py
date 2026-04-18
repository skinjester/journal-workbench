#!/usr/bin/env python3
"""
Stage 1: run one Cursor Agent evaluation per job-description file.

Requires the Cursor Agent CLI (`agent`) on PATH, authenticated for non-interactive use.
See job-evaluation-reports/README.md for prerequisites and examples.

This script does not call cloud LLMs directly; it shells out to `agent` with
--print --force --trust (and optionally --model).
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import collate_job_evaluations as cj


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _find_agent_bin(explicit: str | None) -> str:
    if explicit:
        return explicit
    env = os.environ.get("CURSOR_AGENT_BIN") or os.environ.get("AGENT_BIN")
    if env:
        return env
    for name in ("agent", "cursor-agent"):
        p = shutil.which(name)
        if p:
            return p
    return "agent"


def _list_jd_files(jd_dir: Path) -> list[Path]:
    out: list[Path] = []
    for ent in sorted(jd_dir.iterdir(), key=lambda p: p.name.lower()):
        if ent.name.startswith("."):
            continue
        if ent.is_file():
            out.append(ent)
    return out


def _build_prompt(repo: Path, jd_rel: str) -> str:
    # Repo-relative paths; agent runs with --workspace repo.
    return f"""Automated job-evaluation batch step (single JD).

You MUST read and follow these workspace files before writing:
- JOB_EVALUATION_TEMPLATE.md
- JOB_EVALUATION_REFERENCES.md
- JOB_EVAL_CHAT_COMMAND.md

The job description for this run is:
- {jd_rel}

Requirements (summarized from JOB_EVAL_CHAT_COMMAND.md):
- Write the FULL report under job-evaluation-reports/ using the template naming + collision rules.
- Use the exact PART 1 through PART 6 headings from JOB_EVALUATION_TEMPLATE.md.
- Use both resume variants from JOB_EVALUATION_REFERENCES.md; review every portfolio URL listed there; include header metadata and evidence accounting per template.
- Include at least 2 short quotes total from summaries or monthly dumps in PART 3, each with repo-relative file paths (use the folders listed under JOB_EVALUATION_REFERENCES.md).

After the report file is written, end your reply with a single line exactly in this form (fill in the real path):
OUTPUT_PATH: job-evaluation-reports/<filename>.md
"""


def _append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch-run job evaluations via Cursor Agent CLI.")
    parser.add_argument(
        "--repo",
        type=Path,
        default=None,
        help="Repository root (default: parent of journal_summarizer/).",
    )
    parser.add_argument(
        "--jd-dir",
        type=Path,
        default=None,
        help="Directory of job-description files (default: <repo>/job descriptions).",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="GLOB",
        help="Only JDs whose basename matches this fnmatch pattern (repeatable).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip if job-evaluation-reports/<JD>.eval.md already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned invocations without running agent.",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=None,
        help="Append JSONL log path (default: job-evaluation-reports/_batch_runs.jsonl).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=2400,
        metavar="SEC",
        help="Per-JD subprocess timeout in seconds (default: 2400).",
    )
    parser.add_argument(
        "--agent-bin",
        default=None,
        help="Path to agent executable (default: CURSOR_AGENT_BIN or first of agent, cursor-agent on PATH).",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Pass an explicit model through to `agent --model` (for example: gpt-5.4-medium).",
    )
    args = parser.parse_args()

    repo = (args.repo or _default_repo_root()).resolve()
    jd_dir = (args.jd_dir or (repo / "job descriptions")).resolve()
    log_path = (args.log or (repo / "job-evaluation-reports" / "_batch_runs.jsonl")).resolve()

    if not repo.is_dir():
        print(f"error: repo not a directory: {repo}", file=sys.stderr)
        return 2
    if not jd_dir.is_dir():
        print(f"error: jd-dir not a directory: {jd_dir}", file=sys.stderr)
        return 2

    agent_bin = _find_agent_bin(args.agent_bin)
    if not args.dry_run and not shutil.which(agent_bin):
        print(
            "error: Cursor Agent CLI not found on PATH.\n"
            f"  Tried executable name: {agent_bin!r}\n"
            "  Install from https://cursor.com/install and ensure `agent` is on PATH,\n"
            "  or pass --agent-bin /path/to/agent or set CURSOR_AGENT_BIN.",
            file=sys.stderr,
        )
        return 127

    jd_files = _list_jd_files(jd_dir)
    if args.only:
        filtered: list[Path] = []
        for p in jd_files:
            if any(fnmatch.fnmatch(p.name, pat) for pat in args.only):
                filtered.append(p)
        jd_files = filtered

    if not jd_files:
        print("No job description files matched.", file=sys.stderr)
        return 3

    reports_dir = repo / "job-evaluation-reports"
    run_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    failures = 0

    for jd_path in jd_files:
        try:
            jd_rel = jd_path.relative_to(repo).as_posix()
        except ValueError:
            print(
                f"error: job description must live under repo root (--repo); got: {jd_path}",
                file=sys.stderr,
            )
            return 2
        jd_base = jd_path.name
        ts_start = time.time()

        if args.skip_existing and cj.any_eval_report_exists_for_jd(reports_dir, jd_base):
            row = {
                "run_id": run_id,
                "jd_path": jd_rel,
                "jd_basename": jd_base,
                "skipped": True,
                "reason": "eval_exists",
                "elapsed_sec": round(time.time() - ts_start, 3),
            }
            _append_jsonl(log_path, row)
            print(f"skip (exists): {jd_rel}")
            continue

        before_snap = cj.snapshot_reports_for_jd(reports_dir, jd_base)
        prompt = _build_prompt(repo, jd_rel)
        cmd = [
            agent_bin,
            "--print",
            "--force",
            "--trust",
            "--workspace",
            str(repo),
        ]
        if args.model is not None:
            cmd.extend(["--model", args.model])
        cmd.append(prompt)

        if args.dry_run:
            prefix = " ".join(cmd[:-1])
            print("[dry-run] would run:", prefix, f'"... ({len(prompt)} chars)"')
            continue

        print(f"run: {jd_rel}")
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(repo),
                text=True,
                timeout=args.timeout,
            )
        except subprocess.TimeoutExpired:
            failures += 1
            row = {
                "run_id": run_id,
                "jd_path": jd_rel,
                "jd_basename": jd_base,
                "ok": False,
                "error": "timeout",
                "elapsed_sec": round(time.time() - ts_start, 3),
            }
            _append_jsonl(log_path, row)
            print(f"error: timeout after {args.timeout}s: {jd_rel}", file=sys.stderr)
            continue

        ok = proc.returncode == 0
        output_verified = False
        if ok:
            after_snap = cj.snapshot_reports_for_jd(reports_dir, jd_base)
            output_verified = cj.report_mutation_detected(before_snap, after_snap)
            if not output_verified:
                failures += 1
                print(
                    f"error: agent exited 0 but no new/updated eval report detected for JD key "
                    f"{jd_base!r} under job-evaluation-reports/ ({jd_rel})",
                    file=sys.stderr,
                )
        else:
            failures += 1
        row = {
            "run_id": run_id,
            "jd_path": jd_rel,
            "jd_basename": jd_base,
            "ok": ok,
            "returncode": proc.returncode,
            "output_verified": output_verified if ok else None,
            "elapsed_sec": round(time.time() - ts_start, 3),
        }
        _append_jsonl(log_path, row)
        if not ok:
            print(f"error: agent exit {proc.returncode}: {jd_rel}", file=sys.stderr)

    if args.dry_run:
        print(f"dry-run complete; {len(jd_files)} job(s).")
        return 0

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
