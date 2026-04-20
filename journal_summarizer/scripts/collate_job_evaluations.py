#!/usr/bin/env python3
"""
Collate per-job evaluation markdown reports into a single overview.

Expected report filenames (repo convention):
  job-evaluation-reports/<JD basename>.eval.md
  job-evaluation-reports/<JD basename>.eval - YYYY-MM-DD.md
  job-evaluation-reports/<JD basename>.eval - YYYY-MM-DD - N.md

Dedupe policy:
  Group by <JD basename> (strip the ".eval..." suffix), pick latest mtime.

Output:
  Markdown with a summary table + per-job sections containing PART 5 verdict lines only.
  Optional `--html` / `--html-out`: standalone Plotly HTML dashboard (see `job_eval_overview_html.py`).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


REPORT_NAME_RE = re.compile(
    r"^(?P<base>.+?)\.eval(?P<suffix>(?: - .+)?)\.md$",
    re.IGNORECASE,
)

JOB_LINE_RE = re.compile(r"^\s*-\s*`job`\s*:\s*(.+?)\s*$")
JD_SOURCE_LINE_RE = re.compile(r"^\s*-\s*`jd_source`\s*:\s*(.+?)\s*$")

PART5_START_RE = re.compile(r"^#{1,6}\s*PART\s*5\b", re.IGNORECASE)
PART6_START_RE = re.compile(r"^#{1,6}\s*PART\s*6\b", re.IGNORECASE)

@dataclass(frozen=True)
class VerdictRule:
    column: str
    pattern: re.Pattern[str]


# Leading rating phrase (single match at start of remainder); kept for edge fallbacks.
_RATING_AT_START = re.compile(
    r"^\s*((?:Very\s+)?(?:"
    r"Medium(?:[-–—]High|\s+High)|"
    r"Medium|High|Low|"
    r"N/A|TBD|Unknown"
    r"))\b",
    re.IGNORECASE,
)

# Scan full verdict text for all tier tokens (Medium–High before bare Medium). Used to pick highest tier.
_ALL_RATING_TOKENS_RE = re.compile(
    r"\b(?:Very\s+High|High|Medium(?:[-–—]High|\s+High)|Medium|Low|Unknown|N/A|TBD)\b",
    re.IGNORECASE,
)

# Summary table / chart column order (must match `VerdictRule.column` strings).
VERDICT_TABLE_COLUMNS: Tuple[str, ...] = (
    "Fit on Paper",
    "Capability",
    "Narrative Coherence",
    "Signal Strength (Recruiter)",
    "Signal Strength (HM)",
)

VERDICT_RULES: Tuple[VerdictRule, ...] = (
    VerdictRule(
        "Fit on Paper",
        re.compile(r"^\*{0,2}Fit on paper\*{0,2}\s*:\s*", re.IGNORECASE),
    ),
    VerdictRule(
        "Capability",
        re.compile(
            r"^\*{0,2}Actual capability(?:\s*\(inferred\))?\*{0,2}\s*:\s*",
            re.IGNORECASE,
        ),
    ),
    VerdictRule(
        "Narrative Coherence",
        re.compile(
            r"^\*{0,2}Narrative coherence(?:\s*\(for this JD\))?\*{0,2}\s*:\s*",
            re.IGNORECASE,
        ),
    ),
    VerdictRule(
        "Signal Strength (Recruiter)",
        re.compile(
            r"^\*{0,2}(?:Signal strength:\s*Recruiter|Likelihood of recruiter screen)\*{0,2}\s*:\s*",
            re.IGNORECASE,
        ),
    ),
    VerdictRule(
        "Signal Strength (HM)",
        re.compile(
            r"^\*{0,2}(?:Signal strength:\s*HM|Likelihood of hiring manager screen)\*{0,2}\s*:\s*",
            re.IGNORECASE,
        ),
    ),
)


def _strip_md_noise(s: str) -> str:
    s = s.strip()
    s = s.replace("`", "")
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\\)\[(.+?)\]\([^)]+\)", r"\1", s)  # drop markdown links
    return s.strip()


def extract_job_title(text: str) -> str:
    for line in text.splitlines():
        m = JOB_LINE_RE.match(line)
        if m:
            return _strip_md_noise(m.group(1))
    return ""


def extract_jd_source(text: str) -> str:
    for line in text.splitlines():
        m = JD_SOURCE_LINE_RE.match(line)
        if m:
            return _strip_md_noise(m.group(1))
    return ""


def jd_basename_from_source(jd_source: str) -> str:
    """
    Prefer deriving JD basename from `jd_source` when it references a repo file.
    Fallback: empty string.
    """
    jd_source = jd_source.strip()
    if jd_source.startswith("@") and not jd_source.lower().startswith("@http"):
        jd_source = jd_source[1:].strip()
    for prefix in ("job descriptions/", "job descriptions-processed/"):
        if jd_source.startswith(prefix):
            return jd_source[len(prefix) :].strip()
    return ""


def extract_part5_section(text: str) -> str:
    lines = text.splitlines()
    start_idx: Optional[int] = None
    for i, line in enumerate(lines):
        if PART5_START_RE.match(line.strip()):
            start_idx = i + 1
            break
    if start_idx is None:
        return ""

    out: List[str] = []
    for line in lines[start_idx:]:
        stripped = line.strip()
        if PART6_START_RE.match(stripped):
            break
        out.append(line)
    return "\n".join(out).strip()


def _normalize_rating_token_for_table(raw: str) -> str:
    """Canonical spelling for overview cells (en dash in Medium–High)."""
    s = re.sub(r"\s+", " ", raw.strip())
    low = s.lower().replace("–", "-").replace("—", "-")
    if low.startswith("very high"):
        return "Very High"
    if low == "high":
        return "High"
    if low in ("medium-high", "medium high") or low.replace(" ", "") in ("mediumhigh", "medium-high"):
        return "Medium–High"
    if low == "medium":
        return "Medium"
    if low == "low":
        return "Low"
    if low == "unknown":
        return "Unknown"
    if low == "n/a":
        return "N/A"
    if low == "tbd":
        return "TBD"
    return s.rstrip(".,;:")


def _rating_tier_rank(token: str) -> int:
    """
    Higher = better / stronger tier for overview when multiple ratings appear in one line.
    Unknown / N/A / TBD rank below substantive High/Medium/Low tiers.
    """
    n = _normalize_rating_token_for_table(token).lower().replace("–", "-").replace("—", "-")
    order = (
        "very high",
        "high",
        "medium-high",
        "medium",
        "low",
        "unknown",
        "n/a",
        "tbd",
    )
    try:
        # Higher index in tuple = lower rank score; invert so max() picks best tier
        idx = order.index(n)
    except ValueError:
        return -1
    return 100 - idx  # very high -> 100, tbd -> 92


def rating_only_for_summary(cell_after_label: str) -> str:
    """
    One cell value for the summary table: a single tier (High, Medium–High, Unknown, …).

    If the verdict text lists multiple tiers (e.g. semicolons: Medium–High for X; Medium for Y),
    uses the **highest** tier. If exactly one explicit Unknown / N/A / TBD appears with no higher
    tier, that value is shown.
    """
    t = cell_after_label.strip()
    if not t:
        return ""

    found = [m.group(0) for m in _ALL_RATING_TOKENS_RE.finditer(t)]
    if found:
        best = max(found, key=lambda tok: (_rating_tier_rank(tok), len(tok)))
        return _normalize_rating_token_for_table(best)

    # No known tier token: legacy single-token / first-word fallback
    t2 = t.split("(", 1)[0].strip()
    t2 = t2.split("[", 1)[0].strip()
    if " — " in t2:
        t2 = t2.split(" — ", 1)[0].strip()
    m = _RATING_AT_START.match(t2)
    if m:
        out = re.sub(r"\s+", " ", m.group(1).strip())
        return _normalize_rating_token_for_table(out)
    first = t2.split(None, 1)[0] if t2 else ""
    return first.rstrip(".,;:") if first else ""


def verdict_line_to_table_cell(line: str, column: str) -> str:
    """
    For the summary table only: rating only (e.g. High), no repeated header label or tail prose.
    """
    if not line:
        return ""
    s = line[2:].strip() if line.startswith("- ") else line.strip()
    s = _strip_md_noise(s)
    for rule in VERDICT_RULES:
        if rule.column == column:
            after = rule.pattern.sub("", s).strip()
            return rating_only_for_summary(after)
    return rating_only_for_summary(s)


def tier_cell_to_numeric(cell: str) -> Optional[float]:
    """
    Map a summary-table cell string (post-`verdict_line_to_table_cell`) to a numeric score for charts.
    Uses the same tier ordering as `_rating_tier_rank` (higher = better substantive fit).
    Returns None if empty or not a recognized tier token.
    """
    t = (cell or "").strip()
    if not t:
        return None
    canon = _normalize_rating_token_for_table(t)
    r = _rating_tier_rank(canon)
    if r < 0:
        return None
    return float(r)


def tier_cell_to_chart_numeric(cell: str) -> Optional[float]:
    """
    Map an ordinal verdict cell to a **wide** 0–100 score for HTML charts only.

    Collated markdown tables still show the ordinal label; this spread avoids squeezing
    all tiers into a 92–100 band. Unknown / N/A / TBD sit below Low.
    """
    t = (cell or "").strip()
    if not t:
        return None
    canon = _normalize_rating_token_for_table(t)
    n = canon.lower().replace("–", "-").replace("—", "-")
    chart: Dict[str, float] = {
        "very high": 92.0,
        "high": 80.0,
        "medium-high": 62.0,
        "medium": 40.0,
        "low": 15.0,
        "unknown": 28.0,
        "n/a": 22.0,
        "tbd": 18.0,
    }
    if n not in chart:
        return None
    return chart[n]


def extract_verdict_lines(part5: str) -> Dict[str, str]:
    """
    Return mapping column key -> raw markdown line (trimmed), for PART 5 verdict bullets
    (Fit on Paper through signal-strength lines, including Narrative Coherence).

    Supports:
    - list bullets: ``- **Fit on paper:** **High**``
    - bold-only paragraphs (no leading ``- ``): ``**Fit on paper:** **High**``
    """
    found: Dict[str, str] = {}
    if not part5:
        return found

    for raw_line in part5.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("|"):
            continue
        if line.startswith("- "):
            payload = line[2:].strip()
        else:
            payload = line

        for rule in VERDICT_RULES:
            if rule.pattern.match(payload):
                # First win keeps the line (stable if duplicates exist)
                found.setdefault(rule.column, line)
                break

    return found


def is_collated_overview_markdown(name: str) -> bool:
    """Collated overview outputs (`_OVERVIEW-…` default, legacy `OVERVIEW-…`); never treat as eval reports."""
    return name.startswith("_OVERVIEW") or name.startswith("OVERVIEW-") or name.startswith("_QUEUE")


def iter_candidate_reports(reports_dir: Path) -> Iterable[Path]:
    for p in sorted(reports_dir.iterdir()):
        if not p.is_file():
            continue
        if p.suffix.lower() != ".md":
            continue
        name = p.name
        if name == "README.md":
            continue
        if is_collated_overview_markdown(name):
            continue
        if ".eval" not in name:
            continue
        yield p


def group_key_for_report(path: Path) -> Optional[str]:
    m = REPORT_NAME_RE.match(path.name)
    if not m:
        return None
    return m.group("base").strip()


def snapshot_reports_for_jd(reports_dir: Path, jd_basename: str) -> Dict[str, float]:
    """
    Map resolved path string -> mtime for markdown reports whose filename
    groups to the given JD basename (same key as choose_latest_per_group).
    """
    out: Dict[str, float] = {}
    if not reports_dir.is_dir():
        return out
    for p in reports_dir.iterdir():
        if not p.is_file() or p.suffix.lower() != ".md":
            continue
        key = group_key_for_report(p)
        if key != jd_basename:
            continue
        out[str(p.resolve())] = p.stat().st_mtime
    return out


def report_mutation_detected(before: Dict[str, float], after: Dict[str, float]) -> bool:
    """True if a new report path appeared or any shared path's mtime increased."""
    before_paths: Set[str] = set(before.keys())
    after_paths: Set[str] = set(after.keys())
    if after_paths - before_paths:
        return True
    for path, mtime in after.items():
        if before.get(path, -1.0) < mtime:
            return True
    return False


def any_eval_report_exists_for_jd(reports_dir: Path, jd_basename: str) -> bool:
    """True if any well-formed *.eval*.md report exists for this JD basename."""
    return bool(snapshot_reports_for_jd(reports_dir, jd_basename))


def warn_unparsed_eval_markdown(reports_dir: Path) -> None:
    """
    Emit stderr warnings for markdown files that look like eval reports
    but do not match REPORT_NAME_RE (would be omitted from the overview).
    """
    if not reports_dir.is_dir():
        return
    for p in sorted(reports_dir.iterdir()):
        if not p.is_file() or p.suffix.lower() != ".md":
            continue
        name = p.name
        if name == "README.md":
            continue
        if is_collated_overview_markdown(name):
            continue
        if ".eval" not in name:
            continue
        if group_key_for_report(p) is None:
            print(
                f"collate_job_evaluations: warning: skipping unparsed eval filename: {name!r}",
                file=sys.stderr,
            )


def choose_latest_per_group(paths: Iterable[Path]) -> Dict[str, Path]:
    best: Dict[str, Tuple[float, str, Path]] = {}
    for p in paths:
        key = group_key_for_report(p)
        if not key:
            continue
        mtime = p.stat().st_mtime
        cur = best.get(key)
        # Tie-breaker: lexicographic path name for stability
        if cur is None or mtime > cur[0] or (mtime == cur[0] and p.name > cur[1]):
            best[key] = (mtime, p.name, p)
    return {k: v[2] for k, v in best.items()}


def md_table_row(cells: List[str]) -> str:
    def esc(cell: str) -> str:
        return cell.replace("|", "\\|").replace("\n", " ").strip()

    return "| " + " | ".join(esc(c) for c in cells) + " |"


def rel_posix(from_repo_root: Path, path: Path) -> str:
    try:
        return path.relative_to(from_repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def allocate_overview_path(reports_dir: Path, job_count: int) -> Path:
    """
    Default overview filename: _OVERVIEW-<YYYYMMDD-HHMMSS>(<n>).md
    <n> is the number of JD rows in the summary table. If that path already exists
    (same second, same row count), append -1, -2, ... before .md.
    """
    now = dt.datetime.now().astimezone()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    n = max(0, int(job_count))
    body = f"_OVERVIEW-{stamp}({n})"
    for i in range(200):
        suffix = "" if i == 0 else f"-{i}"
        p = reports_dir / f"{body}{suffix}.md"
        if not p.exists():
            return p
    raise SystemExit("Could not allocate a unique overview filename in job-evaluation-reports/")


@dataclass
class CollatedRow:
    jd_key: str
    job_title: str
    jd_source: str
    jd_inferred: str
    jd_mismatch: bool
    report_rel: str
    verdicts: Dict[str, str]


def build_overview(repo_root: Path, rows: List[CollatedRow]) -> str:
    now = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    lines: List[str] = []
    lines.append("# Job evaluation overview")
    lines.append("")
    lines.append(f"_Generated {now} by `journal_summarizer/scripts/collate_job_evaluations.py`._")
    lines.append("")
    lines.append("## Summary table")
    lines.append("")
    headers = ["JD key", "Report", *VERDICT_TABLE_COLUMNS]
    lines.append(md_table_row(headers))
    lines.append(md_table_row(["---"] * len(headers)))

    def short_verdict(column: str, verdicts: Dict[str, str]) -> str:
        return verdict_line_to_table_cell(verdicts.get(column, ""), column)

    for r in rows:
        report_link = f"[{r.report_rel}]({r.report_rel})"
        cells = [r.jd_key, report_link] + [short_verdict(col, r.verdicts) for col in VERDICT_TABLE_COLUMNS]
        lines.append(md_table_row(cells))

    lines.append("")
    lines.append("## PART 5 verdict lines (per job)")
    lines.append("")

    for r in rows:
        lines.append(f"### {r.jd_key}")
        lines.append("")
        lines.append(f"- **Job (`job`)**: {r.job_title or '_missing_'}")
        lines.append(f"- **JD source**: `{r.jd_source}`" if r.jd_source else "- **JD source**: _missing_")
        if r.jd_inferred and r.jd_mismatch:
            lines.append(
                f"- **Filename vs `jd_source` mismatch**: report filename key `{r.jd_key}` "
                f"does not match inferred JD basename `{r.jd_inferred}` from `jd_source`."
            )
        lines.append(f"- **Full report**: [`{r.report_rel}`]({r.report_rel})")
        lines.append("")
        lines.append("PART 5 verdict lines:")
        lines.append("")
        if not r.verdicts:
            lines.append("_Could not find PART 5 verdict bullets._")
            lines.append("")
            continue
        for label in VERDICT_TABLE_COLUMNS:
            line = r.verdicts.get(label, "")
            if line:
                lines.append(line)
            else:
                lines.append(f"- {label}: _missing_")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_collated_rows(reports_dir: Path, repo_root: Path) -> List[CollatedRow]:
    """Scan reports_dir, dedupe by JD basename, return one CollatedRow per job (sorted by jd_key)."""
    warn_unparsed_eval_markdown(reports_dir)
    candidates = list(iter_candidate_reports(reports_dir))
    chosen = choose_latest_per_group(candidates)

    rows: List[CollatedRow] = []
    for jd_key in sorted(chosen.keys()):
        path = chosen[jd_key]
        text = path.read_text(encoding="utf-8", errors="replace")
        job_title = extract_job_title(text)
        jd_source = extract_jd_source(text)
        inferred_jd = jd_basename_from_source(jd_source)
        jd_mismatch = bool(inferred_jd and inferred_jd != jd_key)

        part5 = extract_part5_section(text)
        verdicts = extract_verdict_lines(part5)
        rows.append(
            CollatedRow(
                jd_key=jd_key,
                job_title=job_title,
                jd_source=jd_source,
                jd_inferred=inferred_jd,
                jd_mismatch=jd_mismatch,
                report_rel=rel_posix(repo_root, path),
                verdicts=verdicts,
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Collate job evaluation reports into one overview markdown file.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root (defaults to journal-workbench/).",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=None,
        help="Directory containing *.eval*.md reports (default: <repo-root>/job-evaluation-reports).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=(
            "Output markdown path. If omitted, writes "
            "job-evaluation-reports/_OVERVIEW-<YYYYMMDD-HHMMSS>(<n>).md "
            "(local time, n = number of jobs in the table)."
        ),
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Also write a Plotly HTML dashboard next to the markdown (same stem, .html).",
    )
    parser.add_argument(
        "--html-out",
        type=Path,
        default=None,
        help="Explicit path for the HTML dashboard (overrides --html default naming).",
    )
    args = parser.parse_args()

    repo_root: Path = args.repo_root.resolve()
    reports_dir: Path = (args.reports_dir or (repo_root / "job-evaluation-reports")).resolve()

    if not reports_dir.is_dir():
        raise SystemExit(f"Reports dir not found: {reports_dir}")

    rows = build_collated_rows(reports_dir, repo_root)

    if args.out is not None:
        out_path = args.out.resolve()
    else:
        out_path = allocate_overview_path(reports_dir, len(rows)).resolve()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_overview(repo_root, rows), encoding="utf-8")
    print(f"Wrote {rel_posix(repo_root, out_path)} ({len(rows)} jobs)")

    if args.html or args.html_out is not None:
        if args.html_out is not None:
            html_path = args.html_out.resolve()
        else:
            html_path = out_path.with_suffix(".html")
        try:
            from job_eval_overview_html import write_overview_chart_html
        except ImportError as e:
            raise SystemExit(
                "Plotly is required for --html / --html-out. Install: pip install -r journal_summarizer/requirements.txt"
            ) from e

        write_overview_chart_html(
            html_path,
            rows,
            repo_root,
            overview_md_rel=rel_posix(repo_root, out_path),
        )
        print(f"Wrote {rel_posix(repo_root, html_path)} ({len(rows)} jobs)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
