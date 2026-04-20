#!/usr/bin/env python3
"""
Write a standalone Plotly HTML dashboard comparing job evaluation tiers.

Charts use `CHART_SCORE_COLUMNS` (PART 5 verdicts + rubric tiers; omits ATS / recruiter hygiene and Risk Factors).

Expects to be imported from `collate_job_evaluations` with the same `sys.path` (scripts directory).
"""

from __future__ import annotations

import datetime as dt
import html as html_module
import re
from collections import Counter
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

import plotly.graph_objects as go

from collate_job_evaluations import (
    CHART_SCORE_COLUMNS,
    SEVEN_STEP_ORDINALS,
    VERDICT_TABLE_COLUMNS,
    CollatedRow,
    _is_mini_family_model,
    rubric_line_to_table_cell,
    tier_cell_to_chart_numeric,
    verdict_line_to_table_cell,
)


MINI_FAMILY_GLYPH = "\u25c7"

# ``Foo.eval - YYYY-MM-DD.md`` or ``… - N.md``; else file mtime → calendar day.
_EVAL_REPORT_DATE_IN_NAME = re.compile(r" - (\d{4}-\d{2}-\d{2})(?: - \d+)?\.md$", re.IGNORECASE)


def _path_for_row_report(repo_root: Path, report_rel: str) -> Path:
    p = (repo_root / report_rel).resolve()
    return p if p.is_file() else Path(report_rel)


def _calendar_date_for_eval_report(path: Path) -> dt.date:
    m = _EVAL_REPORT_DATE_IN_NAME.search(path.name)
    if m:
        try:
            return dt.datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            pass
    try:
        st = path.stat()
        return dt.datetime.fromtimestamp(st.st_mtime, tz=dt.timezone.utc).astimezone().date()
    except (OSError, ValueError):
        return dt.date.today()


def _fig_hero_report_dates(
    rows: Sequence[CollatedRow],
    repo_root: Path,
) -> Tuple[go.Figure, int]:
    """One bar per unique calendar day: height = number of evals whose report maps to that day."""
    c: Counter[dt.date] = Counter()
    for r in rows:
        c[_calendar_date_for_eval_report(_path_for_row_report(repo_root, r.report_rel))] += 1
    ordered = sorted(c.items())
    labels = [d.isoformat() for d, _ in ordered]
    vals = [k for _, k in ordered]
    n = max(1, len(labels))
    y_max = max(vals) if vals else 0
    # Numeric x so we can set range with extra room on the right: bars start at the left
    # (categorical + single day centers one fat bar; linear + padded xmax pins it left).
    x_pos = list(range(n))
    x_max = (n - 1) + 0.5 + 2.75
    # Slender chart: less width per day; narrow bars via bargap + Bar width.
    min_w = int(min(2000, max(320, n * 22 + 140)))
    fig = go.Figure(
        data=go.Bar(
            x=x_pos,
            y=vals,
            width=0.22,
            customdata=labels,
            text=[str(v) for v in vals] if (vals and y_max <= 4) else None,
            textposition="auto",
            textfont=dict(size=8, color=PAGE_BG),
            marker=dict(color=ACCENT, line=dict(width=0), opacity=0.9),
            hovertemplate="%{customdata}<br>Reports: %{y}<extra></extra>",
        )
    )
    # Tight y headroom so the strip stays short; avoid huge empty band above the bar.
    y_hi = (y_max * 1.04 + 0.35) if y_max else 1.0
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.03)",
        margin=dict(l=40, r=2, t=0, b=20),
        height=64,
        width=min_w,
        autosize=False,
        showlegend=False,
        bargap=0.72,
    )
    fig.update_xaxes(
        title=dict(text="Report date", font=dict(size=8, color=MUTED), standoff=2),
        type="linear",
        range=(-0.5, x_max),
        tickmode="array",
        tickvals=x_pos,
        ticktext=labels,
        tickfont=dict(size=7, color=MUTED),
        tickangle=-28 if n > 4 else 0,
        showline=False,
        mirror=False,
        showgrid=True,
        gridcolor="rgba(151,173,210,0.08)",
        automargin=True,
        zeroline=False,
    )
    fig.update_yaxes(
        title=dict(text="Reports", font=dict(size=8, color=MUTED), standoff=2),
        range=(0, y_hi),
        dtick=1 if y_max <= 5 else max(1, (y_max + 2) // 3),
        tickfont=dict(size=7, color=MUTED),
        showline=False,
        showgrid=True,
        gridcolor="rgba(151,173,210,0.1)",
        # Default y=0 "zeroline" reads as a thick white bar along the bottom of the plot.
        zeroline=False,
        rangemode="tozero",
        fixedrange=True,
    )
    return fig, min_w


CHART_SCORE_COLUMN_WEIGHTS: dict[str, float] = {
    "Fit on Paper": 20.0,
    "Capability": 20.0,
    "Narrative Coherence": 20.0,
    "Signal Strength (Recruiter)": 20.0,
    "Signal Strength (HM)": 20.0,
    "Problem Match": 25.0,
    "Relevant Proof": 20.0,
    "Recency": 15.0,
    "Role Readability": 15.0,
    "Differentiation": 10.0,
    "Narrative Coherence (rubric)": 5.0,
}


PAGE_BG = "#0a0f1a"
PANEL_BG = "#101826"
PANEL_BG_ALT = "#0d1422"
BORDER = "rgba(151, 173, 210, 0.16)"
TEXT = "#ecf3ff"
MUTED = "#94a8c6"
ACCENT = "#77e6ff"
ACCENT_2 = "#9b7cff"
SERIES = ["#77e6ff", "#9b7cff", "#55d6be", "#ff8a65", "#ffd166", "#ff6fae", "#64b5f6", "#c3f73a"]

# Grouped bar chart: fill by nearest ordinal (weakest → strongest). Single-hue blue ramp (darker →
# lighter) aligned with ``HEATMAP_MONO_COLORSCALE`` so it matches the dot matrix without extra hues.
ORDINAL_BAR_COLORS: Tuple[str, ...] = (
    "#0f1826",
    "#131f33",
    "#1a2944",
    "#223456",
    "#2c426a",
    "#3a5680",
    "#5c7a9e",
)

# Single-hue blues; stops spaced for roughly equal perceived lightness steps (reads cleanly in grayscale).
HEATMAP_MONO_COLORSCALE: List[Tuple[float, str]] = [
    [0.0, "#070b14"],
    [0.125, "#101e33"],
    [0.25, "#17304c"],
    [0.375, "#214566"],
    [0.5, "#2f5d82"],
    [0.625, "#44769c"],
    [0.75, "#6794b5"],
    [0.875, "#9cb9d4"],
    [1.0, "#dceaf7"],
]


def _heatmap_left_margin_px(jobs: Sequence[str]) -> int:
    """Space for full job titles on the heatmap Y-axis (template default l=56 clips long labels)."""
    if not jobs:
        return 220
    longest = max(len(j) for j in jobs)
    # ~5.2px per character at tick font 10px; snug so no dead space to the left.
    return min(340, max(160, int(longest * 5.2) + 8))


# Dot-matrix column headers: tilted ticks keep columns compact while labels stay readable (no overlap).
HEATMAP_DIM_LABEL_FONT_PX = 9
HEATMAP_X_TICK_ANGLE = -40
# With angled ticks, columns can be narrower than horizontal multi-line headers required.
HEATMAP_WIDTH_PX_PER_CATEGORY = 54
HEATMAP_WIDTH_EXTRA_PX = 260
# Vertical pixels per job row (grid cell); larger = more space between dots and grid lines.
HEATMAP_ROW_HEIGHT_PX = 46

# Grouped horizontal bars: target ~2px-thick stripes; figure height is derived from job count × row budget.
GROUPED_BAR_STRIPE_PX = 2.0
GROUPED_BAR_INNER_GAP_PX = 1.0
GROUPED_BAR_ROW_PAD_PX = 10.0


def _grouped_bar_row_height_px(n_dim: int) -> int:
    """Vertical pixels budget per job row so dimension stripes render near ``GROUPED_BAR_STRIPE_PX`` tall."""
    if n_dim <= 0:
        return 20
    inner = max(0, n_dim - 1) * GROUPED_BAR_INNER_GAP_PX
    return int(n_dim * GROUPED_BAR_STRIPE_PX + inner + GROUPED_BAR_ROW_PAD_PX)


def _heatmap_figure_width_px(n_dims: int) -> int:
    """Figure width so category spacing stays readable; page scrolls horizontally when very wide."""
    return max(700, min(8000, HEATMAP_WIDTH_PX_PER_CATEGORY * n_dims + HEATMAP_WIDTH_EXTRA_PX))


_VERDICT_COLS = frozenset(VERDICT_TABLE_COLUMNS)


def _wrap_dim_label(label: str, max_first_line: int = 8, *, heatmap_ticks: bool = False) -> str:
    """Split a dimension label for multi-line heatmap column headers (HTML <br>)."""
    # Dot matrix: stack "Signal / Strength / (…)" so two adjacent Signal columns do not collide.
    if heatmap_ticks and label.startswith("Signal Strength ("):
        rest = label[len("Signal Strength ") :].lstrip()
        return f"Signal<br>Strength<br>{rest}"
    # Other charts (e.g. dot-plot subplot titles): two lines are enough.
    if label.startswith("Signal Strength ("):
        rest = label[len("Signal Strength ") :].lstrip()
        return f"Signal Strength<br>{rest}"
    # Break before parenthesis so "Foo (rubric)" stacks; reduces horizontal tick overlap.
    if "(" in label:
        idx = label.index("(")
        if idx > 0:
            head, tail = label[:idx].strip(), label[idx:].strip()
            if head:
                return f"{head}<br>{tail}"
    words = label.split()
    if len(words) <= 1 or len(label) <= max_first_line:
        return label
    mid = len(label) // 2
    best_i = 0
    best_dist = float("inf")
    pos = 0
    for i, w in enumerate(words[:-1]):
        pos += len(w) + 1
        dist = abs(pos - mid)
        if dist < best_dist:
            best_dist = dist
            best_i = i
    return " ".join(words[: best_i + 1]) + "<br>" + " ".join(words[best_i + 1 :])


def _with_alpha(hex_color: str, alpha: float) -> str:
    hex_value = hex_color.lstrip("#")
    if len(hex_value) != 6:
        return hex_color
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"


def _studio_template() -> go.layout.Template:
    return go.layout.Template(
        layout=go.Layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color=TEXT, family="Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif", size=12),
            title=dict(x=0.02, xanchor="left", font=dict(size=20, color=TEXT)),
            margin=dict(l=56, r=28, t=32, b=52),
            legend=dict(
                bgcolor="rgba(0,0,0,0)",
                borderwidth=0,
                font=dict(color=MUTED),
                title=dict(font=dict(color=TEXT)),
            ),
            hoverlabel=dict(
                bgcolor="#0b1220",
                bordercolor=_with_alpha(ACCENT, 0.28),
                font=dict(color=TEXT),
            ),
            colorway=SERIES,
            xaxis=dict(
                gridcolor="rgba(151, 173, 210, 0.12)",
                linecolor="rgba(151, 173, 210, 0.18)",
                zerolinecolor="rgba(151, 173, 210, 0.12)",
                tickfont=dict(color=MUTED),
                title=dict(font=dict(color=MUTED)),
            ),
            yaxis=dict(
                gridcolor="rgba(151, 173, 210, 0.12)",
                linecolor="rgba(151, 173, 210, 0.18)",
                zerolinecolor="rgba(151, 173, 210, 0.12)",
                tickfont=dict(color=MUTED),
                title=dict(font=dict(color=MUTED)),
            ),
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                angularaxis=dict(gridcolor="rgba(151, 173, 210, 0.12)", linecolor="rgba(151, 173, 210, 0.18)", tickfont=dict(color=MUTED)),
                radialaxis=dict(gridcolor="rgba(151, 173, 210, 0.12)", linecolor="rgba(151, 173, 210, 0.18)", tickfont=dict(color=MUTED)),
            ),
        )
    )


def _score_matrix(rows: Sequence[CollatedRow]) -> Tuple[List[str], List[str], List[List[Optional[float]]], List[List[str]]]:
    jobs = [r.jd_key for r in rows]
    dims = list(CHART_SCORE_COLUMNS)
    z: List[List[Optional[float]]] = []
    z_text: List[List[str]] = []
    for r in rows:
        row_vals: List[Optional[float]] = []
        row_txt: List[str] = []
        for d in dims:
            if d in _VERDICT_COLS:
                cell = verdict_line_to_table_cell(r.verdicts.get(d, ""), d)
            else:
                cell = rubric_line_to_table_cell(r.rubric.get(d, ""), d)
            row_txt.append(cell if cell.strip() else "—")
            row_vals.append(tier_cell_to_chart_numeric(cell))
        z.append(row_vals)
        z_text.append(row_txt)
    return jobs, dims, z, z_text


def _mean_non_null(values: Sequence[Optional[float]]) -> Optional[float]:
    xs = [v for v in values if v is not None]
    return (sum(xs) / len(xs)) if xs else None


def _weighted_row_score(
    dims: Sequence[str],
    values: Sequence[Optional[float]],
) -> Optional[float]:
    """Weighted mean across chart score columns.

    Rubric columns use the PART 6 template weights (Problem Match 25, Relevant Proof 20,
    Recency 15, Role Readability 15, Differentiation 10, Narrative Coherence rubric 5;
    Risk Factors / ATS are omitted from charts). PART 5 headlines each weight 20 so the
    two halves balance roughly 100 (PART 5 total) vs 90 (rubric subset).
    """
    num = 0.0
    denom = 0.0
    for d, v in zip(dims, values):
        if v is None:
            continue
        w = CHART_SCORE_COLUMN_WEIGHTS.get(d, 1.0)
        num += float(v) * w
        denom += w
    if denom <= 0:
        return None
    return num / denom


# Anchors for mapping batch numeric mean → readable tier label (chart-wide 0–100 encoding).
_MEAN_TIER_ANCHOR_LABELS: Tuple[str, ...] = (
    "Very High",
    "High",
    "Medium-High",
    "Medium",
    "Medium-Low",
    "Low",
    "Very Low",
)


def _mean_numeric_to_nearest_tier_label(avg: float) -> str:
    """Nearest substantive verdict tier to the chart numeric mean (wide 0–100 ordinal map)."""
    if avg <= 0:
        return "—"
    best_label = "—"
    best_dist = float("inf")
    for label in _MEAN_TIER_ANCHOR_LABELS:
        n = tier_cell_to_chart_numeric(label)
        if n is None:
            continue
        dist = abs(avg - n)
        if dist < best_dist:
            best_dist = dist
            best_label = label
    return best_label


def _sort_jobs_for_dot_plots(
    jobs: List[str],
    dims: Sequence[str],
    z: List[List[Optional[float]]],
    z_text: Optional[List[List[str]]],
) -> Tuple[List[str], List[List[Optional[float]]], Optional[List[List[str]]]]:
    """Descending weighted tier score; alphabetical job key for stable ties."""
    order = sorted(
        range(len(jobs)),
        key=lambda i: (-(_weighted_row_score(dims, z[i]) or float("-inf")), jobs[i].lower()),
    )
    jobs2 = [jobs[i] for i in order]
    z2 = [list(z[i]) for i in order]
    zt2 = [list(z_text[i]) for i in order] if z_text else None
    return jobs2, z2, zt2


# Imputed chart score for missing cells in radar (aligned with unknown-tier chart encoding).
_RADAR_MISSING_SCORE = 26.0


def _radar_radial_axis_range() -> Tuple[float, float]:
    """
    Fixed **0–100** radial scale, matching ``tier_cell_to_chart_numeric`` / dot matrix.

    Previously we zoomed to each cohort's min/max so polygons spread out—but then the
    inner edge of the chart was the *cohort minimum*, not numeric zero. A Medium tier
    (~40) sitting near that minimum looked like a "zero" at the origin. Keeping 0–100
    makes radius proportional to the same chart score everywhere.
    """
    return (0.0, 100.0)


# Radar-only: ordinals are placed at equal radial steps. (Dot matrix / color still use the wide
# ``tier_cell_to_chart_numeric`` spread so tiers don’t collapse in other views.)
_RADAR_TIER_STEPS = len(SEVEN_STEP_ORDINALS) - 1  # 6 intervals between 7 tiers on 0–100


def _tier_index_to_equal_radar_radius(idx: int) -> float:
    """Map tier index 0..6 to equally spaced radii 0..100 (Very Low → Very High)."""
    return (100.0 / float(_RADAR_TIER_STEPS)) * float(idx)


def _radar_equal_radial_ticks() -> Tuple[List[float], List[str]]:
    """Seven concentric rings at equal spacing; outer ring has no label (avoids clutter at 100)."""
    vals = [_tier_index_to_equal_radar_radius(i) for i in range(len(SEVEN_STEP_ORDINALS))]
    texts = list(SEVEN_STEP_ORDINALS)
    if texts:
        texts[-1] = ""
    return vals, texts


def _chart_score_to_nearest_tier_index(score: float) -> int:
    """Nearest substantive tier index 0..6 for a chart numeric (wide spread)."""
    best_i = 0
    best_d = float("inf")
    for i, label in enumerate(SEVEN_STEP_ORDINALS):
        n = tier_cell_to_chart_numeric(label)
        if n is None:
            continue
        d = abs(score - n)
        if d < best_d:
            best_d = d
            best_i = i
    return best_i


def _bar_color_for_chart_score(score: Optional[float]) -> str:
    """Solid fill for grouped horizontal bars from chart numeric (same map as dot matrix)."""
    if score is None:
        return "#2a3344"
    return ORDINAL_BAR_COLORS[_chart_score_to_nearest_tier_index(float(score))]


def _dim_short_legend(dim: str, max_len: int = 26) -> str:
    d = dim.strip()
    if len(d) <= max_len:
        return d
    return d[: max_len - 1] + "…"


def _chart_score_to_ordinal_hover_label(score: float) -> str:
    """Radar hover: show tier name for mapped chart scores; keep numeric fallback."""
    for label in SEVEN_STEP_ORDINALS:
        n = tier_cell_to_chart_numeric(label)
        if n is not None and abs(score - n) < 0.05:
            return label
    if abs(score - _RADAR_MISSING_SCORE) < 0.05:
        return "—"
    return f"{score:.0f}"


def _best_overall_job(
    jobs: Sequence[str],
    dims: Sequence[str],
    z: Sequence[Sequence[Optional[float]]],
) -> str:
    """Job with the highest weighted tier score across dimensions."""
    best_job = jobs[0]
    best_avg = -1.0
    for i, job in enumerate(jobs):
        avg = _weighted_row_score(dims, z[i])
        if avg is not None and avg > best_avg:
            best_avg = avg
            best_job = job
    return best_job


def _lowest_overall_job(
    jobs: Sequence[str],
    dims: Sequence[str],
    z: Sequence[Sequence[Optional[float]]],
) -> str:
    """Job with the lowest weighted tier score across dimensions."""
    worst_job = jobs[0]
    worst_avg = float("inf")
    for i, job in enumerate(jobs):
        avg = _weighted_row_score(dims, z[i])
        if avg is not None and avg < worst_avg:
            worst_avg = avg
            worst_job = job
    return worst_job


# Dot matrix: marker diameter (px) per **nearest ordinal** (Very Low → Very High). Discrete steps
# make tier differences obvious at a glance; color still encodes the continuous chart score.
_DOT_MATRIX_TIER_MARKER_SIZES_PX: Tuple[float, ...] = (
    6.5,
    9.5,
    13.0,
    17.5,
    23.0,
    30.0,
    39.0,
)
# Chart encoding for missing / unparsed cells (matches unknown-tier spread in tier_cell_to_chart_numeric).
_HEATMAP_MISSING_SCORE = 26.0


def _fig_heatmap(jobs: List[str], dims: List[str], z: List[List[Optional[float]]], z_text: List[List[str]]) -> go.Figure:
    """
    Dot matrix: each cell is a circle whose **color** encodes the chart tier score (0–100) and
    **size** encodes the nearest ordinal tier (discrete steps) so adjacent tiers read clearly.
    """
    COLOR_LO, COLOR_HI = 0.0, 100.0

    # Angled ticks: use lighter wrapping (tall multi-line + rotation eats top margin). Horizontal (angle≈0):
    # use heatmap_ticks=True so adjacent "Signal Strength" columns stack narrower.
    if abs(HEATMAP_X_TICK_ANGLE) < 1.0:
        wrapped_dims = [_wrap_dim_label(d, max_first_line=6, heatmap_ticks=True) for d in dims]
    else:
        wrapped_dims = [_wrap_dim_label(d, max_first_line=11, heatmap_ticks=False) for d in dims]

    xs: List[str] = []
    ys: List[str] = []
    sizes: List[float] = []
    colors: List[float] = []
    hovers: List[str] = []

    for i, job in enumerate(jobs):
        for j, dim in enumerate(dims):
            v = z[i][j]
            score = float(v) if v is not None else _HEATMAP_MISSING_SCORE
            tier_i = _chart_score_to_nearest_tier_index(score)
            sz = _DOT_MATRIX_TIER_MARKER_SIZES_PX[tier_i]
            tier_label = (z_text[i][j] if z_text and i < len(z_text) and j < len(z_text[i]) else "—") or "—"
            xs.append(dim)
            ys.append(job)
            sizes.append(sz)
            colors.append(score)
            hovers.append(f"{job}<br>{dim}<br>{tier_label}<extra></extra>")

    fig = go.Figure(
        data=go.Scatter(
            x=xs,
            y=ys,
            mode="markers",
            marker=dict(
                size=sizes,
                color=colors,
                colorscale=HEATMAP_MONO_COLORSCALE,
                cmin=COLOR_LO,
                cmax=COLOR_HI,
                showscale=False,
                line=dict(width=0),
            ),
            hovertemplate=hovers,
            showlegend=False,
        )
    )

    fig.update_layout(
        height=max(400, HEATMAP_ROW_HEIGHT_PX * len(jobs) + 200),
        xaxis=dict(
            side="top",
            tickangle=HEATMAP_X_TICK_ANGLE,
            tickmode="array",
            tickvals=dims,
            ticktext=wrapped_dims,
            tickfont=dict(size=HEATMAP_DIM_LABEL_FONT_PX, color=MUTED),
            showgrid=True,
            gridcolor="rgba(151,173,210,0.10)",
            zeroline=False,
            automargin=True,
        ),
        yaxis=dict(
            tickfont=dict(size=10),
            autorange="reversed",
            showgrid=True,
            gridcolor="rgba(151,173,210,0.10)",
            zeroline=False,
        ),
    )
    return fig


def _fig_radar(jobs: List[str], dims: List[str], z: List[List[Optional[float]]]) -> go.Figure:
    r0, r1 = _radar_radial_axis_range()
    rticks, rtext = _radar_equal_radial_ticks()
    fig = go.Figure()
    theta = list(dims) + [dims[0]]
    for i, job in enumerate(jobs):
        r_raw = [z[i][j] if z[i][j] is not None else _RADAR_MISSING_SCORE for j in range(len(dims))]
        r_plot = [
            _tier_index_to_equal_radar_radius(_chart_score_to_nearest_tier_index(float(v)))
            for v in r_raw
        ]
        r_closed = r_plot + [r_plot[0]]
        hover_labs = [_chart_score_to_ordinal_hover_label(float(v)) for v in (r_raw + [r_raw[0]])]
        color = SERIES[i % len(SERIES)]
        fig.add_trace(
            go.Scatterpolar(
                r=r_closed,
                theta=theta,
                customdata=hover_labs,
                mode="lines",
                name=job[:48] + ("…" if len(job) > 48 else ""),
                line=dict(color=color, width=2),
                fill="toself",
                fillcolor=_with_alpha(color, 0.08),
                opacity=0.72,
                hovertemplate="%{fullData.name}<br>%{theta}: %{customdata}<extra></extra>",
            )
        )
    fig.update_layout(
        polar=dict(
            # Shrink the polar plot area so long angular labels (e.g. "Signal Strength (Recruiter)")
            # live in the surrounding gutter instead of overlapping the polygon.
            domain=dict(x=[0.02, 0.62], y=[0.08, 0.94]),
            radialaxis=dict(
                visible=True,
                range=[r0, r1],
                tickmode="array",
                tickvals=rticks,
                ticktext=rtext,
                tickangle=90,
                tickfont=dict(size=9, color=MUTED),
            ),
            angularaxis=dict(
                tickfont=dict(size=10, color=MUTED),
            ),
        ),
        height=560,
        # Explicit margins so angular labels on every side have room; legend on the right
        # gets its own column via the polar domain above.
        margin=dict(l=110, r=40, t=28, b=60),
        legend=dict(
            x=0.66,
            y=0.5,
            xanchor="left",
            yanchor="middle",
            tracegroupgap=0,
            font=dict(size=9),
            itemclick="toggle",
            itemdoubleclick="toggleothers",
        ),
    )
    return fig


def _fig_job_grouped_bars(
    jobs: List[str],
    dims: List[str],
    z: List[List[Optional[float]]],
    z_text: Optional[List[List[str]]] = None,
) -> go.Figure:
    """Grouped horizontal bars: one row per job, one bar per dimension; length = chart score; color = ordinal tier."""
    jobs, z, z_text = _sort_jobs_for_dot_plots(jobs, dims, z, z_text)
    fig = go.Figure()
    for j, dim in enumerate(dims):
        xs: List[float] = []
        colors: List[str] = []
        custom: List[str] = []
        for i in range(len(jobs)):
            raw = z[i][j]
            score = float(raw) if raw is not None else _HEATMAP_MISSING_SCORE
            xs.append(score)
            colors.append(_bar_color_for_chart_score(raw))
            if z_text:
                tier = (z_text[i][j] if j < len(z_text[i]) else "—") or "—"
            else:
                tier = _chart_score_to_ordinal_hover_label(score)
            custom.append(tier)
        fig.add_trace(
            go.Bar(
                name=_dim_short_legend(dim),
                legendgroup=dim,
                y=jobs,
                x=xs,
                orientation="h",
                marker=dict(
                    color=colors,
                    opacity=1.0,
                    line=dict(width=0),
                ),
                customdata=custom,
                hovertemplate="%{y}<br>" + html_module.escape(dim) + "<br>%{customdata}<br>score %{x:.0f}<extra></extra>",
            )
        )
    # bargroupgap / bargap: with a tall enough figure (see write_overview_chart_html), stripes sit near 2px;
    # slightly higher bargroupgap keeps dimension stripes visually distinct without outlines.
    fig.update_layout(
        barmode="group",
        bargap=0.16,
        bargroupgap=0.10,
        xaxis=dict(
            title=None,
            range=[0.0, 100.0],
            showgrid=True,
            gridcolor="rgba(151,173,210,0.10)",
            zeroline=False,
            tickfont=dict(size=10, color=MUTED),
        ),
        yaxis=dict(
            title=None,
            autorange="reversed",
            tickfont=dict(size=10, color=MUTED),
            ticklabelposition="outside left",
            ticklabelstandoff=14,
            showgrid=True,
            gridcolor="rgba(151,173,210,0.08)",
            zeroline=False,
            automargin=True,
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.12,
            x=0,
            xanchor="left",
            font=dict(size=10, color=MUTED),
            traceorder="normal",
            itemclick="toggle",
            itemdoubleclick="toggleothers",
            valign="top",
        ),
        margin=dict(l=8, r=20, t=32, b=132),
    )
    return fig


def write_overview_chart_html(
    out_html: Path,
    rows: Sequence[CollatedRow],
    repo_root: Path,
    overview_md_rel: str,
) -> None:
    """Write a single HTML file with Plotly views (dot matrix, radar, grouped bars)."""
    if not rows:
        raise ValueError("rows is empty; nothing to chart")

    jobs, dims, z, z_text = _score_matrix(rows)

    label_by_key = {
        r.jd_key: (f"{MINI_FAMILY_GLYPH} {r.jd_key}" if _is_mini_family_model(r.model_used) else r.jd_key)
        for r in rows
    }
    display_jobs = [label_by_key.get(j, j) for j in jobs]

    studio_template = _studio_template()
    best_job = _best_overall_job(display_jobs, dims, z)
    worst_job = _lowest_overall_job(display_jobs, dims, z)
    per_row_weighted = [_weighted_row_score(dims, row) for row in z]
    avg_all = _mean_non_null(per_row_weighted) or 0.0
    mean_tier_label = _mean_numeric_to_nearest_tier_label(avg_all)

    n_dim = len(dims)
    figures: List[Tuple[str, go.Figure]] = [
        ("Dot matrix", _fig_heatmap(display_jobs, dims, z, z_text)),
        ("Radar", _fig_radar(display_jobs, dims, z)),
        ("Grouped bars", _fig_job_grouped_bars(display_jobs, dims, z, z_text)),
    ]

    sections: List[str] = []
    nav_links: List[str] = []
    for i, (title, fig) in enumerate(figures):
        fig.update_layout(template=studio_template, font=dict(size=12))
        heatmap_wide = title == "Dot matrix"
        if heatmap_wide:
            lm = _heatmap_left_margin_px(jobs)
            hw = _heatmap_figure_width_px(n_dim)
            # Top margin: room for x-axis (side=top) + tilted tick labels only; keep chart snug to the section title.
            fig.update_layout(
                width=hw,
                autosize=False,
                margin=dict(l=lm, r=28, t=100, b=64),
                xaxis=dict(
                    tickangle=HEATMAP_X_TICK_ANGLE,
                    tickfont=dict(size=HEATMAP_DIM_LABEL_FONT_PX, color=MUTED),
                    automargin=True,
                ),
                yaxis=dict(
                    automargin=False,
                    tickfont=dict(size=10, color=MUTED),
                    title=None,
                    autorange="reversed",
                ),
            )
        elif title == "Radar":
            # Wider canvas so the polar plot (domain x=[0.02, 0.62]) has room for
            # angular labels on the left/right and the legend column on the right.
            fig.update_layout(
                width=max(1000, min(4200, 72 * n_dim + 360)),
                height=max(560, min(900, 28 * n_dim + 240)),
                autosize=False,
            )
        elif title == "Grouped bars":
            lm = _heatmap_left_margin_px(jobs)
            row_px = _grouped_bar_row_height_px(n_dim)
            fig.update_layout(
                width=max(1080, min(2200, 900 + n_dim * 18)),
                height=max(420, min(9000, row_px * len(jobs) + 320)),
                autosize=False,
                margin=dict(l=lm, r=24, t=32, b=168),
            )
        responsive = not heatmap_wide
        chunk = fig.to_html(
            full_html=False,
            include_plotlyjs=False,
            config={"displayModeBar": True, "responsive": responsive, "displaylogo": False},
        )
        nav_links.append(f'<a href="#viz-{i}">{html_module.escape(title)}</a>')
        shell_class = "chart-shell chart-shell-scroll" if heatmap_wide else "chart-shell"
        sections.append(
            f'<section class="viz-card" id="viz-{i}">'
            f'  <div class="viz-head">'
            f'    <div class="viz-kicker">{i + 1:02d}</div>'
            f'    <div class="viz-copy">'
            f"      <h2>{html_module.escape(title)}</h2>"
            f"    </div>"
            f"  </div>"
            f'  <div class="{shell_class}">{chunk}</div>'
            f"</section>"
        )

    nav_tabs = "".join(nav_links)

    hero_fig, hero_min_w = _fig_hero_report_dates(rows, repo_root)
    hero_fig.update_layout(
        font=dict(
            color=TEXT,
            family="Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif",
            size=12,
        )
    )
    hero_chunk = hero_fig.to_html(
        full_html=False,
        include_plotlyjs="cdn",
        config={"displayModeBar": False, "responsive": True, "displaylogo": False},
    )

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Job evaluation comparison</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: {PAGE_BG};
      --panel: {PANEL_BG};
      --panel-alt: {PANEL_BG_ALT};
      --border: {BORDER};
      --text: {TEXT};
      --muted: {MUTED};
      --accent: {ACCENT};
      --accent-2: {ACCENT_2};
      --shadow: 0 24px 80px rgba(0, 0, 0, 0.38);
      /* Align hero summary copy and "On this page" with the same left inset. */
      --hero-inline-pad: 1.35rem;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      min-height: 100vh;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(119, 230, 255, 0.14), transparent 32%),
        radial-gradient(circle at top right, rgba(155, 124, 255, 0.16), transparent 28%),
        linear-gradient(180deg, #09101a 0%, var(--bg) 46%, #070b13 100%);
    }}
    .page {{
      width: min(1440px, calc(100vw - 40px));
      margin: 0 auto;
      padding: 36px 0 72px;
    }}
    .hero {{
      position: relative;
      overflow: hidden;
      padding: 36px;
      border: 1px solid var(--border);
      border-radius: 28px;
      background:
        linear-gradient(135deg, rgba(16, 24, 38, 0.96), rgba(10, 15, 26, 0.94)),
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0));
      box-shadow: var(--shadow);
    }}
    .hero::after {{
      content: "";
      position: absolute;
      inset: auto -10% -45% auto;
      width: 360px;
      height: 360px;
      background: radial-gradient(circle, rgba(119, 230, 255, 0.16), transparent 68%);
      pointer-events: none;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(1.75rem, 3.4vw, 3.5rem);
      line-height: 1.05;
      letter-spacing: -0.04em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
    }}
    .hero-timeline {{
      position: relative;
      z-index: 1;
      margin-top: 22px;
      max-width: 100%;
    }}
    .hero-timeline-scroll {{
      max-width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
    }}
    .hero-timeline-scroll .plotly-graph-div {{
      min-width: var(--tl-min, 100%);
    }}
    .hero-summary {{
      position: relative;
      z-index: 1;
      margin-top: 22px;
      padding: 1.1rem var(--hero-inline-pad);
      border-radius: 16px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(0, 0, 0, 0.22);
    }}
    .summary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem 1.75rem;
      align-items: start;
    }}
    .summary-item {{
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
      min-width: 0;
    }}
    .summary-k {{
      display: block;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
      font-weight: 600;
    }}
    .summary-v {{
      display: block;
      font-size: 1.12rem;
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: -0.02em;
      word-break: break-word;
    }}
    .summary-hint {{
      display: block;
      margin: 0;
      font-size: 0.72rem;
      font-weight: 500;
      line-height: 1.4;
      color: var(--muted);
    }}
    .submeta {{
      margin-top: 18px;
      color: var(--muted);
      font-size: 0.92rem;
    }}
    .submeta code {{
      color: var(--text);
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 999px;
      padding: 0.2rem 0.5rem;
    }}
    .quick-nav {{
      position: relative;
      z-index: 1;
      margin-top: 0.9rem;
      /* Same horizontal inset as .hero-summary so labels line up with .summary-k. */
      padding: 0 var(--hero-inline-pad);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      column-gap: 0.75rem;
      row-gap: 0.5rem;
    }}
    .quick-nav-eyebrow {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
      font-weight: 600;
      flex-shrink: 0;
      /* Optical vertical alignment with pill tab cap-height */
      line-height: 1;
      padding-top: 0.1rem;
    }}
    .quick-nav-tabs {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }}
    .quick-nav-tabs a {{
      color: var(--text);
      text-decoration: none;
      font-size: 0.9rem;
      line-height: 1.2;
      padding: 0.7rem 0.95rem;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
    }}
    .quick-nav-tabs a:hover {{
      transform: translateY(-1px);
      border-color: rgba(119, 230, 255, 0.34);
      background: rgba(119, 230, 255, 0.08);
    }}
    .dashboard {{
      margin-top: 22px;
      display: grid;
      gap: 22px;
    }}
    .viz-card {{
      padding: 24px;
      border-radius: 24px;
      border: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(16, 24, 38, 0.92), rgba(11, 18, 32, 0.94));
      box-shadow: var(--shadow);
    }}
    .viz-head {{
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 16px;
      align-items: center;
      margin-bottom: 2px;
    }}
    .viz-kicker {{
      min-width: 50px;
      height: 50px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 16px;
      background: linear-gradient(135deg, rgba(119, 230, 255, 0.14), rgba(155, 124, 255, 0.16));
      border: 1px solid rgba(255,255,255,0.07);
      color: var(--accent);
      font-weight: 800;
      letter-spacing: 0.08em;
    }}
    .viz-copy h2 {{
      margin: 0;
      font-size: 1.25rem;
      letter-spacing: -0.02em;
    }}
    .chart-shell {{
      padding: 0 8px 0;
      border-radius: 20px;
      background:
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
        var(--panel-alt);
      border: 1px solid rgba(255,255,255,0.05);
      overflow-x: auto;
      overflow-y: hidden;
    }}
    .chart-shell-scroll {{
      max-width: 100%;
    }}
    .plotly-graph-div {{ border-radius: 16px; }}
    .modebar {{
      background: rgba(7, 12, 22, 0.62) !important;
      border: 1px solid rgba(255,255,255,0.08) !important;
      border-radius: 12px !important;
      backdrop-filter: blur(12px);
    }}
    @media (max-width: 900px) {{
      .page {{ width: min(100vw - 24px, 1440px); padding-top: 20px; }}
      .hero {{ padding: 24px; border-radius: 22px; }}
      .viz-card {{ padding: 18px; border-radius: 20px; }}
      .viz-head {{ grid-template-columns: 1fr; }}
      .viz-kicker {{ width: 50px; }}
      .summary-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="hero">
      <h1>Job evaluation comparative views</h1>
      <div
        class="hero-timeline"
        style="--tl-min: {hero_min_w}px"
        role="region"
        aria-label="Count of eval reports by calendar day (date from report filename, otherwise file date)"
      >
        <div class="hero-timeline-scroll">{hero_chunk}</div>
      </div>
      <div class="hero-summary" role="region" aria-label="Batch summary">
        <div class="summary-grid">
          <div class="summary-item">
            <span class="summary-k">Jobs in scope</span>
            <span class="summary-v">{len(rows)}</span>
          </div>
          <div class="summary-item">
            <span class="summary-k">Verdict dimensions</span>
            <span class="summary-v">{len(dims)}</span>
          </div>
          <div class="summary-item" title="Ordinal tiers use an internal ~93–100 mapping for charting. Shown value is the tier nearest the batch mean—not a 0–100% grade.">
            <span class="summary-k">Mean verdict tier</span>
            <span class="summary-v">{html_module.escape(mean_tier_label)}</span>
            <span class="summary-hint">Nearest ordinal label, not a percentage.</span>
          </div>
          <div class="summary-item">
            <span class="summary-k">Top overall</span>
            <span class="summary-v">{html_module.escape(best_job)}</span>
          </div>
          <div class="summary-item">
            <span class="summary-k">Lowest overall</span>
            <span class="summary-v">{html_module.escape(worst_job)}</span>
          </div>
        </div>
      </div>
      <nav class="quick-nav" aria-label="On this page">
        <span class="quick-nav-eyebrow">On this page</span>
        <div class="quick-nav-tabs">{nav_tabs}</div>
      </nav>
    </header>
    <main class="dashboard">
      {"".join(sections)}
    </main>
  </div>
</body>
</html>
"""

    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(doc, encoding="utf-8")
