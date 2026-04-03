#!/usr/bin/env python3
"""
Scan summaries/*.md and build visualizations/summaries-timeline.html
(one horizontal card per month). Re-run after adding or editing summaries.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

SUMMARY_GLOB = "*.md"
SECTION_RE = re.compile(r"^### (.+)$", re.MULTILINE)

ESO_KEYWORDS = (
    "elder scrolls",
    "eso ",
    "eso:",
    "zenimax",
    "tamriel",
    "morrowind",
    "summerset",
    "elsweyr",
    "greymoor",
    "blackwood",
    "high isle",
    "necrom",
    "crown store",
    "crown pack",
    "dlc/",
    "gamepad",
    "playstation",
    "xbox",
    "champion screen",
    "console ui",
    "vivec",
    "khajiit",
    "nirn",
    "bethesda",
    "axure",
    "confluence",
    "jira",
    "webteam",
    "morrowind",
    "skyrim",
    "dovah",
    "quest tracker",
    "inventory menu",
    "trade ui",
    "mail screen",
    "armor dyeing",
)

PORT_KEYWORDS = (
    "wordpress",
    "portfolio site",
    "portfolio ",
    "typekit",
    " svn",
    "svn ",
    "jquery",
    "css3",
    "spritesheet",
    "htaccess",
    "carousel",
    "fout",
    "wp-framework",
    "parent theme",
)


def extract_section(md: str, heading: str) -> str | None:
    """Return body of ### {heading} through next ### or EOF."""
    pattern = rf"^### {re.escape(heading)}\s*\n(.*?)(?=^### |\Z)"
    m = re.search(pattern, md, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else None


def bullets_from_block(block: str) -> list[str]:
    out: list[str] = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("- "):
            out.append(line[2:].strip())
    return out


def goals_and_fallback(md: str) -> list[str]:
    for title in ("Goals", "Workstream", "Technical Accomplishments"):
        block = extract_section(md, title)
        if block:
            b = bullets_from_block(block)
            if b:
                return b
    return []


def infer_track(full_lower: str) -> tuple[str, str]:
    eso = sum(1 for k in ESO_KEYWORDS if k in full_lower)
    port = sum(1 for k in PORT_KEYWORDS if k in full_lower)
    if eso > port and eso >= 1:
        return "eso", "Elder Scrolls Online"
    if port > eso and port >= 1:
        return "portfolio", "Portfolio site"
    if eso and port and eso == port:
        return "neutral", "Mixed (portfolio + ESO / work)"
    return "neutral", "Journal / other"


def truncate_words(s: str, max_len: int) -> str:
    s = re.sub(r"\s+", " ", s.strip())
    if len(s) <= max_len:
        return s
    cut = s[: max_len + 1]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def month_tag(ym: str) -> tuple[str, int, int]:
    y, m = ym.split("-")
    names = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    return f"{names[int(m) - 1]} {y}", int(y), int(m)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def build_card(
    stem: str,
    headline: str,
    blurb: str,
    track: str,
    project_label: str,
    has_dump: bool,
    show_year: bool,
    year: int,
) -> str:
    month_label, _, _ = month_tag(stem)
    tag_class = track
    year_html = ""
    if show_year:
        year_html = f'            <p class="year-stamp">{esc(str(year))}</p>\n'

    links = [f'<a href="../summaries/{esc(stem)}.md">Summary</a>']
    if has_dump:
        links.append(
            f'<a class="dump" href="../monthly_dumps/{esc(stem)}.md">Raw month</a>'
        )
    links_html = "\n              ".join(links)

    return f"""        <div class="segment {esc(tag_class)}" role="listitem">
          <div class="node {esc(tag_class)}"></div>
          <article class="card">
{year_html}            <span class="tag {esc(tag_class)}">{esc(month_label)}</span>
            <p class="card-project">{esc(project_label)}</p>
            <h2>{esc(headline)}</h2>
            <p>{esc(blurb)}</p>
            <div class="card-links">
              {links_html}
            </div>
          </article>
        </div>"""


def main() -> None:
    root = Path(__file__).resolve().parent
    summaries_dir = root / "summaries"
    dumps_dir = root / "monthly_dumps"
    out_path = root / "visualizations" / "summaries-timeline.html"

    files = sorted(summaries_dir.glob(SUMMARY_GLOB), key=lambda p: p.stem)
    if not files:
        raise SystemExit(f"No summaries under {summaries_dir}")

    cards: list[str] = []
    prev_year: int | None = None

    for path in files:
        stem = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        full_lower = text.lower()
        track, project_label = infer_track(full_lower)

        bullets = goals_and_fallback(text)
        if bullets:
            headline = truncate_words(bullets[0], 88)
            blurb = truncate_words(" ".join(bullets[:3]), 320)
        else:
            headline = "Monthly summary"
            blurb = "No Goals / Workstream bullets parsed; open the summary file."

        _, y, _ = month_tag(stem)
        show_year = prev_year != y
        prev_year = y

        has_dump = (dumps_dir / f"{stem}.md").exists()
        cards.append(
            build_card(
                stem,
                headline,
                blurb,
                track,
                project_label,
                has_dump,
                show_year,
                y,
            )
        )

    n = len(cards)
    cards_html = "\n".join(cards)

    # Neutral track (not "gap" — that pattern reads as dataset hole)
    css_extra = """
    :root {
      --track-neutral: #7a7a8c;
      --track-neutral-dim: rgba(122, 122, 140, 0.22);
    }

    .dot.neutral {
      background: var(--track-neutral);
      box-shadow: 0 0 12px var(--track-neutral-dim);
    }

    .segment.neutral::before {
      background: linear-gradient(90deg, var(--track-neutral-dim), var(--track-neutral), var(--track-neutral-dim));
    }

    .node.neutral {
      background: var(--track-neutral);
    }

    .tag.neutral {
      background: var(--track-neutral-dim);
      color: #c8c8d8;
    }

    .year-stamp {
      font-family: "Fraunces", Georgia, serif;
      font-size: 1.65rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin: 0 0 0.5rem;
      color: var(--fg);
      opacity: 0.9;
    }

    .card {
      animation: rise 0.4s ease backwards;
    }

    @media (prefers-reduced-motion: reduce) {
      .card {
        animation: none;
      }
    }

    .card code {
      font-size: 0.88em;
      background: var(--line);
      padding: 0.08rem 0.28rem;
      border-radius: 3px;
      color: var(--fg);
    }
"""

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Journal summaries — timeline</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bg: #1a1814;
      --fg: #e8e4db;
      --muted: #9a958a;
      --track-portfolio: #c45c3e;
      --track-portfolio-dim: rgba(196, 92, 62, 0.22);
      --track-eso: #4a9b8e;
      --track-eso-dim: rgba(74, 155, 142, 0.2);
      --gap: #3d3a34;
      --line: #2e2b26;
      --card: #222019;
      --shadow: rgba(0, 0, 0, 0.45);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      min-height: 100vh;
      font-family: "Newsreader", Georgia, serif;
      font-size: 17px;
      line-height: 1.45;
      color: var(--fg);
      background:
        radial-gradient(ellipse 120% 80% at 20% -10%, rgba(196, 92, 62, 0.12), transparent 50%),
        radial-gradient(ellipse 100% 60% at 90% 100%, rgba(74, 155, 142, 0.1), transparent 45%),
        var(--bg);
    }}

    .wrap {{
      max-width: none;
      margin: 0;
      padding: 2.5rem clamp(1rem, 4vw, 2.5rem) 4rem;
    }}

    header h1 {{
      font-family: "Fraunces", Georgia, serif;
      font-weight: 700;
      font-size: clamp(1.75rem, 4vw, 2.35rem);
      letter-spacing: -0.02em;
      margin: 0 0 0.35rem;
    }}

    header p {{ margin: 0; color: var(--muted); font-size: 1.05rem; }}

    .legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      margin: 2rem 0 1.5rem;
      font-size: 0.92rem;
    }}

    .legend span {{ display: inline-flex; align-items: center; gap: 0.45rem; }}

    .dot {{
      width: 11px;
      height: 11px;
      border-radius: 50%;
    }}

    .dot.portfolio {{
      background: var(--track-portfolio);
      box-shadow: 0 0 12px var(--track-portfolio-dim);
    }}

    .dot.eso {{
      background: var(--track-eso);
      box-shadow: 0 0 12px var(--track-eso-dim);
    }}

    .timeline-scroll {{
      overflow-x: auto;
      overflow-y: visible;
      padding: 0.75rem 0 1.35rem;
      -webkit-overflow-scrolling: touch;
      overscroll-behavior-x: contain;
      scroll-snap-type: x proximity;
      scrollbar-gutter: stable;
    }}

    .timeline-hint {{
      margin: 0 0 0.35rem;
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 0.8rem;
      letter-spacing: 0.02em;
      color: var(--muted);
    }}

    .timeline-hint kbd {{
      font: inherit;
      font-size: 0.88em;
      padding: 0.08rem 0.35rem;
      border-radius: 3px;
      border: 1px solid var(--line);
      background: var(--card);
      color: var(--fg);
    }}

    .timeline {{
      display: flex;
      align-items: stretch;
      gap: 0;
      width: max-content;
      padding: 0;
    }}

    .segment {{
      flex: 0 0 clamp(272px, 78vw, 352px);
      scroll-snap-align: start;
      position: relative;
      padding-top: 2.75rem;
    }}

    .segment::before {{
      content: "";
      position: absolute;
      top: 1rem;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--line);
      border-radius: 2px;
    }}

    .segment:first-child::before {{ border-radius: 2px 0 0 2px; }}
    .segment:last-child::before {{ border-radius: 0 2px 2px 0; }}

    .segment.portfolio::before {{
      background: linear-gradient(90deg, var(--track-portfolio-dim), var(--track-portfolio), var(--track-portfolio-dim));
    }}

    .segment.eso::before {{
      background: linear-gradient(90deg, var(--track-eso-dim), var(--track-eso), var(--track-eso-dim));
    }}

    .node {{
      position: absolute;
      top: 0.55rem;
      left: 50%;
      transform: translateX(-50%);
      width: 14px;
      height: 14px;
      border-radius: 50%;
      border: 2px solid var(--bg);
      z-index: 1;
    }}

    .node.portfolio {{ background: var(--track-portfolio); }}
    .node.eso {{ background: var(--track-eso); }}

    .card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 1.45rem 1.25rem 1.35rem;
      margin: 0 0.6rem 0.75rem;
      box-shadow: 0 4px 20px var(--shadow);
    }}

    @keyframes rise {{
      from {{ opacity: 0; transform: translateY(8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .card h2 {{
      font-family: "Fraunces", Georgia, serif;
      font-size: 1.14rem;
      font-weight: 700;
      margin: 0 0 0.65rem;
      letter-spacing: -0.01em;
      line-height: 1.25;
    }}

    .tag {{
      display: inline-block;
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      padding: 0.28rem 0.5rem;
      border-radius: 3px;
      margin-bottom: 0.75rem;
      font-family: system-ui, sans-serif;
    }}

    .tag.portfolio {{
      background: var(--track-portfolio-dim);
      color: #f0a090;
    }}

    .tag.eso {{
      background: var(--track-eso-dim);
      color: #8fd4c9;
    }}

    .card-project {{
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.03em;
      margin: 0 0 1rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid var(--line);
      color: var(--muted);
      line-height: 1.45;
    }}

    .card > p:not(.card-project):not(.year-stamp) {{
      margin: 0;
      font-size: 0.94rem;
      line-height: 1.58;
      color: var(--muted);
    }}

    .card > p:not(.card-project):not(.year-stamp) strong {{
      color: var(--fg);
      font-weight: 600;
    }}

    footer {{
      margin-top: 2.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--line);
      font-size: 0.88rem;
      color: var(--muted);
    }}

    footer code {{
      font-size: 0.82em;
      background: var(--line);
      padding: 0.12rem 0.35rem;
      border-radius: 4px;
      color: var(--fg);
    }}

    .browser-hint {{
      margin-top: 1.25rem;
      padding: 1rem 1.1rem;
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 10px;
      font-size: 0.9rem;
      color: var(--muted);
    }}

    .browser-hint strong {{ color: var(--fg); }}

    .browser-hint code {{
      font-size: 0.84em;
      background: var(--line);
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      color: var(--fg);
    }}

    .card-links {{
      margin-top: 1.1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--line);
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem 1.25rem;
    }}

    .card-links a {{
      font-family: system-ui, -apple-system, sans-serif;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #c9a87a;
      text-decoration: none;
      border-bottom: 1px solid rgba(201, 168, 122, 0.35);
    }}

    .card-links a:hover {{
      color: #e4d4b8;
      border-bottom-color: #e4d4b8;
    }}

    .card-links a.dump {{
      color: #7eb8ae;
      border-bottom-color: rgba(126, 184, 174, 0.35);
    }}

    .card-links a.dump:hover {{
      color: #a8ddd4;
      border-bottom-color: #a8ddd4;
    }}
{css_extra}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>Journal summaries</h1>
      <p>{n} months ({files[0].stem} — {files[-1].stem}). Timeline is wide on purpose—scroll horizontally. Track colors are heuristic (keywords in the full summary); override labels in the source markdown if you add front matter later.</p>
      <div class="browser-hint">
        <strong>Regenerate:</strong>
        <code>cd journal_summarizer &amp;&amp; python3 build_summaries_timeline.py</code>
        (or pass the script path from your project root)
        <br /><strong>Open:</strong> this file in a browser, or serve the folder with
        <code>python3 -m http.server 8765</code> under <code>visualizations/</code>.
      </div>
    </header>

    <div class="legend">
      <span><span class="dot portfolio"></span> Portfolio site (keyword match)</span>
      <span><span class="dot eso"></span> Elder Scrolls Online (keyword match)</span>
      <span><span class="dot neutral"></span> Journal / other or mixed</span>
    </div>

    <p class="timeline-hint" id="timeline-hint">Scroll the timeline: trackpad swipe, touch drag, <kbd>Shift</kbd> + mouse wheel, or the scrollbar below.</p>

    <div class="timeline-scroll" role="region" aria-labelledby="timeline-hint" tabindex="0">
      <div class="timeline" role="list">
{cards_html}
      </div>
    </div>

    <footer>
      Generated <code>summaries-timeline.html</code> — {n} cards from <code>summaries/*.md</code>
    </footer>
  </div>
</body>
</html>
"""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {out_path} ({n} months)")


if __name__ == "__main__":
    main()
