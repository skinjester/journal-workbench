# Manual peer edges (mutual–mutual)

**Optional, extra:** The graph **already** infers *co-capture* links (same comma-separated line under an anchor) from [network-map.md](network-map.md) — you do not type those by hand. Use *this* file when you need an edge the capture lines will never represent (e.g. they know each other but you never co-listed them, or a relationship across anchors you want to highlight with a **gold** line and note).

Add **undirected** links between people who are **anchors** or **mutuals** in the main map, or add people only here (they become nodes without an anchor `##` until you add one).

**Regenerate:** `python3 scripts/build_network_graph.py`

## Table

| Person A | Person B | Note (optional) |
|----------|----------|-----------------|
| Chris Balser | Jeremy Sera | Template — replace with links you know, or delete this row |
|  |  |  |

*Match names to the map; different spelling = a different node.*

## Bullets (alternative)

One pair per line (leading `-` or `*`), comma between names, optional `;` then a note (shown on edge hover). Example: `- Chris Balser, Jeremy Sera; same studio` as its own line — not inside a fenced code block.
