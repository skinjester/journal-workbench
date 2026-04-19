#!/usr/bin/env python3
"""
Write a standalone Plotly HTML dashboard comparing job evaluation verdict tiers.

Expects to be imported from `collate_job_evaluations` with the same `sys.path` (scripts directory).
"""

from __future__ import annotations

import html as html_module
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from collate_job_evaluations import (
    VERDICT_TABLE_COLUMNS,
    CollatedRow,
    tier_cell_to_chart_numeric,
    verdict_line_to_table_cell,
)


PAGE_BG = "#0a0f1a"
PANEL_BG = "#101826"
PANEL_BG_ALT = "#0d1422"
BORDER = "rgba(151, 173, 210, 0.16)"
TEXT = "#ecf3ff"
MUTED = "#94a8c6"
ACCENT = "#77e6ff"
ACCENT_2 = "#9b7cff"
SERIES = ["#77e6ff", "#9b7cff", "#55d6be", "#ff8a65", "#ffd166", "#ff6fae", "#64b5f6", "#c3f73a"]

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


def _wrap_dim_label(label: str, max_first_line: int = 10) -> str:
    """Split a dimension label at a natural word boundary for 2-line heatmap column headers."""
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
    dims = list(VERDICT_TABLE_COLUMNS)
    z: List[List[Optional[float]]] = []
    z_text: List[List[str]] = []
    for r in rows:
        row_vals: List[Optional[float]] = []
        row_txt: List[str] = []
        for d in dims:
            cell = verdict_line_to_table_cell(r.verdicts.get(d, ""), d)
            row_txt.append(cell if cell.strip() else "—")
            row_vals.append(tier_cell_to_chart_numeric(cell))
        z.append(row_vals)
        z_text.append(row_txt)
    return jobs, dims, z, z_text


def _mean_non_null(values: Sequence[Optional[float]]) -> Optional[float]:
    xs = [v for v in values if v is not None]
    return (sum(xs) / len(xs)) if xs else None


# Anchors for mapping batch numeric mean → readable tier label (chart-wide 0–100 encoding).
_MEAN_TIER_ANCHOR_LABELS: Tuple[str, ...] = (
    "Very High",
    "High",
    "Medium–High",
    "Medium",
    "Low",
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
    z: List[List[Optional[float]]],
    z_text: Optional[List[List[str]]],
) -> Tuple[List[str], List[List[Optional[float]]], Optional[List[List[str]]]]:
    """Descending mean tier score; alphabetical job key for stable ties."""
    order = sorted(
        range(len(jobs)),
        key=lambda i: (-(_mean_non_null(z[i]) or float("-inf")), jobs[i].lower()),
    )
    jobs2 = [jobs[i] for i in order]
    z2 = [list(z[i]) for i in order]
    zt2 = [list(z_text[i]) for i in order] if z_text else None
    return jobs2, z2, zt2


def _tier_score_x_range(z: Sequence[Sequence[Optional[float]]]) -> Tuple[float, float]:
    """Pad min/max chart scores (0–100) so dots are not crushed into one vertical strip."""
    flat = [v for row in z for v in row if v is not None]
    if not flat:
        return 0.0, 100.0
    lo, hi = min(flat), max(flat)
    span = hi - lo
    pad = max(2.0, span * 0.35) if span > 1e-9 else 4.0
    return max(0.0, lo - pad), min(100.0, hi + pad)


# Imputed chart score for missing cells in radar (aligned with unknown-tier chart encoding).
_RADAR_MISSING_SCORE = 28.0


def _radar_radial_range(z: Sequence[Sequence[Optional[float]]]) -> Tuple[float, float]:
    """
    Tight radial bounds around this cohort so polygons are not stacked in a thin ring.
    Uses the same missing-value fill as the traces.
    """
    vals: List[float] = []
    for row in z:
        for v in row:
            vals.append(float(v) if v is not None else _RADAR_MISSING_SCORE)
    if not vals:
        return -2.0, 102.0
    lo, hi = min(vals), max(vals)
    span = hi - lo
    if span < 1e-9:
        pad = 4.0
        return max(0.0, lo - pad), min(100.0, hi + pad)
    pad = max(1.0, span * 0.08)
    return max(0.0, lo - pad), min(100.0, hi + pad)


def _best_overall_job(
    jobs: Sequence[str],
    z: Sequence[Sequence[Optional[float]]],
) -> str:
    """Job with the highest mean tier score across dimensions."""
    best_job = jobs[0]
    best_avg = -1.0
    for i, job in enumerate(jobs):
        avg = _mean_non_null(z[i])
        if avg is not None and avg > best_avg:
            best_avg = avg
            best_job = job
    return best_job


def _lowest_overall_job(
    jobs: Sequence[str],
    z: Sequence[Sequence[Optional[float]]],
) -> str:
    """Job with the lowest mean tier score across dimensions."""
    worst_job = jobs[0]
    worst_avg = float("inf")
    for i, job in enumerate(jobs):
        avg = _mean_non_null(z[i])
        if avg is not None and avg < worst_avg:
            worst_avg = avg
            worst_job = job
    return worst_job


DOT_MARKER_MIN_PX = 10.0
DOT_MARKER_MAX_PX = 34.0
# Chart encoding for missing / unparsed cells (matches unknown-tier spread in tier_cell_to_chart_numeric).
_HEATMAP_MISSING_SCORE = 28.0


def _fig_heatmap(jobs: List[str], dims: List[str], z: List[List[Optional[float]]], z_text: List[List[str]]) -> go.Figure:
    """
    Dot matrix: each cell is a circle whose size AND color both encode the chart tier score (0–100).

    Size uses a **fixed** 0–100 scale (not cohort min/max) so identical ordinals get identical dots;
    color uses the same score on a 0–100 colorscale.
    """
    COLOR_LO, COLOR_HI = 0.0, 100.0

    wrapped_dims = [_wrap_dim_label(d) for d in dims]

    xs: List[str] = []
    ys: List[str] = []
    sizes: List[float] = []
    colors: List[float] = []
    hovers: List[str] = []

    for i, job in enumerate(jobs):
        for j, dim in enumerate(dims):
            v = z[i][j]
            score = float(v) if v is not None else _HEATMAP_MISSING_SCORE
            norm = max(0.0, min(1.0, score / 100.0))
            sz = DOT_MARKER_MIN_PX + norm * (DOT_MARKER_MAX_PX - DOT_MARKER_MIN_PX)
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
                colorbar=dict(
                    orientation="h",
                    x=0.5,
                    xanchor="center",
                    y=-0.08,
                    yanchor="top",
                    len=0.6,
                    thickness=10,
                    title=dict(
                        text="Chart score (ordinal → 0–100)",
                        side="top",
                        font=dict(color=MUTED, size=10),
                    ),
                    tickfont=dict(color=MUTED, size=9),
                    tickvals=[0, 20, 40, 60, 80, 100],
                ),
                line=dict(width=0),
            ),
            hovertemplate=hovers,
            showlegend=False,
        )
    )

    fig.update_layout(
        height=max(380, 36 * len(jobs) + 160),
        xaxis=dict(
            side="top",
            tickangle=0,
            tickmode="array",
            tickvals=dims,
            ticktext=wrapped_dims,
            tickfont=dict(size=11),
            showgrid=True,
            gridcolor="rgba(151,173,210,0.10)",
            zeroline=False,
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


def _column_percentile_ranks(z: List[List[Optional[float]]]) -> List[List[Optional[float]]]:
    """
    Per column, average-rank percentile in [0, 1] for non-missing scores (ties get mean rank).
    Missing cells stay None.
    """
    if not z or not z[0]:
        return []
    n_rows = len(z)
    n_cols = len(z[0])
    out: List[List[Optional[float]]] = [[None] * n_cols for _ in range(n_rows)]
    for j in range(n_cols):
        pairs: List[Tuple[float, int]] = []
        for i in range(n_rows):
            v = z[i][j]
            if v is not None:
                pairs.append((float(v), i))
        m = len(pairs)
        if m == 0:
            continue
        if m == 1:
            out[pairs[0][1]][j] = 0.5
            continue
        pairs.sort(key=lambda x: x[0])
        a = 0
        while a < m:
            b = a + 1
            while b < m and pairs[b][0] == pairs[a][0]:
                b += 1
            avg_r = (a + b - 1) / 2.0
            denom = max(1.0, float(m - 1))
            for t in range(a, b):
                row_i = pairs[t][1]
                out[row_i][j] = avg_r / denom
            a = b
    return out


def _fig_heatmap_batch_rank(
    jobs: List[str],
    dims: List[str],
    z: List[List[Optional[float]]],
    z_text: List[List[str]],
    pct: List[List[Optional[float]]],
) -> go.Figure:
    """
    Dot matrix: marker **size** encodes within-batch rank per column; **color** still encodes chart score.
    """
    COLOR_LO, COLOR_HI = 0.0, 100.0
    wrapped_dims = [_wrap_dim_label(d) for d in dims]

    xs: List[str] = []
    ys: List[str] = []
    sizes: List[float] = []
    colors: List[float] = []
    hovers: List[str] = []

    for i, job in enumerate(jobs):
        for j, dim in enumerate(dims):
            v = z[i][j]
            score = float(v) if v is not None else _HEATMAP_MISSING_SCORE
            pr = pct[i][j]
            norm = float(pr) if pr is not None else 0.0
            sz = DOT_MARKER_MIN_PX + norm * (DOT_MARKER_MAX_PX - DOT_MARKER_MIN_PX)
            tier_label = (z_text[i][j] if z_text and i < len(z_text) and j < len(z_text[i]) else "—") or "—"
            rank_note = f"{100.0 * norm:.0f}th pct" if pr is not None else "—"
            xs.append(dim)
            ys.append(job)
            sizes.append(sz)
            colors.append(score)
            hovers.append(
                f"{job}<br>{dim}<br>{tier_label}<br>Batch rank (column): {rank_note}<extra></extra>"
            )

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
                colorbar=dict(
                    orientation="h",
                    x=0.5,
                    xanchor="center",
                    y=-0.08,
                    yanchor="top",
                    len=0.6,
                    thickness=10,
                    title=dict(
                        text="Chart score (color); size = batch rank",
                        side="top",
                        font=dict(color=MUTED, size=10),
                    ),
                    tickfont=dict(color=MUTED, size=9),
                    tickvals=[0, 20, 40, 60, 80, 100],
                ),
                line=dict(width=0),
            ),
            hovertemplate=hovers,
            showlegend=False,
        )
    )

    fig.update_layout(
        height=max(380, 36 * len(jobs) + 160),
        xaxis=dict(
            side="top",
            tickangle=0,
            tickmode="array",
            tickvals=dims,
            ticktext=wrapped_dims,
            tickfont=dict(size=11),
            showgrid=True,
            gridcolor="rgba(151,173,210,0.10)",
            zeroline=False,
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
    r0, r1 = _radar_radial_range(z)
    span = r1 - r0
    if span <= 8.0:
        dtick = 2.0
    elif span <= 20.0:
        dtick = 5.0
    else:
        dtick = 10.0
    fig = go.Figure()
    theta = list(dims) + [dims[0]]
    for i, job in enumerate(jobs):
        rvals = [z[i][j] if z[i][j] is not None else _RADAR_MISSING_SCORE for j in range(len(dims))]
        r_closed = rvals + [rvals[0]]
        color = SERIES[i % len(SERIES)]
        fig.add_trace(
            go.Scatterpolar(
                r=r_closed,
                theta=theta,
                mode="lines",
                name=job[:48] + ("…" if len(job) > 48 else ""),
                line=dict(color=color, width=2),
                fill="toself",
                fillcolor=_with_alpha(color, 0.08),
                opacity=0.72,
                hovertemplate="%{fullData.name}<br>%{theta}: %{r:.0f}<extra></extra>",
            )
        )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[r0, r1],
                dtick=dtick,
                tickformat=".1f",
            )
        ),
        height=560,
        legend=dict(tracegroupgap=0, font=dict(size=9)),
    )
    return fig


def _fig_dot_plots(
    jobs: List[str],
    dims: List[str],
    z: List[List[Optional[float]]],
    z_text: Optional[List[List[str]]] = None,
) -> go.Figure:
    jobs, z, z_text = _sort_jobs_for_dot_plots(jobs, z, z_text)
    n_dims = len(dims)
    x0, x1 = _tier_score_x_range(z)
    wrapped_titles = [_wrap_dim_label(d) for d in dims]
    fig = make_subplots(
        rows=1,
        cols=n_dims,
        subplot_titles=wrapped_titles,
        horizontal_spacing=0.04,
        shared_yaxes=True,
    )
    for j in range(n_dims):
        xs = [z[i][j] if z[i][j] is not None else float("nan") for i in range(len(jobs))]
        colors = [
            float(v) if v is not None else _HEATMAP_MISSING_SCORE
            for v in [z[i][j] for i in range(len(jobs))]]
        cd: Optional[List[str]] = None
        ht = "%{y}<br>%{x:.0f}<extra></extra>"
        if z_text:
            cd = [z_text[i][j] if j < len(z_text[i]) else "" for i in range(len(jobs))]
            ht = "%{y}<br>%{customdata}<br>score %{x:.0f}<extra></extra>"
        fig.add_trace(
            go.Scatter(
                x=xs,
                y=jobs,
                mode="markers",
                marker=dict(
                    size=11,
                    color=colors,
                    colorscale=HEATMAP_MONO_COLORSCALE,
                    cmin=0.0,
                    cmax=100.0,
                    showscale=False,
                    line=dict(width=1, color="rgba(255,255,255,0.10)"),
                ),
                customdata=cd,
                hovertemplate=ht,
                showlegend=False,
            ),
            row=1,
            col=j + 1,
        )
        fig.update_xaxes(
            title_text="",
            range=[x0, x1],
            showticklabels=False,
            showgrid=True,
            row=1,
            col=j + 1,
        )
    fig.update_yaxes(row=1, col=1, automargin=True, tickfont=dict(size=10, color=MUTED))
    for c in range(2, n_dims + 1):
        fig.update_yaxes(showticklabels=False, row=1, col=c)
    # Match subplot title font to the dot-matrix column header style.
    fig.update_annotations(font=dict(size=11, color=TEXT))
    fig.update_layout(
        height=max(480, 22 * len(jobs) + 80),
        margin=dict(l=220, r=20, t=68, b=40),
    )
    return fig


def write_overview_chart_html(
    out_html: Path,
    rows: Sequence[CollatedRow],
    repo_root: Path,
    overview_md_rel: str,
) -> None:
    """Write a single HTML file with Plotly views (dot matrix, optional batch rank, radar, dot plots)."""
    if not rows:
        raise ValueError("rows is empty; nothing to chart")

    jobs, dims, z, z_text = _score_matrix(rows)
    studio_template = _studio_template()
    best_job = _best_overall_job(jobs, z)
    worst_job = _lowest_overall_job(jobs, z)
    avg_all = _mean_non_null([_mean_non_null(row) for row in z]) or 0.0
    mean_tier_label = _mean_numeric_to_nearest_tier_label(avg_all)
    pct = _column_percentile_ranks(z)

    n_dim = len(dims)
    figures: List[Tuple[str, str, go.Figure]] = [
        (
            "Dot matrix",
            "Each cell is a circle: size and color encode the ordinal tier mapped to a 0–100 chart score (wide spread). Hover for the verdict label.",
            _fig_heatmap(jobs, dims, z, z_text),
        ),
        (
            "Dot matrix (batch rank)",
            "Same chart scores for color; marker size encodes within-batch rank in each column (0 = weakest in this overview, 1 = strongest). Not an absolute grade—useful when many cells share the same ordinal.",
            _fig_heatmap_batch_rank(jobs, dims, z, z_text, pct),
        ),
        (
            "Radar",
            "Shape of each job across dimensions. Radial axis is zoomed to this run’s min/max chart scores; toggle traces in the legend when overlap is still dense. Missing dimensions use the same placeholder as unknown-tier (28).",
            _fig_radar(jobs, dims, z),
        ),
        (
            "Dot plots",
            f"{n_dim} small multiples for quick within-dimension comparison. Rows sort by mean chart score.",
            _fig_dot_plots(jobs, dims, z, z_text),
        ),
    ]

    sections: List[str] = []
    nav_links: List[str] = []
    for i, (title, blurb, fig) in enumerate(figures):
        fig.update_layout(template=studio_template, font=dict(size=12))
        if title == "Dot matrix" or title.startswith("Dot matrix ("):
            lm = _heatmap_left_margin_px(jobs)
            fig.update_layout(
                margin=dict(l=lm, r=28, t=64, b=64),
                yaxis=dict(
                    automargin=False,
                    tickfont=dict(size=10, color=MUTED),
                    title=None,
                    autorange="reversed",
                ),
            )
        chunk = fig.to_html(
            full_html=False,
            include_plotlyjs="cdn" if i == 0 else False,
            config={"displayModeBar": True, "responsive": True, "displaylogo": False},
        )
        nav_links.append(f'<a href="#viz-{i}">{html_module.escape(title)}</a>')
        sections.append(
            f'<section class="viz-card" id="viz-{i}">'
            f'  <div class="viz-head">'
            f'    <div class="viz-kicker">{i + 1:02d}</div>'
            f'    <div class="viz-copy">'
            f"      <h2>{html_module.escape(title)}</h2>"
            f'      <p class="blurb">{html_module.escape(blurb)}</p>'
            f"    </div>"
            f"  </div>"
            f'  <div class="chart-shell">{chunk}</div>'
            f"</section>"
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
    .lede {{
      max-width: 64ch;
      margin: 16px 0 0;
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.65;
    }}
    .hero-meta {{
      margin-top: 24px;
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
    }}
    .hero-meta .metric-pair {{
      flex: 1 1 100%;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .hero-meta .metric-pair .metric {{
      min-width: 0;
    }}
    .metric {{
      min-width: 170px;
      padding: 16px 18px;
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 18px;
      background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
      backdrop-filter: blur(14px);
    }}
    .metric .label {{
      display: block;
      color: var(--muted);
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }}
    .metric strong {{
      display: block;
      font-size: 1.3rem;
      line-height: 1.1;
      letter-spacing: -0.03em;
    }}
    .metric small.metric-hint {{
      display: block;
      margin-top: 6px;
      font-size: 0.72rem;
      font-weight: 500;
      line-height: 1.35;
      color: var(--muted);
      letter-spacing: 0.01em;
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
      margin-top: 22px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .quick-nav a {{
      color: var(--text);
      text-decoration: none;
      padding: 0.7rem 0.95rem;
      border-radius: 999px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
    }}
    .quick-nav a:hover {{
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
      align-items: start;
      margin-bottom: 8px;
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
      margin: 2px 0 6px;
      font-size: 1.25rem;
      letter-spacing: -0.02em;
    }}
    .blurb {{
      margin: 0;
      max-width: 72ch;
      color: var(--muted);
      line-height: 1.65;
      font-size: 0.97rem;
    }}
    .chart-shell {{
      padding: 2px 8px 0;
      border-radius: 20px;
      background:
        linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)),
        var(--panel-alt);
      border: 1px solid rgba(255,255,255,0.05);
      overflow-x: auto;
      overflow-y: hidden;
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
      .hero-meta .metric-pair {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="hero">
      <h1>Job evaluation comparative views</h1>
      <p class="lede">A polished dark-mode review board for comparing role fit across the current evaluation set.</p>
      <div class="hero-meta">
        <div class="metric"><span class="label">Jobs in scope</span><strong>{len(rows)}</strong></div>
        <div class="metric"><span class="label">Verdict dimensions</span><strong>{len(dims)}</strong></div>
        <div class="metric" title="Ordinal tiers use an internal ~93–100 mapping for charting. Shown value is the tier nearest the batch mean—not a 0–100% grade.">
          <span class="label">Mean verdict tier</span>
          <strong>{html_module.escape(mean_tier_label)}</strong>
          <small class="metric-hint">Nearest ordinal label · not a percentage score</small>
        </div>
        <div class="metric-pair">
          <div class="metric"><span class="label">Top overall</span><strong>{html_module.escape(best_job)}</strong></div>
          <div class="metric"><span class="label">Lowest overall</span><strong>{html_module.escape(worst_job)}</strong></div>
        </div>
      </div>
      <nav class="quick-nav">{"".join(nav_links)}</nav>
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
