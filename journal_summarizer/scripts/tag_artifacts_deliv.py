#!/usr/bin/env python3
"""
Insert `deliv:*` after project tags on Artifacts Delivered bullets.
Run: python3 journal_summarizer/scripts/tag_artifacts_deliv.py
"""
from __future__ import annotations

import re
from pathlib import Path

SUMMARIES = Path(__file__).resolve().parent.parent / "summaries"
BULLET_RE = re.compile(r"^(- \*\*\[([^\]]+)\]\*\*) (.*)$")

# First matching rule wins (order matters).
RULES: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(
            r"invoice|payment verification|tax voucher|accountant|dns\b|/\s*mx\b|"
            r"backup|b2\b|synology|hyperbackup|cloudsync|goodsync|rack\b|cable map|patchbay|"
            r"domain/registry|registry checklist|keyboard build|switch/stab|speed test|gateway setting|"
            r"migration checklist|drive map|flywheel ticket|elastic ip|gpu pool|render orchestration|"
            r"storage topology|wall-wart|din-rail|zone 2|ansible|parts list|assembly milestones|"
            r"interface driver notes|fiber\b"
        ),
        "operations",
    ),
    (
        re.compile(
            r"questionpro|\bsurvey instrument\b|survey \+|comp site analysis|"
            r"search pattern|search examples|screen-capture library.*search|search review|"
            r"age-gate best-practice|bam storefront audit|storefront audit|"
            r"collating search examples"
        ),
        "audit",
    ),
    (
        re.compile(
            r"axure/html|axshare|axure html|\bhtml5/s3\b|html/css demo|opt-in test|optinmonster|"
            r"kuula workaround demo|interactive prototype|browser build matrix|"
            r"prototype build links|html5 deployment|s3 publish checklist|kestrel.*in-browser|"
            r"php artisan|clickable/authorable|multi-camera unreal|unreal.*scene|unreal diorama|"
            r"html5 kestrel|local server started|runnable.*artifact|staging urls for preorder"
        ),
        "prototype",
    ),
    (
        re.compile(
            r"powerpoint|keynote|\bdeck for|exec deck|stakeholder deck|show-and-tell|"
            r"bridge deck|slide/deck|deck package|presentation marked|\bdeck,|\bdecks "
        ),
        "presentation",
    ),
    (
        re.compile(
            r"styleguide|style guide|ui kit|component taxonomy|form layout guide|"
            r"tooltip.*v\d|figma library v|team libraries|item tooltip styleguide"
        ),
        "design-system",
    ),
    (
        re.compile(
            r"wireframe|high-fidelity comp|\bcomps\b|photoshop|png/state|state export|\bgif\b|"
            r"after effects|\bae sequences\b|animatic|render queue|tiled render|1080p output|"
            r"compositor|frame sequence|movie render|marketing still|spritesheet|sprite\b|"
            r"responsive comp set|export bundle|flythrough|niagara study|master comp|hdr ingest|"
            r"dark feed spec|application framework screens|wire exports|inspector components|"
            r"sitemap pages.*figma|figma sitemap|visual design|promo creative brief|"
            r"crown pack hero|cover image|bkg template|fullscreen bkg"
        ),
        "visuals",
    ),
    (
        re.compile(
            r"confluence|jira|functional spec|experience map|mind map|\bsitemap\b|flow matrix|"
            r"bam email.*notes|handoff message|about draft|panel bio|notion design|data model|"
            r"notification matrix|clustering strateg|temporal nav|ar spreadsheet|"
            r"prototype install doc|getting the prototype|install doc|documentation drops|"
            r"handoff cleanup|story grouping|revision notes|bug reports|written menu|"
            r"timeline spec|workaround doc|legal form|account creation form|age-gate research|"
            r"invoice packet|retro confluence|audit summary updates|status doc expansions|"
            r"contentful entry|mesa outline|charter notes|strategy memo|quest lifecycle|"
            r"tabbed spec|sprint backlog export|decision log|documentation outline|"
            r"handoff message archive|equipment skin documentation|mod menu spec|bio/rates|"
            r"value-prop|jira board config|curation list|brand fork|bug thread summary|"
            r"cta variants|contact block|payment verification notes|workshop doc|runbook|"
            r"invite list|shot list|validated html|functions\.php|quality-control backlog|"
            r"email template design notes|written ux response|mind map \+|pdf/slides|"
            r"medium piece outline|festival program edits|render queue logs|sanitized"
        ),
        "documentation",
    ),
]


def classify(rest: str) -> str:
    if "deliv:" in rest:
        return ""
    tl = rest.lower()
    for pat, d in RULES:
        if pat.search(tl):
            return d
    if "localhost" in tl and ("production" in tl or "theme" in tl or "portfolio" in tl):
        return "prototype"
    if "localhost" in tl and "flywheel" in tl:
        return "prototype"
    if "milanote" in tl:
        return "documentation"
    if "unreal" in tl:
        return "prototype"
    if "pdf" in tl and "proposal" in tl:
        return "presentation"
    return "documentation"


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    if "### Artifacts Delivered" not in text:
        return 0
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_section = False
    changed = 0
    for line in lines:
        if line.startswith("### ") and in_section and not line.startswith("### Artifacts"):
            in_section = False
        if line.startswith("### Artifacts Delivered"):
            in_section = True
            out.append(line)
            continue
        if in_section:
            raw = line.rstrip("\n\r")
            eol = line[len(raw) :]
            m = BULLET_RE.match(raw)
            if m and "`deliv:" not in line:
                prefix, rest = m.group(1), m.group(3)
                d = classify(rest)
                if d:
                    out.append(f"{prefix} `deliv:{d}` {rest}{eol}")
                    changed += 1
                    continue
            out.append(line)
        else:
            out.append(line)
    if changed:
        path.write_text("".join(out), encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    for path in sorted(SUMMARIES.glob("*.md")):
        n = process_file(path)
        if n:
            print(f"{path.name}: {n}")
            total += n
    print(f"Total bullets tagged: {total}")


if __name__ == "__main__":
    main()
