#!/usr/bin/env python3
"""
One-shot pipeline: Stage 1 (batch job evaluations via Cursor Agent) then Stage 2 (collate overview).

Default behavior matches a safe "press start" re-run: skip JDs that already have eval reports,
then write a timestamped overview under job-evaluation-reports/ (see collate --help). Use --no-skip-existing to force a full re-evaluation of every JD.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def main() -> int:
    repo = _repo_root()
    batch_script = repo / "journal_summarizer" / "scripts" / "batch_job_evaluations.py"
    collate_script = repo / "journal_summarizer" / "scripts" / "collate_job_evaluations.py"

    parser = argparse.ArgumentParser(
        description="Run job-eval Stage 1 (batch) then Stage 2 (collate overview).",
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=None,
        help=f"Repository root (default: {repo}).",
    )
    parser.add_argument(
        "--no-skip-existing",
        action="store_true",
        help="Re-run the agent for every JD even if a report already exists (expensive).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Stage 1 only: print planned agent invocations without calling agent. Skips Stage 2 (no new overview file).",
    )
    parser.add_argument(
        "--stage1-only",
        action="store_true",
        help="Only run batch evaluations; skip collate.",
    )
    parser.add_argument(
        "--stage2-only",
        action="store_true",
        help="Only run Stage 2 collate from existing reports (skip Stage 1).",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="GLOB",
        help="Stage 1: only JD basenames matching this pattern (repeatable).",
    )
    parser.add_argument(
        "--jd-dir",
        type=Path,
        default=None,
        help="Stage 1: job descriptions directory (default: <repo>/job descriptions).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        metavar="SEC",
        help="Stage 1: per-JD agent timeout (default: batch script default).",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=None,
        help="Stage 1: JSONL log path (default: job-evaluation-reports/_batch_runs.jsonl).",
    )
    parser.add_argument(
        "--agent-bin",
        default=None,
        help="Stage 1: path to agent executable.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Stage 1: pass an explicit model through to `agent --model`.",
    )
    parser.add_argument(
        "--heartbeat-sec",
        type=float,
        default=None,
        metavar="SEC",
        help=(
            "Stage 1: forwarded to batch_job_evaluations.py "
            "(status line every SEC seconds while agent runs; omit for batch default 30; 0 disables)."
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=(
            "Stage 2: explicit overview path (default: "
            "_OVERVIEW-<YYYYMMDD-HHMMSS>(<n>).md in job-evaluation-reports/)."
        ),
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Stage 2: also pass --html to collate (Plotly dashboard beside the overview .md).",
    )
    parser.add_argument(
        "--html-out",
        type=Path,
        default=None,
        help="Stage 2: pass --html-out to collate (explicit HTML path).",
    )
    args = parser.parse_args()

    repo = (args.repo or repo).resolve()
    if args.stage1_only and args.stage2_only:
        print("error: --stage1-only and --stage2-only are mutually exclusive", file=sys.stderr)
        return 2

    py = sys.executable
    s1 = 0
    s2 = 0
    dry_skip_collate = args.dry_run

    if args.stage2_only and args.dry_run:
        print("=== Nothing to do (--dry-run skips Stage 2; omit --stage2-only to dry-run Stage 1) ===", flush=True)
        return 0

    if not args.stage2_only:
        cmd = [py, str(batch_script), "--repo", str(repo)]
        if not args.no_skip_existing:
            cmd.append("--skip-existing")
        if args.dry_run:
            cmd.append("--dry-run")
        if args.only:
            for pat in args.only:
                cmd.extend(["--only", pat])
        if args.jd_dir is not None:
            cmd.extend(["--jd-dir", str(args.jd_dir)])
        if args.timeout is not None:
            cmd.extend(["--timeout", str(args.timeout)])
        if args.log is not None:
            cmd.extend(["--log", str(args.log)])
        if args.agent_bin is not None:
            cmd.extend(["--agent-bin", args.agent_bin])
        if args.model is not None:
            cmd.extend(["--model", args.model])
        if args.heartbeat_sec is not None:
            cmd.extend(["--heartbeat-sec", str(args.heartbeat_sec)])

        print("=== Stage 1: batch job evaluations ===", flush=True)
        s1 = subprocess.call(cmd, cwd=str(repo))
        if s1 != 0:
            print(f"=== Stage 1 exited {s1} (continuing to Stage 2 if enabled) ===", flush=True)

    if dry_skip_collate:
        print("=== Stage 2 skipped (--dry-run writes no overview file) ===", flush=True)

    if not args.stage1_only and not dry_skip_collate:
        cmd2 = [py, str(collate_script), "--repo-root", str(repo)]
        if args.out is not None:
            cmd2.extend(["--out", str(args.out)])
        if args.html:
            cmd2.append("--html")
        if args.html_out is not None:
            cmd2.extend(["--html-out", str(args.html_out)])
        print("=== Stage 2: collate overview ===", flush=True)
        s2 = subprocess.call(cmd2, cwd=str(repo))

    if args.stage2_only:
        return s2
    if args.stage1_only:
        return s1
    return 1 if (s1 != 0 or s2 != 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
