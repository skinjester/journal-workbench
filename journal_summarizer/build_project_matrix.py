#!/usr/bin/env python3
"""
Build the `data` payload for `visualizations/project-matrix-all-summaries.html`
from tagged monthly summaries (`summaries/*.md`), plus provenance data for the drill-down page.

Usage (from repo root or this directory):
    python build_project_matrix.py
    python build_project_matrix.py --html visualizations/project-matrix-all-summaries.html
    python build_project_matrix.py --summaries summaries/ --stdout   # inspect JSON only

Each bullet line must look like: - **[TAG]** ... where TAG is in ALLOWED_PROJECT_TAGS
(keep in sync with categorizer.py). Expand rows bucket **line items by description**
(keyword/heuristic activity types), not by summary section headings (### Goals, etc.).

Matrix rows are ordered by **first month with any activity** for that project (earlier starts
higher on the y-axis). Projects that first appear in the same month keep `ROW_ORDER` as tie-breaker.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

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

def first_activity_month_index(project: str, per_month_tags: List[Dict[str, Counter]]) -> int:
    """Index of the first month where `project` has at least one tagged line (0-based)."""
    for mi, tags in enumerate(per_month_tags):
        if int(tags.get(project, 0)) > 0:
            return mi
    return len(per_month_tags)


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

# Ordered lifecycle stages for tooltips (explore → ship). Counts come from line text + activity buckets.
LIFECYCLE_STAGE_KEYS: Tuple[str, ...] = (
    "explore",
    "design",
    "prototype",
    "present",
    "ship",
)


def _empty_lifecycle_counts() -> Dict[str, int]:
    return {k: 0 for k in LIFECYCLE_STAGE_KEYS}


# `deliv:` tags override coarse bucket→stage when present (outcomes vs exploration).
_DELIV_LIFECYCLE: Dict[str, str] = {
    "prototype": "prototype",
    "presentation": "present",
    "visuals": "ship",
    "documentation": "ship",
    "operations": "ship",
    "design-system": "design",
    "audit": "explore",
}

# Map classify_activity() bucket labels → lifecycle stage (single line item → one stage).
_ACTIVITY_BUCKET_LIFECYCLE: Dict[str, str] = {
    "General & planning": "explore",
    "Research & discovery": "explore",
    "Meetings & coordination": "explore",
    "Recruiting & studio site": "explore",
    "Community & social surfaces": "explore",
    "Generative & ML art": "explore",
    "Audio & hardware studio": "explore",
    "Keyboard & desk hardware": "explore",
    "Rack & cabling": "explore",
    "Marketing & player-facing web": "ship",
    "Site build & CMS": "ship",
    "Visual design & wireframes": "design",
    "Information architecture": "design",
    "Templates & page systems": "design",
    "Navigation & hubs": "design",
    "Visual design & theming": "design",
    "Branding & identity": "design",
    "Copywriting & messaging": "design",
    "Accessibility": "design",
    "Design systems & components": "design",
    "Quest & journal systems": "design",
    "HUD & objectives": "design",
    "Inventory & equipment": "design",
    "Map & world navigation": "design",
    "Video & motion": "design",
    "Immersive & installation": "prototype",
    "Prototyping & wireframes": "prototype",
    "Prototyping & experiments": "prototype",
    "Presentations & deck work": "present",
    "Presentations & critiques": "present",
    "Workshops & talks": "present",
    "Documentation & specs": "ship",
    "Engineering handoff": "ship",
    "Domains, hosting & deploy": "ship",
    "CMS & publishing": "ship",
    "Integrations & APIs": "ship",
    "Infrastructure & scripts": "ship",
    "Store & monetization": "ship",
    "Email & newsletters": "ship",
    "Analytics & measurement": "ship",
    "Research & audits": "explore",
    "Operations & runbooks": "ship",
}

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

# Timeline rows (order = top → bottom in the chart). Aligns with CURSOR_SYNTHESIS_INSTRUCTIONS deliv slugs + pdf.
DELIV_MILESTONE_SLUGS: Tuple[str, ...] = (
    "audit",
    "documentation",
    "design-system",
    "visuals",
    "prototype",
    "presentation",
    "operations",
    "pdf",
)

DELIV_MILESTONE_LABELS: Dict[str, str] = {
    "audit": "Audit",
    "documentation": "Documentation",
    "design-system": "Design system",
    "visuals": "Visuals",
    "prototype": "Prototype",
    "presentation": "Presentation",
    "operations": "Operations",
    "pdf": "PDF",
}

DELIV_MILESTONE_HOVER: Dict[str, str] = {
    "audit": "Month includes <code>deliv:audit</code> (audits, comparisons, capture reviews, surveys).",
    "documentation": "Month includes <code>deliv:documentation</code> (specs, Confluence, diagrams-as-spec, handoff).",
    "design-system": "Month includes <code>deliv:design-system</code> (styleguides, UI kits, pattern libraries).",
    "visuals": "Month includes <code>deliv:visuals</code> (stills/motion, comps, exports, non-interactive visuals).",
    "prototype": "Month includes <code>deliv:prototype</code> or prototype/wireframe vocabulary (legacy cue).",
    "presentation": "Month includes <code>deliv:presentation</code> or deck/slides vocabulary (legacy cue).",
    "operations": "Month includes <code>deliv:operations</code> (infra, DNS, rack, invoices, migrations).",
    "pdf": "Month includes <code>deliv:pdf</code> or mentions PDF / <code>.pdf</code> (legacy cue).",
}


def deliv_milestone_hits_per_month(
    per_month_full_text: List[str],
    strict_proto: List[int],
    strict_pres: List[int],
    strict_pdf: List[int],
) -> Dict[str, List[int]]:
    """One row per deliverable slug: 1 if that month’s summary has the tag (or merged legacy cues)."""
    n = len(per_month_full_text)
    slugs = DELIV_MILESTONE_SLUGS
    hits: Dict[str, List[int]] = {s: [0] * n for s in slugs}
    for i, text in enumerate(per_month_full_text):
        seen: Set[str] = set()
        for m in DELIV_RE.finditer(text):
            key = m.group(1).lower().replace("_", "-")
            if key in hits:
                seen.add(key)
        for k in seen:
            hits[k][i] = 1
        if strict_proto[i]:
            hits["prototype"][i] = 1
        if strict_pres[i]:
            hits["presentation"][i] = 1
        if strict_pdf[i]:
            hits["pdf"][i] = 1
    return hits


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
    ("Operations & runbooks", (r"runbook", r"checklist", r"speed test", r"gateway", r"router", r"disk management", r"mount point", r"drive letter", r"filesystem")),
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
    ("Documentation & specs", (r"documentation", r"design doc", r"spec\b", r"readme", r"style guide", r"status doc", r"audit summary", r"acceptance criteria", r"implementation notes")),
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
        ("Operations & runbooks", (r"nas", r"drive", r"migration", r"backup", r"restore", r"throughput", r"bandwidth", r"disk", r"users/gary")),
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


def lifecycle_stage_for_line(project_tag: str, description: str) -> str:
    dm = DELIV_RE.search(description)
    if dm:
        k = dm.group(1).lower()
        if k in _DELIV_LIFECYCLE:
            return _DELIV_LIFECYCLE[k]
    bucket = classify_activity(project_tag, description)
    return _ACTIVITY_BUCKET_LIFECYCLE.get(bucket, "explore")


def markdown_inline_to_tooltip_html(text: str) -> str:
    """Translate a small markdown subset to escaped HTML."""
    escaped = html.escape(text.strip(), quote=False)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"\1", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"\1", escaped)
    return escaped


def extract_closing_paragraph_html(text: str) -> str:
    """Return the final summary paragraph after the closing rule, if present."""
    tail = text.split("---")[-1].strip()
    if not tail:
        return ""
    blocks = [block.strip() for block in re.split(r"\n\s*\n", tail) if block.strip()]
    if not blocks:
        return ""
    return f'<div class="tt-closing">{markdown_inline_to_tooltip_html(blocks[-1])}</div>'


def parse_month_file(
    path: Path,
) -> Tuple[
    str,
    str,
    Counter,
    Dict[str, Counter],
    str,
    Dict[str, Dict[str, int]],
    Dict[str, Dict[str, List[str]]],
]:
    """
    Returns (
        month_key,
        full_file_text,
        tag_totals,
        per_tag_activity_counts,
        closing_paragraph_html,
        per_tag_lifecycle_counts,
        per_tag_activity_lines (verbatim bullet lines per activity bucket),
    ).
    """
    stem = path.stem
    text = path.read_text(encoding="utf-8", errors="replace")
    tag_totals: Counter = Counter()
    tag_activity: Dict[str, Counter] = defaultdict(Counter)
    tag_lifecycle: Dict[str, Dict[str, int]] = defaultdict(_empty_lifecycle_counts)
    tag_activity_lines: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    closing_paragraph_html = extract_closing_paragraph_html(text)

    for line in text.splitlines():
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
        stage = lifecycle_stage_for_line(raw_tag, desc)
        tag_lifecycle[raw_tag][stage] += 1
        tag_activity_lines[raw_tag][bucket].append(line.rstrip("\n"))

    lines_out: Dict[str, Dict[str, List[str]]] = {
        tag: {act: list(lines) for act, lines in acts.items()}
        for tag, acts in tag_activity_lines.items()
    }
    return stem, text, tag_totals, dict(tag_activity), closing_paragraph_html, dict(tag_lifecycle), lines_out


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
    per_month_full_text: List[str] = []
    per_month_tag_activity_lines: List[Dict[str, Dict[str, List[str]]]] = []
    per_month_tags: List[Dict[str, Counter]] = []
    per_month_activities: List[Dict[str, Dict[str, int]]] = []
    month_closing_html: List[str] = []
    per_month_tag_lifecycle: List[Dict[str, Dict[str, int]]] = []
    strict_proto: List[int] = []
    strict_pres: List[int] = []
    strict_pdf: List[int] = []

    grand_totals: Counter = Counter()

    for path in files:
        month, full_text, tag_totals, tag_act, closing_html, tag_lc, tag_lines = parse_month_file(path)
        months.append(month)
        per_month_full_text.append(full_text)
        per_month_tag_activity_lines.append(tag_lines)
        per_month_tags.append(tag_totals)
        per_month_activities.append({k: dict(v) for k, v in tag_act.items()})
        month_closing_html.append(closing_html)
        per_month_tag_lifecycle.append(tag_lc)
        grand_totals.update(tag_totals)
        p, r, d = strict_flags_for_text(full_text)
        strict_proto.append(p)
        strict_pres.append(r)
        strict_pdf.append(d)

    deliv_milestone_hits = deliv_milestone_hits_per_month(
        per_month_full_text, strict_proto, strict_pres, strict_pdf
    )

    projects = [p for p in ROW_ORDER if p in ALLOWED_PROJECT_TAGS and grand_totals[p] > 0]
    if not projects:
        projects = [p for p in ROW_ORDER if p in ALLOWED_PROJECT_TAGS]
    row_order_rank = {p: i for i, p in enumerate(ROW_ORDER)}
    projects.sort(
        key=lambda p: (
            first_activity_month_index(p, per_month_tags),
            row_order_rank.get(p, 10**6),
        )
    )

    n = len(months)
    project_scores: Dict[str, List[int]] = {p: [0] * n for p in projects}
    activity_hints: Dict[str, List[str]] = {p: [""] * n for p in projects}
    activity_top_rows: Dict[str, List[List[Dict[str, Any]]]] = {p: [[] for _ in range(n)] for p in projects}
    month_notes: Dict[str, str] = {}
    project_lifecycle_counts: Dict[str, List[Dict[str, int]]] = {
        DISPLAY_NAMES[p]: [_empty_lifecycle_counts() for _ in range(n)] for p in projects
    }

    for mi, month in enumerate(months):
        month_scores = {p: int(per_month_tags[mi].get(p, 0)) for p in projects}
        for p in projects:
            project_scores[p][mi] = month_scores[p]
            act_map = per_month_activities[mi].get(p, {})
            activity_hints[p][mi] = format_top_activities(act_map)
            activity_top_rows[p][mi] = top_activity_rows(act_map)
            lc_src = per_month_tag_lifecycle[mi].get(p)
            if lc_src:
                dest = project_lifecycle_counts[DISPLAY_NAMES[p]][mi]
                for k in LIFECYCLE_STAGE_KEYS:
                    dest[k] = int(lc_src.get(k, 0))
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

    month_sources: Dict[str, str] = {months[i]: per_month_full_text[i] for i in range(n)}
    activity_provenance: Dict[str, Dict[str, List[List[str]]]] = {}
    for p in projects:
        dname = DISPLAY_NAMES[p]
        activity_provenance[dname] = {}
        for act in project_activities[p]:
            act_name = act["name"]
            activity_provenance[dname][act_name] = [
                list(per_month_tag_activity_lines[mi].get(p, {}).get(act_name, []))
                for mi in range(n)
            ]

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
        "delivMilestoneSlugs": list(DELIV_MILESTONE_SLUGS),
        "delivMilestoneLabels": DELIV_MILESTONE_LABELS,
        "delivMilestoneHits": deliv_milestone_hits,
        "delivMilestoneHover": DELIV_MILESTONE_HOVER,
        "monthNotes": month_notes,
        "descriptions": descriptions,
        "projectScores": {DISPLAY_NAMES[p]: project_scores[p] for p in projects},
        "projectActivities": {DISPLAY_NAMES[p]: project_activities[p] for p in projects},
        "monthSources": month_sources,
        "activityProvenance": activity_provenance,
        "activityHints": {DISPLAY_NAMES[p]: activity_hints[p] for p in projects},
        "activityTopRows": {DISPLAY_NAMES[p]: activity_top_rows[p] for p in projects},
        "monthClosingHtml": month_closing_html,
        "projectLifecycleCounts": {DISPLAY_NAMES[p]: project_lifecycle_counts[DISPLAY_NAMES[p]] for p in projects},
        "lifecycleStageOrder": list(LIFECYCLE_STAGE_KEYS),
        "lifecycleStageLabels": {
            "explore": "Explore & plan",
            "design": "Design & IA",
            "prototype": "Prototype",
            "present": "Present & review",
            "ship": "Ship & deliver",
        },
        "xticks": months[:: max(1, n // 12)] if n else [],
        "xticktext": months[:: max(1, n // 12)] if n else [],
        "heatWidth": heat_w,
        "mileWidth": heat_w,
        "coverageStart": months[0] if months else "",
        "coverageEnd": months[-1] if months else "",
        "summaryCount": len(files),
        "monthsWithEffort": sum(1 for e in efforts if e is not None),
        "monthsWithMilestones": sum(
            1
            for i in range(n)
            if any(deliv_milestone_hits[s][i] for s in DELIV_MILESTONE_SLUGS)
        ),
        "dominantRuns": dom,
        "defaultProject": DISPLAY_NAMES[best_proj],
        "intensityMode": intensity_mode,
    }


def strip_builder_only_keys(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys not consumed by the HTML viewer."""
    out = {k: v for k, v in payload.items() if not k.startswith("_")}
    return out


def splice_html(
    html_path: Path, payload: Dict[str, Any], provenance: Dict[str, Any] | None = None
) -> None:
    text = html_path.read_text(encoding="utf-8")
    start = text.find("const data = ")
    if start < 0:
        raise SystemExit(f"Could not find `const data =` in {html_path}")
    start += len("const data = ")
    # Must be the block *after* provenanceData — not `const mileRows` (that line follows
    # `mileSlugs` and its `];` also ends with `;`, so find() would strip `mileSlugs` every run).
    end = text.find(";\n    const mileSlugs", start)
    if end < 0:
        raise SystemExit(
            f"Could not find splice end marker `;\\n    const mileSlugs` in {html_path}"
        )
    json_blob = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    prov_insert = ""
    if provenance is not None:
        prov_json = json.dumps(provenance, separators=(",", ":"), ensure_ascii=False)
        prov_insert = f";\n    const provenanceData = {prov_json}"
    new_text = text[:start] + json_blob + prov_insert + text[end:]
    html_path.write_text(new_text, encoding="utf-8")


def splice_provenance_html(html_path: Path, prov: Dict[str, Any]) -> None:
    text = html_path.read_text(encoding="utf-8")
    start_marker = "const provenanceData = "
    end_marker = "// __PROVENANCE_DATA_END__"
    start = text.find(start_marker)
    if start < 0:
        raise SystemExit(f"Could not find `{start_marker}` in {html_path}")
    start += len(start_marker)
    end = text.find(end_marker, start)
    if end < 0:
        raise SystemExit(f"Could not find `{end_marker}` in {html_path}")
    json_blob = json.dumps(prov, separators=(",", ":"), ensure_ascii=False)
    html_path.write_text(text[:start] + json_blob + text[end:], encoding="utf-8")


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
    ap.add_argument(
        "--provenance",
        type=Path,
        default=Path(__file__).resolve().parent / "visualizations" / "provenance.html",
        help="Provenance drill-down HTML file to patch with monthSources + activityProvenance",
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
    prov_subset = {
        "months": raw["months"],
        "monthSources": raw["monthSources"],
        "activityProvenance": raw["activityProvenance"],
    }
    matrix_raw = {k: v for k, v in raw.items() if k not in ("monthSources", "activityProvenance")}
    payload = strip_builder_only_keys(matrix_raw)

    if args.stdout:
        json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return

    if not args.html.is_file():
        print(f"Missing HTML file: {args.html}", file=sys.stderr)
        sys.exit(1)

    splice_html(args.html, payload, prov_subset)
    if not args.provenance.is_file():
        print(f"Missing provenance HTML: {args.provenance}", file=sys.stderr)
        sys.exit(1)
    splice_provenance_html(args.provenance, prov_subset)
    print(
        f"Wrote data -> {args.html} ({payload['summaryCount']} summaries, {len(payload['months'])} months); "
        f"provenance -> {args.provenance}"
    )


if __name__ == "__main__":
    main()
