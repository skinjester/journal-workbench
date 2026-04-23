#!/usr/bin/env python3
"""Build a graph dataset from contacts/network-map.md.

Outputs:
  contacts/network-graph.data.json   Canonical data (nodes, edges, meta). Each
                                     node has superWeight = sum of incident edge
                                     weights (used for superconnector sizing).
  contacts/network-graph.data.js     Same data assigned to window.NETWORK_DATA
                                     so network-graph.html works over file://.
  contacts/riot-2nd-shared-1st-connections.md  2nd targets × shared 1st (from
                                     card) + in-map match (if riot json merged).

Re-run whenever contacts/network-map.md, contacts/network-map-anchors.json,
contacts/riot-2nd-degree-ux-2026.json, or the R&D profile flags table
in contacts/riot-games.md changes:

    python3 scripts/build_network_graph.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP_MD = ROOT / "contacts" / "network-map.md"
ANCHORS_JSON = ROOT / "contacts" / "network-map-anchors.json"
RIOT_MD = ROOT / "contacts" / "riot-games.md"
TAGS_JSON = ROOT / "contacts" / "network-map.tags.json"
OUT_JSON = ROOT / "contacts" / "network-graph.data.json"
OUT_JS = ROOT / "contacts" / "network-graph.data.js"
RIOT_2ND_JSON = ROOT / "contacts" / "riot-2nd-degree-ux-2026.json"
RIOT_2ND_1ST_MD = ROOT / "contacts" / "riot-2nd-shared-1st-connections.md"

# Anchor-level `##` sections that are not people.
SKIP_ANCHOR_HEADINGS = {
    "How to re-open the full list in a browser",
    "Hubs (repeat names across many anchors' page-1 samples)",
    "Hubs (repeat names across many anchors\u2019 page-1 samples)",
    "Remaining anchors (same workflow)",
}


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def clean_anchor_heading(heading: str) -> str:
    """Strip trailing disambiguation like ' (Riot)' or ' (Game Caviar)'."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", heading).strip()


def clean_person_token(raw: str) -> str | None:
    """Return a canonical display name for one comma-separated token, or None if skipped."""
    t = raw.strip()
    if not t:
        return None
    # Drop trailing parenthetical annotations — including ones that happen to
    # contain bold names (e.g. "(many rows show **Steven Chiang** ...)").
    t = re.sub(r"\s*\([^)]*\)\s*", " ", t).strip()
    # Strip markdown emphasis and inline code fences.
    t = t.replace("**", "").replace("*", "").replace("`", "")
    # Collapse whitespace.
    t = re.sub(r"\s+", " ", t).strip()
    # Skip obvious non-name tokens: URLs, residual meta like "and others; walk"
    if not t:
        return None
    if t.lower().startswith(("http://", "https://")):
        return None
    # A name should look like at least two word-ish chunks (first + last).
    if " " not in t:
        return None
    # Guard against leftover prose fragments from dropped parentheticals.
    lowered = t.lower()
    if lowered.startswith(("and others", "e.g.", "many rows", "as ")):
        return None
    return t


def parse_bridge_names(bridge: str) -> list[str]:
    """Names from a LinkedIn card 'mutuals with you and X' / bridge list (CSV-ish)."""
    if not bridge or not bridge.strip():
        return []
    t = bridge.strip()
    if t in ("—", "-", "—", "\u2014"):
        return []
    s = re.sub(r"\s+and\s+(\d+\s+)?other", "", bridge, flags=re.IGNORECASE)
    s = s.replace(" and ", ", ")
    out: list[str] = []
    for raw in s.split(","):
        tok = raw.strip()
        if not tok or tok in ("—", "-", "\u2014"):
            continue
        if re.match(r"^\+\d+\s*other", tok, re.I) or re.fullmatch(r"\+\d+", tok):
            continue
        if re.search(r"other\s+mutual", tok, re.I):
            continue
        if "3rd+" in tok or tok.lower().startswith("message "):
            continue
        if tok.lower().startswith("(card:"):
            continue
        tok = re.sub(r"\s*\+\d+\s*$", "", tok).strip()
        name = clean_person_token(tok)
        if name:
            out.append(name)
    return out


def second_degree_id(name: str) -> str:
    return f"2nd:{slugify(name)}"


def merge_second_degree_riot(
    base: dict, riot_path: Path
) -> tuple[list[dict], list[dict], int] | None:
    """2nd-degree outreach nodes + bridge edges to names that exist in the base graph."""
    if not riot_path.exists():
        return None
    data = json.loads(riot_path.read_text(encoding="utf-8"))
    people: list[dict] = data.get("people", [])
    # Only 1st-layer ids (anchors + mutuals) — not You, not other 2nd.
    resolvable: set[str] = {
        n["id"] for n in base["nodes"] if not n.get("isYou") and not n.get("isSecond")
    }
    id_name: dict[str, str] = {
        n["id"]: n["name"]
        for n in base["nodes"]
        if not n.get("isYou") and not n.get("isSecond")
    }
    # Captured 1st-degree anchors in network-map (people with a ## section + mutuals).
    anchor_id_set: set[str] = {n["id"] for n in base["nodes"] if n.get("isAnchor")}
    bridge_edges: list[dict] = []
    second_nodes: list[dict] = []
    second_ids: set[str] = set()
    n_skipped_3p = 0
    for p in people:
        if p.get("networkDistance") != "2nd":
            if p.get("networkDistance") in ("3rd+", "3rd"):
                n_skipped_3p += 1
            continue
        name = (p.get("name") or "").strip()
        if not name:
            continue
        sid = second_degree_id(name)
        if sid in resolvable or sid in second_ids:
            continue
        second_ids.add(sid)
        raw_line = (p.get("bridgeMutuals") or "").strip()
        bridges = parse_bridge_names(p.get("bridgeMutuals", "") or "")
        targets: set[str] = set()
        in_map: list[dict] = []
        for b in bridges:
            bid = slugify(b)
            if bid in resolvable and bid != sid:
                targets.add(bid)
                in_map.append(
                    {
                        "id": bid,
                        "name": id_name.get(bid, b),
                        "inMapAsAnchor": bid in anchor_id_set,
                    }
                )
        in_map.sort(key=lambda x: x["name"].lower())
        in_ids = {d["id"] for d in in_map}
        not_in_map = [b for b in bridges if slugify(b) not in in_ids]
        for bid in sorted(targets):
            bridge_edges.append(
                {"source": sid, "target": bid, "type": "bridge", "weight": 1}
            )
        title_raw = (p.get("title") or "").replace("\\", "").strip()
        second_nodes.append(
            {
                "id": sid,
                "name": name,
                "isAnchor": False,
                "isSecond": True,
                "isYou": False,
                "isRD": False,
                "mutualDegree": 0,
                "bridgeCount": len(targets),
                "mutualPages": None,
                "connectionOf": None,
                "searchHint": None,
                "headline": title_raw or None,
                "profileUrl": p.get("profileUrl"),
                "company": None,
                "role": "design",
                "tier": None,
                "cardMutuals": raw_line or None,
                "firstConnParsed": bridges,
                "firstConnInMap": in_map,
                "firstConnNotInMap": not_in_map,
            }
        )
    if not second_nodes:
        return None
    return second_nodes, bridge_edges, n_skipped_3p


def write_riot_2nd_shared_1st_md(
    out_path: Path, second_nodes: list[dict], source_rel: str
) -> None:
    """Scannable: which LinkedIn 1st connections overlap each 2nd target; map match status."""
    lines: list[str] = [
        "# 2nd-degree (Riot/UX) — your shared 1st connections",
        "",
        f"*Generated from `{source_rel}` and your network map. The **card line** is what LinkedIn showed (names you both know as your 1st; often truncated with +N). **Parsed names** are what we could extract. **In this map** = same person appears as a node in the graph (1st-captured = has a `##` anchor in network-map, or only as a listed mutual). Names only on LinkedIn but not in the map still matter for outreach — find them in LinkedIn.*",
        "",
    ]
    for n in sorted(second_nodes, key=lambda x: x["name"].lower()):
        name = n["name"]
        lines.append(f"## {name}")
        if n.get("headline"):
            lines.append(f"* {n['headline']}")
        card = n.get("cardMutuals")
        if card:
            lines.append(f"- **On LinkedIn card (shared 1st):** {card}")
        parsed = n.get("firstConnParsed") or []
        if parsed:
            lines.append(
                f"- **Parsed 1st names** ({len(parsed)}): "
                + ", ".join(parsed)
            )
        in_map = n.get("firstConnInMap") or []
        if in_map:
            lines.append(
                f"- **In this map** ({len(in_map)}): "
            )
            for d in in_map:
                role = "1st anchor (captured in network-map)" if d.get("inMapAsAnchor") else "in map as mutual, not a captured 1st anchor"
                lines.append(f"  - **{d['name']}** — {role}")
        else:
            lines.append("- **In this map:** *(none of the parsed names match a node yet)*")
        nm = n.get("firstConnNotInMap") or []
        if nm:
            lines.append(
                f"- **Parsed but not in this map** ({len(nm)}): {', '.join(nm)}"
            )
        if n.get("profileUrl"):
            lines.append(f"- [Profile]({n['profileUrl']})")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def parse_network_map(md_text: str) -> dict[str, list[str]]:
    """Return anchor_display_name -> [mutual display name, ...] (order preserved, dedup'd per anchor)."""
    lines = md_text.splitlines()
    anchors: dict[str, list[str]] = {}

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if not m:
            i += 1
            continue

        raw_heading = m.group(1).strip()
        if raw_heading in SKIP_ANCHOR_HEADINGS:
            i += 1
            continue

        anchor_name = clean_anchor_heading(raw_heading)
        j = i + 1
        mutual_block_start: int | None = None

        # Find the next "### Mutuals" block before the next "##" or EOF.
        while j < n and not lines[j].startswith("## "):
            if lines[j].startswith("### Mutuals"):
                mutual_block_start = j + 1
                break
            j += 1

        mutuals: list[str] = []
        seen: set[str] = set()
        if mutual_block_start is not None:
            k = mutual_block_start
            while k < n:
                cur = lines[k]
                if cur.startswith("## ") or cur.strip() == "---":
                    break
                if cur.startswith("### "):
                    break
                stripped = cur.strip()
                if stripped.startswith("- "):
                    body = stripped[2:].strip()
                    # Skip italic meta rows like "*(Card lines also reference…)*".
                    if body.startswith("*"):
                        k += 1
                        continue
                    for token in body.split(","):
                        name = clean_person_token(token)
                        if name and name not in seen:
                            seen.add(name)
                            mutuals.append(name)
                k += 1

        anchors[anchor_name] = mutuals
        # Jump to the next "##" to continue scanning.
        i = j
    return anchors


def parse_rd_flags(riot_md_text: str) -> set[str]:
    """Names in the 'R&D profile flags (LinkedIn)' table in riot-games.md."""
    lines = riot_md_text.splitlines()
    in_section = False
    flagged: set[str] = set()
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip().startswith("## R&D profile flags")
            continue
        if not in_section:
            continue
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        first = cells[0]
        # Skip header and separator rows.
        if not first or first.lower() == "name" or set(first) <= {"-", " "}:
            continue
        flagged.add(first.replace("**", "").strip())
    return flagged


def build_graph(
    anchors_md: dict[str, list[str]],
    anchors_json: dict,
    rd_flags: set[str],
    tags_overlay: dict,
) -> dict:
    tags = (tags_overlay or {}).get("tags", {}) or {}
    roles_map = (tags_overlay or {}).get("roles", {}) or {}
    tiers_map = (tags_overlay or {}).get("tiers", {}) or {}
    default_tier_opacity = (tags_overlay or {}).get("defaultTierOpacity", 0.35)
    # Normalize names to ids; preserve display names.
    display_by_id: dict[str, str] = {}
    anchor_ids: set[str] = set()

    for anchor_name in anchors_md:
        aid = slugify(anchor_name)
        anchor_ids.add(aid)
        display_by_id.setdefault(aid, anchor_name)

    # Anchor metadata (connectionOf, mutual_pages) keyed by display name in JSON.
    anchor_meta_by_id: dict[str, dict] = {}
    for key, meta in anchors_json.get("anchors", {}).items():
        aid = slugify(key)
        anchor_meta_by_id[aid] = {
            "connectionOf": meta.get("connectionOf"),
            "mutualPages": meta.get("mutual_pages"),
            "searchHint": meta.get("search_hint"),
        }

    anchor_lists_by_id: list[tuple[str, list[str]]] = []
    for anchor_name, mutuals in anchors_md.items():
        aid = slugify(anchor_name)
        mid_list: list[str] = []
        for m in mutuals:
            mid = slugify(m)
            display_by_id.setdefault(mid, m)
            mid_list.append(mid)
        anchor_lists_by_id.append((aid, mid_list))

    # Anchor -> mutual edges (weight 1 per membership).
    list_edges: list[dict] = []
    for aid, mids in anchor_lists_by_id:
        for mid in mids:
            if mid == aid:
                continue
            list_edges.append(
                {"source": aid, "target": mid, "type": "lists", "weight": 1}
            )

    # Degree (# anchors listing this person), as a mutual.
    mutual_degree: dict[str, int] = defaultdict(int)
    for _, mids in anchor_lists_by_id:
        for mid in set(mids):
            mutual_degree[mid] += 1

    # Assemble nodes.
    nodes: list[dict] = []
    for nid, display in sorted(display_by_id.items(), key=lambda kv: kv[1].lower()):
        is_anchor = nid in anchor_ids
        meta = anchor_meta_by_id.get(nid, {})
        tag = tags.get(display, {}) or {}
        nodes.append(
            {
                "id": nid,
                "name": display,
                "isAnchor": is_anchor,
                "isSecond": False,
                "isYou": False,
                "isRD": display in rd_flags,
                "mutualDegree": mutual_degree.get(nid, 0),
                "mutualPages": meta.get("mutualPages"),
                "connectionOf": meta.get("connectionOf"),
                "searchHint": meta.get("searchHint"),
                "company": tag.get("company"),
                "role": tag.get("role"),
                "tier": tag.get("tier"),
            }
        )

    you_id = "__you__"
    you_node: dict = {
        "id": you_id,
        "name": "You",
        "isAnchor": False,
        "isSecond": False,
        "isYou": True,
        "isRD": False,
        "mutualDegree": 0,
        "mutualPages": None,
        "connectionOf": None,
        "searchHint": None,
        "company": None,
        "role": None,
        "tier": None,
    }
    nodes.insert(0, you_node)

    you_to_anchor_edges: list[dict] = [
        {
            "source": you_id,
            "target": aid,
            "type": "you-anchor",
            "weight": 1.0,
        }
        for aid in sorted(anchor_ids)
    ]
    # No "coanchor" / peer–peer co-list edges: we only model anchor → mutual (and you → anchor,
    # 2nd → bridge). Co-appearing on the same comma-separated line is not an edge.
    edges = you_to_anchor_edges + list_edges

    return {
        "meta": {
            "generatedAt": date.today().isoformat(),
            "sourceMd": str(MAP_MD.relative_to(ROOT)),
            "anchorsJson": str(ANCHORS_JSON.relative_to(ROOT)),
            "tagsJson": str(TAGS_JSON.relative_to(ROOT)) if TAGS_JSON.exists() else None,
            "anchorCount": len(anchor_ids),
            "secondDegreeCount": 0,
            "nodeCount": len(nodes),
            "edgeCount": len(edges),
            "disclaimer": (
                "1st-layer data reflects LinkedIn mutual samples in contacts/network-map.md. "
                "The graph uses anchor → mutual (and you → anchor) only; it does not draw "
                "edges between mutuals who merely appear on the same list line. "
                "Node size = superWeight (sum of incident edge weights). 2nd-degree Riot/UX "
                "rows use contacts/riot-2nd-degree-ux-2026.json (bridge edges to matched 1st)."
            ),
        },
        "roles": roles_map,
        "tiers": tiers_map,
        "defaultTierOpacity": default_tier_opacity,
        "nodes": nodes,
        "edges": edges,
    }


def apply_superconnector_weights(graph: dict) -> None:
    """Set each node's superWeight = sum of incident edge weights (full graph)."""
    strength: dict[str, float] = defaultdict(float)
    for e in graph["edges"]:
        w = float(e.get("weight", 1))
        a, b = e["source"], e["target"]
        strength[a] += w
        strength[b] += w
    for n in graph["nodes"]:
        n["superWeight"] = float(strength.get(n["id"], 0.0))


def main() -> int:
    if not MAP_MD.exists():
        print(f"missing {MAP_MD}", file=sys.stderr)
        return 1
    if not ANCHORS_JSON.exists():
        print(f"missing {ANCHORS_JSON}", file=sys.stderr)
        return 1

    anchors_md = parse_network_map(MAP_MD.read_text(encoding="utf-8"))
    anchors_json = json.loads(ANCHORS_JSON.read_text(encoding="utf-8"))
    rd_flags = (
        parse_rd_flags(RIOT_MD.read_text(encoding="utf-8")) if RIOT_MD.exists() else set()
    )
    tags_overlay = (
        json.loads(TAGS_JSON.read_text(encoding="utf-8")) if TAGS_JSON.exists() else {}
    )

    graph = build_graph(anchors_md, anchors_json, rd_flags, tags_overlay)

    s2 = merge_second_degree_riot(graph, RIOT_2ND_JSON)
    if s2:
        second_nodes, bridge_edges, _n3 = s2
        graph["nodes"].extend(second_nodes)
        graph["edges"].extend(bridge_edges)
        m = graph["meta"]
        m["secondDegreeCount"] = len(second_nodes)
        m["secondBridgeEdgeCount"] = len(bridge_edges)
        m["riot2ndSource"] = str(RIOT_2ND_JSON.relative_to(ROOT))
        m["nodeCount"] = len(graph["nodes"])
        m["edgeCount"] = len(graph["edges"])
        write_riot_2nd_shared_1st_md(
            RIOT_2ND_1ST_MD,
            second_nodes,
            str(RIOT_2ND_JSON.relative_to(ROOT)),
        )

    apply_superconnector_weights(graph)
    graph["meta"]["nodeCount"] = len(graph["nodes"])
    graph["meta"]["edgeCount"] = len(graph["edges"])

    OUT_JSON.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    OUT_JS.write_text(
        "window.NETWORK_DATA = "
        + json.dumps(graph, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )

    meta = graph["meta"]
    s2c = meta.get("secondDegreeCount", 0)
    out_bits = f"{OUT_JSON.relative_to(ROOT)} and {OUT_JS.relative_to(ROOT)}"
    if s2c:
        out_bits += f" and {RIOT_2ND_1ST_MD.relative_to(ROOT)}"
    print(
        f"wrote {out_bits} — {meta['anchorCount']} anchors, {s2c} 2nd-degree, "
        f"{meta['nodeCount']} nodes, {meta['edgeCount']} edges"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
