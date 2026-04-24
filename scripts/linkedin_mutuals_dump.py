#!/usr/bin/env python3
"""
Dump visible text from LinkedIn mutual people-search pages for each anchor in
`contacts/network-map-anchors.json`.

**Personal / compliance:** LinkedIn’s Terms of Service may restrict automated
access. Use for your own account, private notes, and at your own risk. Do not
commit the saved session or dumps if they are sensitive.

Install (once, from repo root; use the same `python3` for pip + script + this line):
  python3 -m venv .venv && source .venv/bin/activate  # optional
  python3 -m pip install -r scripts/requirements-linkedin-dump.txt
  python3 -m playwright install chromium
  # Do not run bare `playwright install` (CLI may not be on PATH). If "Executable
  # doesn't exist", run: python3 -m playwright install chromium

Run (visible browser; first time you sign in, then key Enter):
  python3 scripts/linkedin_mutuals_dump.py

Options:
  --out DIR          default: contacts/linkedin-mutual-dumps
  --state FILE       default: .playwright/linkedin-state.json
  --dry-run          print URLs, do not open browser
  --only NAME        substring of anchor name (e.g. "Derek")
  --max-page N       cap page index per anchor (overrides file’s mutual_pages)
  --delay SEC        pause between page loads (default 1.2)
  --re-login         ignore saved state and re-login before dumping
  --headless         use after a successful login save (faster, no window)

Session: On first run (or --re-login), a Chromium window opens. Sign in to
LinkedIn, return to the terminal, press Enter. Session is written to
`--state` so the next run can reuse it (e.g. with --headless).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any

# Repo root: scripts/ -> parent
REPO = Path(__file__).resolve().parent.parent
DEFAULT_ANCHORS = REPO / "contacts" / "network-map-anchors.json"
DEFAULT_OUT = REPO / "contacts" / "linkedin-mutual-dumps"
DEFAULT_STATE = REPO / ".playwright" / "linkedin-state.json"
BASE = "https://www.linkedin.com/search/results/people/"

SYNC_PLAYWRIGHT_ERROR = "Install: pip install -r scripts/requirements-linkedin-dump.txt"


def _slug(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s)
    return re.sub(r"-{2,}", "-", s).strip("-") or "anchor"


def build_mutual_url(connection_id: str, page: int = 1) -> str:
    net = urllib.parse.quote('["F"]', safe="")
    cval = f'["{connection_id}"]'
    cenc = urllib.parse.quote(cval, safe="")
    u = f"{BASE}?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network={net}&connectionOf={cenc}"
    if page and page > 1:
        u += f"&page={page}"
    return u


def _load_anchors(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _visible_text_for_page(page) -> str:
    """Best-effort visible text from main feed area."""
    for sel in (
        "main[role='main']",
        "div[role='main']",
        "div.scaffold-layout__main",  # class names shift; this may miss
        "main",
    ):
        loc = page.locator(sel)
        try:
            if loc.count() == 0:
                continue
            t = loc.first.inner_text(timeout=15_000)
            if t and t.strip():
                return t
        except Exception:
            continue
    return page.inner_text("body", timeout=15_000)


def _ensure_state(state: Path, headless: bool, re_login: bool) -> Path:
    state.parent.mkdir(parents=True, exist_ok=True)
    if re_login and state.exists():
        state.unlink()
    if state.exists() and not re_login:
        return state

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as e:  # pragma: no cover
        print(SYNC_PLAYWRIGHT_ERROR, file=sys.stderr)
        raise SystemExit(1) from e

    print("Opening Chromium. Sign in to LinkedIn, then return here and press Enter…")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            locale="en-US",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()
        page.goto("https://www.linkedin.com/", wait_until="domcontentloaded")
        try:
            input("Press Enter after you are logged in and the feed (or home) has loaded. ")
        except EOFError:
            print("No TTY; cannot wait for Enter. Re-run in a terminal.", file=sys.stderr)
            browser.close()
            raise SystemExit(1)
        context.storage_state(path=str(state))
        browser.close()
    print(f"Saved session: {state}")
    return state


def main() -> int:
    ap = argparse.ArgumentParser(description="LinkedIn mutual search text dump (Playwright).")
    ap.add_argument(
        "--anchors",
        type=Path,
        default=DEFAULT_ANCHORS,
        help="network-map-anchors.json path",
    )
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output directory for .txt")
    ap.add_argument("--state", type=Path, default=DEFAULT_STATE, help="Playwright storage state file")
    ap.add_argument("--dry-run", action="store_true", help="print URLs only")
    ap.add_argument(
        "--only",
        type=str,
        default="",
        help="filter anchors whose name contains this substring (case-insensitive)",
    )
    ap.add_argument(
        "--max-page",
        type=int,
        default=0,
        help="max page number per anchor (0 = use mutual_pages from json)",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=1.2,
        help="seconds between navigations",
    )
    ap.add_argument(
        "--re-login",
        action="store_true",
        help="discard saved state and go through sign-in again",
    )
    ap.add_argument(
        "--headless",
        action="store_true",
        help="run without window (use after a successful --state is saved)",
    )
    ap.add_argument(
        "--wait-network",
        type=str,
        default="load",
        choices=["commit", "domcontentloaded", "load", "networkidle"],
        help="page.goto wait_until",
    )
    args = ap.parse_args()
    if not args.anchors.is_file():
        print(f"Anchors file not found: {args.anchors}", file=sys.stderr)
        return 1
    data = _load_anchors(args.anchors)
    anchors: dict[str, Any] = data.get("anchors") or {}
    if not isinstance(anchors, dict) or not anchors:
        print("No anchors in JSON.", file=sys.stderr)
        return 1

    only = args.only.strip().lower()
    to_run: list[tuple[str, str, int]] = []
    for name, rec in sorted(anchors.items(), key=lambda x: x[0].lower()):
        if only and only not in name.lower():
            continue
        if not isinstance(rec, dict) or "connectionOf" not in rec:
            continue
        conn = str(rec["connectionOf"])
        if args.max_page and args.max_page > 0:
            mp = args.max_page
        else:
            mp = int(rec.get("mutual_pages") or 1)
        to_run.append((name, conn, max(1, min(mp, 50))))

    if not to_run:
        print("No anchors to process after filter.", file=sys.stderr)
        return 1

    if args.dry_run:
        for name, connection_id, pages in to_run:
            for p in range(1, pages + 1):
                u = build_mutual_url(connection_id, page=p)
                print(f"{_slug(name)}-p{p}\n  {u}")
        return 0

    if args.headless and (args.re_login or not args.state.is_file()):
        print(
            "Refusing --headless on first run or with --re-login. "
            "Log in without --headless, then re-run with --headless if you like.",
            file=sys.stderr,
        )
        return 1

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as e:
        print(SYNC_PLAYWRIGHT_ERROR, file=sys.stderr)
        raise SystemExit(1) from e

    state_path = _ensure_state(
        args.state, headless=args.headless, re_login=args.re_login
    )
    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".last-run.txt").write_text(
        f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n", encoding="utf-8"
    )

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=args.headless,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            storage_state=str(state_path),
            locale="en-US",
        )
        page = context.new_page()
        for name, connection_id, pages in to_run:
            for pg in range(1, pages + 1):
                url = build_mutual_url(connection_id, page=pg)
                rel = f"{_slug(name)}-p{pg}.txt"
                fpath = out_dir / rel
                print(f"-> {fpath.name} ({url})")
                try:
                    page.goto(
                        url,
                        wait_until=args.wait_network,
                        timeout=90_000,
                    )
                except Exception as e:
                    err = f"[goto error: {e}]\n"
                    fpath.write_text(
                        f"# {name} page {pg}\n# URL: {url}\n{err}\n", encoding="utf-8"
                    )
                    if args.delay:
                        time.sleep(args.delay)
                    continue
                # Small settle for client-render
                time.sleep(0.8)
                try:
                    text = _visible_text_for_page(page)
                except Exception as e:
                    text = f"(visible text failed: {e})"
                header = (
                    f"# {name} — page {pg}\n"
                    f"# {url}\n"
                    f"# generated by scripts/linkedin_mutuals_dump.py\n"
                    f"\n"
                )
                fpath.write_text(header + (text or ""), encoding="utf-8")
                if args.delay:
                    time.sleep(args.delay)
        browser.close()

    print(f"Done. Wrote under {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
