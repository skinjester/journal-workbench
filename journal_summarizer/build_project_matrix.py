#!/usr/bin/env python3
"""
Build the `data` payload for `visualizations/project-matrix-all-summaries.html`
from tagged monthly summaries (`summaries/*.md`).

Usage (from repo root or this directory):
    python build_project_matrix.py
    python build_project_matrix.py --html visualizations/project-matrix-all-summaries.html
    python build_project_matrix.py --summaries summaries/ --stdout   # inspect JSON only

Each bullet line must look like: - **[TAG]** ... where TAG is in ALLOWED_PROJECT_TAGS
(keep in sync with categorizer.py). Expand rows bucket **line items by description**
(keyword/heuristic activity types), not by summary section headings (### Goals, etc.).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

# Mirror categorizer.ALLOWED_PROJECT_TAGS / SYNTHESIS_SECTION_ORDER (avoid importing yaml chain).
ALLOWED_PROJECT_TAGS = frozenset(
    {
        "ESO",
        "ESO-Platform",
        "ESO-Studio Site",
        "KESTREL",
        "OPS",
        "Portfolio",
        "Project Ansible",
        "skinjestercorp",
        "Image Garden",
        "deepdreamvisionquest",
        "xoholo",
        "iveda",
        "RPVR",
    }
)

ROW_ORDER = [
    "ESO",
    "ESO-Platform",
    "ESO-Studio Site",
    "KESTREL",
    "OPS",
    "Portfolio",
    "Project Ansible",
    "skinjestercorp",
    "Image Garden",
    "deepdreamvisionquest",
    "xoholo",
    "iveda",
    "RPVR",
]

DISPLAY_NAMES = {
    "ESO": "ESO",
    "ESO-Platform": "ESO-Platform",
    "ESO-Studio Site": "ESO-Studio Site",
    "KESTREL": "KESTREL",
    "OPS": "OPS",
    "Portfolio": "Portfolio",
    "Project Ansible": "Project Ansible",
    "skinjestercorp": "skinjestercorp",
    "Image Garden": "Image Garden",
    "deepdreamvisionquest": "deepdreamvisionquest",
    "xoholo": "xoholo",
    "iveda": "iveda",
    "RPVR": "RPVR",
}

DESCRIPTIONS = {
    "ESO": "Game client UI and related live product work (PC/console), tagged as ESO in summaries.",
    "ESO-Platform": "ElderScrollsOnline.com, marketing web, and merchandising surfaces.",
    "ESO-Studio Site": "Studio recruiting / studio site work.",
    "KESTREL": "Kestrel-era UI systems: quests, HUD, inventory, navigation, design deliverables.",
    "OPS": "Personal infrastructure, tooling, and operations.",
    "Portfolio": "Portfolio sites, web publishing, and personal web projects.",
    "Project Ansible": "Studio rack, audio, controllers, and production-environment work.",
    "skinjestercorp": "skinjestercorp-related work as tagged in summaries.",
    "Image Garden": "Image Garden workshops, talks, and related creative-tech work.",
    "deepdreamvisionquest": "DeepDream Vision Quest and related experiments.",
    "xoholo": "Futureworld / CineChamber / immersive media threads tagged xoholo.",
    "iveda": "iveda-tagged project work.",
    "RPVR": "RPVR-tagged project work.",
}

TAG_LINE = re.compile(r"^\s*-\s*\*\*\[([^\]]+)\]\*\*\s*(.*)$")
SECTION_LINE = re.compile(r"^\s*###\s+(.*?)\s*$")

PROTO_RE = re.compile(
    r"\b(prototype|prototyping|wireframe|wireframes|mockup|mock-up|sketchbox)\b",
    re.I,
)
PRES_RE = re.compile(
    r"\b(presentation|presentations|slides?|keynote|slide deck|deck\b|town hall|critique)\b",
    re.I,
)
PDF_RE = re.compile(r"(\.pdf\b|\bpdf\b)", re.I)

DELIV_RE = re.compile(r"`deliv:([a-z0-9_-]+)`", re.I)

# Ordered (name, patterns): first regex match wins. Tuned for journal summary vocabulary.
_DELIV_BUCKET = {
    "visuals": "Visual design & wireframes",
    "documentation": "Documentation & specs",
    "presentation": "Presentations & deck work",
    "prototype": "Prototyping & experiments",
    "design-system": "Design systems & components",
    "operations": "Operations & runbooks",
    "audit": "Research & audits",
}

ACTIVITY_RULES: List[Tuple[str, Tuple[str, ...]]] = [
    ("Recruiting & studio site", (r"\brecruit", r"studio site", r"candidate", r"job post")),
    ("Store & monetization", (r"crown store", r"\bbuy now\b", r"merch", r"dlc", r"purchase flow")),
    ("Community & social surfaces", (r"community hub", r"guild", r"social", r"forum")),
    ("Email & newsletters", (r"newsletter", r"mailchimp", r"subscribe", r"email blast")),
    ("Analytics & measurement", (r"analytics", r"\bseo\b", r"funnel", r"metrics", r"instrumentation")),
    ("CMS & publishing", (r"\bcms\b", r"confluence", r"publishing", r"boilerplate", r"content matrix")),
    ("Templates & page systems", (r"template", r"layout system", r"responsive", r"breakpoint")),
    ("Navigation & hubs", (r"\bhub\b", r"navigation", r"breadcrumb", r"tab switcher", r"wayfinding")),
    ("Information architecture", (r"information architecture", r"\bia\b", r"sitemap", r"taxonomy")),
    ("Visual design & theming", (r"typography", r"palette", r"theme", r"visual polish", r"skin\b")),
    ("Integrations & APIs", (r"\bapi\b", r"integration", r"oauth", r"webhook")),
    ("Domains, hosting & deploy", (r"\bdns\b", r"domain", r"hosting", r"\bssl\b", r"\bcdn\b", r"deploy")),
    ("Copywriting & messaging", (r"copywriting", r"microcopy", r"messaging", r"value prop")),
    ("Branding & identity", (r"branding", r"\blogo\b", r"brand identity")),
    ("Quest & journal systems", (r"\bquest\b", r"journal", r"quest tracker", r"dependency chart")),
    ("HUD & objectives", (r"\bhud\b", r"objective", r"\bcompass\b", r"notification", r"toast")),
    ("Inventory & equipment", (r"inventory", r"loadout", r"\bmod\b menu", r"equipment", r"gear\b")),
    ("Map & world navigation", (r"\bmap\b", r"waypoint", r"fast travel", r"nav-assist", r"zone\b")),
    ("Video & motion", (r"\bvideo\b", r"motion", r"animation", r"cinematic")),
    ("Workshops & talks", (r"workshop", r"\btalk\b", r"lecture", r"\bpanel\b")),
    ("Generative & ML art", (r"deepdream", r"neural", r"model training", r"\bgan\b")),
    ("Immersive & installation", (r"immersive", r"cinechamber", r"projection", r"niagara", r"sequencer")),
    ("Audio & hardware studio", (r"\brack\b", r"\baudio\b", r"midi", r"cable map", r"controller")),
    ("Accessibility", (r"a11y", r"accessibility", r"screen reader", r"wcag")),
    ("Documentation & specs", (r"documentation", r"design doc", r"spec\b", r"readme", r"style guide")),
    ("Prototyping & wireframes", (r"prototype", r"wireframe", r"mock-?up", r"figma", r"\bxd\b")),
    ("Presentations & critiques", (r"presentation", r"slide", r"keynote", r"critique", r"town hall")),
    ("Meetings & coordination", (r"1:1", r"stand-?up", r"\bmeeting\b", r"sync\b", r"retro")),
    ("Engineering handoff", (r"handoff", r"export", r"developer", r"implementation")),
    ("Infrastructure & scripts", (r"script", r"automate", r"pipeline", r"docker", r"backup", r"migration")),
    ("Research & discovery", (r"\bspike\b", r"research", r"evaluate", r"survey")),
]

# Extra rules evaluated before ACTIVITY_RULES for specific project tags.
PROJECT_PREFIX_RULES: Dict[str, List[Tuple[str, Tuple[str, ...]]]] = {
    "ESO-Platform": [
        ("Marketing & player-facing web", (r"player guide", r"marketing web", r"elderscrollsonline", r"buy crow")),
    ],
    "Portfolio": [
        ("Site build & CMS", (r"flywheel", r"squarespace", r"wordpress", r"portfolio site")),
    ],
    "OPS": [
        ("Keyboard & desk hardware", (r"keyboard", r"switch\b", r"desk setup")),
    ],
    "Project Ansible": [
        ("Rack & cabling", (r"rack", r"cable", r"patch", r"zone 2")),
    ],
}


def classify_activity(project_tag: str, description: str) -> str:
    dm = DELIV_RE.search(description)
    if dm:
        key = dm.group(1).lower()
        if key in _DELIV_BUCKET:
            return _DELIV_BUCKET[key]
    lowered = description.lower()
    chain: List[Tuple[str, Tuple[str, ...]]] = list(PROJECT_PREFIX_RULES.get(project_tag, []))
    chain.extend(ACTIVITY_RULES)
    for name, patterns in chain:
        for pat in patterns:
            if re.search(pat, lowered):
                return name
    return "General & planning"


def markdown_inline_to_tooltip_html(text: str) -> str:
    """Translate a small markdown subset to escaped HTML."""
    escaped = html.escape(text.strip(), quote=False)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"\1", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"\1", escaped)
    return escaped


def markdown_bullet_to_tooltip_html(text: str) -> str:
    """Wrap one markdown bullet as structured HTML for the custom tooltip."""
    body = markdown_inline_to_tooltip_html(text)
    if not body:
        return ""
    return f'<div class="tt-bullet">{body}</div>'


def parse_month_file(path: Path) -> Tuple[str, Counter, Dict[str, Counter], Dict[str, str]]:
    """
    Returns (month_key, tag_totals, per_tag_activity_counts, per_tag_summary_html).
    Each tagged bullet increments one activity bucket from classify_activity (section headers ignored).
    """
    stem = path.stem
    text = path.read_text(encoding="utf-8", errors="replace")
    tag_totals: Counter = Counter()
    tag_activity: Dict[str, Counter] = defaultdict(Counter)
    tag_summary_lines: Dict[str, List[str]] = defaultdict(list)
    last_section_for_tag: Dict[str, str] = {}
    current_section = ""

    for line in text.splitlines():
        sm = SECTION_LINE.match(line)
        if sm:
            current_section = sm.group(1).strip()
            continue
        tm = TAG_LINE.match(line)
        if not tm:
            continue
        raw_tag = tm.group(1).strip()
        if raw_tag not in ALLOWED_PROJECT_TAGS:
            continue
        desc = tm.group(2).strip()
        tag_totals[raw_tag] += 1
        bucket = classify_activity(raw_tag, desc)
        tag_activity[raw_tag][bucket] += 1
        if current_section and last_section_for_tag.get(raw_tag) != current_section:
            tag_summary_lines[raw_tag].append(
                f'<div class="tt-section-title">{html.escape(current_section)}</div>'
            )
            last_section_for_tag[raw_tag] = current_section
        tag_summary_lines[raw_tag].append(markdown_bullet_to_tooltip_html(desc))

    return stem, tag_totals, dict(tag_activity), {k: "".join(v) for k, v in tag_summary_lines.items()}


def _count_to_intensity(s: int, max_s: int) -> int:
    """Single count vs row/column max → 0–3 (shared by dominance and volume modes)."""
    if s <= 0 or max_s <= 0:
        return 0
    if s == max_s:
        return 3
    if s >= max(2, int(max_s * 0.45 + 0.999)):
        return 2
    return 1


def compute_intensity_row(month_scores: Dict[str, int], projects: List[str]) -> List[int]:
    """Per month: compare projects (whoever has max bullets that month → 3)."""
    scores = [month_scores.get(p, 0) for p in projects]
    max_s = max(scores) if scores else 0
    return [_count_to_intensity(s, max_s) for s in scores]


def intensity_row_from_own_series(counts: List[int]) -> List[int]:
    """Per project: rank active months by bullet count, assign ~lower/middle/upper third → 1/2/3.

    Spreads shade variation along the row even when raw counts cluster (e.g. many similar months
    and one outlier). Zeros stay 0.
    """
    n = len(counts)
    active_idx = [i for i, c in enumerate(counts) if c > 0]
    if not active_idx:
        return [0] * n
    active_idx.sort(key=lambda i: (counts[i], i))
    L = len(active_idx)
    out = [0] * n
    for rank, mi in enumerate(active_idx):
        if rank * 3 < L:
            out[mi] = 1
        elif rank * 3 < 2 * L:
            out[mi] = 2
        else:
            out[mi] = 3
    return out


def format_top_activities(act_counts: Dict[str, int], limit: int = 6) -> str:
    if not act_counts:
        return ""
    items = sorted(act_counts.items(), key=lambda kv: (-kv[1], kv[0].lower()))
    top = items[:limit]
    body = ", ".join(f"{label} {n}" for label, n in top)
    return f"Top activities: {body}"


def top_activity_rows(act_counts: Dict[str, int], limit: int = 3) -> List[Dict[str, Any]]:
    """Structured rows for matrix tooltips (label + count); only top `limit` by count."""
    if not act_counts:
        return []
    items = sorted(act_counts.items(), key=lambda kv: (-kv[1], kv[0].lower()))
    return [{"label": lbl, "n": int(n)} for lbl, n in items[:limit]]


def month_activity_label(month_scores: Dict[str, int], projects: List[str]) -> str:
    if sum(month_scores.values()) == 0:
        return "No tagged project bullets this month."
    ordered = sorted(
        ((p, month_scores.get(p, 0)) for p in projects if month_scores.get(p, 0) > 0),
        key=lambda x: -x[1],
    )
    names = [f"{DISPLAY_NAMES.get(p, p)}" for p, _ in ordered[:6]]
    if len(ordered) > 6:
        names.append("…")
    return "Active projects: " + ", ".join(names)


def strict_flags_for_text(text: str) -> Tuple[int, int, int]:
    return (
        1 if PROTO_RE.search(text) else 0,
        1 if PRES_RE.search(text) else 0,
        1 if PDF_RE.search(text) else 0,
    )


def dominant_runs(months: List[str], projects: List[str], project_scores: Dict[str, List[int]]) -> List[List[str]]:
    """Longest stretches where a project had the raw bullet max that month (independent of heatmap mode)."""
    n = len(months)
    proj_by_month: List[str] = []
    for mi in range(n):
        best = max((project_scores[p][mi] for p in projects), default=0)
        if best <= 0:
            proj_by_month.append("__low__")
            continue
        leaders = [p for p in projects if project_scores[p][mi] == best]
        proj_by_month.append(leaders[0])

    runs: List[List[str]] = []
    i = 0
    while i < n:
        p = proj_by_month[i]
        j = i
        while j < n and proj_by_month[j] == p:
            j += 1
        label = "Low-signal month" if p == "__low__" else DISPLAY_NAMES.get(p, p)
        runs.append([months[i], months[j - 1], label])
        i = j
    return runs


def build_payload(summaries_dir: Path, intensity_mode: str = "volume") -> Dict[str, Any]:
    files = sorted(summaries_dir.glob("*.md"))
    months: List[str] = []
    per_month_tags: List[Dict[str, Counter]] = []
    per_month_activities: List[Dict[str, Dict[str, int]]] = []
    per_month_summary_html: List[Dict[str, str]] = []
    strict_proto: List[int] = []
    strict_pres: List[int] = []
    strict_pdf: List[int] = []

    grand_totals: Counter = Counter()

    for path in files:
        month, tag_totals, tag_act, tag_summary_html = parse_month_file(path)
        months.append(month)
        per_month_tags.append(tag_totals)
        per_month_activities.append({k: dict(v) for k, v in tag_act.items()})
        per_month_summary_html.append(tag_summary_html)
        grand_totals.update(tag_totals)
        text = path.read_text(encoding="utf-8", errors="replace")
        p, r, d = strict_flags_for_text(text)
        strict_proto.append(p)
        strict_pres.append(r)
        strict_pdf.append(d)

    projects = [p for p in ROW_ORDER if p in ALLOWED_PROJECT_TAGS and grand_totals[p] > 0]
    if not projects:
        projects = [p for p in ROW_ORDER if p in ALLOWED_PROJECT_TAGS]

    n = len(months)
    project_scores: Dict[str, List[int]] = {p: [0] * n for p in projects}
    activity_hints: Dict[str, List[str]] = {p: [""] * n for p in projects}
    activity_top_rows: Dict[str, List[List[Dict[str, Any]]]] = {p: [[] for _ in range(n)] for p in projects}
    project_summary_html: Dict[str, List[str]] = {p: [""] * n for p in projects}
    month_notes: Dict[str, str] = {}

    for mi, month in enumerate(months):
        month_scores = {p: int(per_month_tags[mi].get(p, 0)) for p in projects}
        for p in projects:
            project_scores[p][mi] = month_scores[p]
            act_map = per_month_activities[mi].get(p, {})
            activity_hints[p][mi] = format_top_activities(act_map)
            activity_top_rows[p][mi] = top_activity_rows(act_map)
            project_summary_html[p][mi] = per_month_summary_html[mi].get(p, "")
        month_notes[month] = month_activity_label(month_scores, projects)

    intensity: List[List[int]] = []
    if intensity_mode == "dominance":
        for p in projects:
            row = []
            for mi in range(n):
                ms = {proj: project_scores[proj][mi] for proj in projects}
                row.append(compute_intensity_row(ms, projects)[projects.index(p)])
            intensity.append(row)
    elif intensity_mode == "volume":
        for p in projects:
            series = [project_scores[p][mi] for mi in range(n)]
            intensity.append(intensity_row_from_own_series(series))
    else:
        raise ValueError(f"Unknown intensity_mode: {intensity_mode!r}")

    efforts = [None] * n

    project_activities: Dict[str, List[Dict[str, Any]]] = {}
    for p in projects:
        activity_monthly: Dict[str, List[int]] = defaultdict(lambda: [0] * n)
        for mi in range(n):
            for act_name, c in per_month_activities[mi].get(p, {}).items():
                activity_monthly[act_name][mi] += c
        activities = []
        for act_name, monthly in activity_monthly.items():
            total = sum(monthly)
            if total <= 0:
                continue
            active_months = sum(1 for v in monthly if v > 0)
            activities.append(
                {
                    "name": act_name,
                    "total": total,
                    "activeMonths": active_months,
                    "monthly": monthly,
                }
            )
        activities.sort(
            key=lambda a: (
                -a["activeMonths"],
                -a["total"],
                a["name"].lower(),
            )
        )
        project_activities[p] = activities

    # Match Plotly heatmap xgap (~2) + cell body (~40px) in project-matrix-all-summaries.html.
    cell_w, gap = 40, 2
    heat_w = n * (cell_w + gap) + 80

    best_proj = max(projects, key=lambda pr: sum(project_scores[pr]))
    dom = dominant_runs(months, projects, project_scores)

    descriptions = {DISPLAY_NAMES[p]: DESCRIPTIONS.get(p, "") for p in projects}

    return {
        "months": months,
        "rows": [DISPLAY_NAMES[p] for p in projects],
        "_project_slugs": projects,
        "intensity": intensity,
        "efforts": efforts,
        "strictProto": strict_proto,
        "strictPres": strict_pres,
        "strictPdf": strict_pdf,
        "monthNotes": month_notes,
        "descriptions": descriptions,
        "projectScores": {DISPLAY_NAMES[p]: project_scores[p] for p in projects},
        "projectActivities": {DISPLAY_NAMES[p]: project_activities[p] for p in projects},
        "activityHints": {DISPLAY_NAMES[p]: activity_hints[p] for p in projects},
        "activityTopRows": {DISPLAY_NAMES[p]: activity_top_rows[p] for p in projects},
        "projectSummaryHtml": {DISPLAY_NAMES[p]: project_summary_html[p] for p in projects},
        "xticks": months[:: max(1, n // 12)] if n else [],
        "xticktext": months[:: max(1, n // 12)] if n else [],
        "heatWidth": heat_w,
        "mileWidth": heat_w,
        "coverageStart": months[0] if months else "",
        "coverageEnd": months[-1] if months else "",
        "summaryCount": len(files),
        "monthsWithEffort": sum(1 for e in efforts if e is not None),
        "monthsWithMilestones": sum(
            1 for i in range(n) if strict_proto[i] or strict_pres[i] or strict_pdf[i]
        ),
        "dominantRuns": dom,
        "defaultProject": DISPLAY_NAMES[best_proj],
        "intensityMode": intensity_mode,
    }


def strip_builder_only_keys(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys not consumed by the HTML viewer."""
    out = {k: v for k, v in payload.items() if not k.startswith("_")}
    return out


def splice_html(html_path: Path, payload: Dict[str, Any]) -> None:
    text = html_path.read_text(encoding="utf-8")
    start = text.find("const data = ")
    if start < 0:
        raise SystemExit(f"Could not find `const data =` in {html_path}")
    start += len("const data = ")
    end = text.find(";\n    const mileRows", start)
    if end < 0:
        raise SystemExit(f"Could not find splice end marker in {html_path}")
    json_blob = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    new_text = text[:start] + json_blob + text[end:]
    html_path.write_text(new_text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--summaries",
        type=Path,
        default=Path(__file__).resolve().parent / "summaries",
        help="Directory of YYYY-MM.md summaries",
    )
    ap.add_argument(
        "--html",
        type=Path,
        default=Path(__file__).resolve().parent / "visualizations" / "project-matrix-all-summaries.html",
        help="HTML file to patch with generated JSON",
    )
    ap.add_argument("--stdout", action="store_true", help="Print JSON only; do not patch HTML")
    ap.add_argument(
        "--intensity-mode",
        choices=("volume", "dominance"),
        default="volume",
        help="volume (default): each project row scores months vs that project's own peak—more contrast along time. "
        "dominance: each month scores projects against each other—flat row if one project always wins.",
    )
    args = ap.parse_args()

    if not args.summaries.is_dir():
        print(f"Missing summaries directory: {args.summaries}", file=sys.stderr)
        sys.exit(1)

    raw = build_payload(args.summaries, intensity_mode=args.intensity_mode)
    payload = strip_builder_only_keys(raw)

    if args.stdout:
        json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return

    if not args.html.is_file():
        print(f"Missing HTML file: {args.html}", file=sys.stderr)
        sys.exit(1)

    splice_html(args.html, payload)
    print(f"Wrote data -> {args.html} ({payload['summaryCount']} summaries, {len(payload['months'])} months)")


if __name__ == "__main__":
    main()
