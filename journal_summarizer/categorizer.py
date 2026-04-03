"""Rule-based journal categorization and tagged monthly summaries (no external APIs)."""

import re
from typing import List, Dict, Optional
from dataclasses import dataclass, field

from parsers import JournalEntry


@dataclass
class CategorizedEntry:
    """Entry with assigned categories."""
    entry: JournalEntry
    categories: List[str]
    summary: Optional[str] = None
    people: List[str] = field(default_factory=list)


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

SYNTHESIS_SECTION_ORDER = [
    "Goals",
    "Workstream",
    "Artifacts Delivered",
    "Key Decisions",
    "Open Questions / Follow Ups",
]


def infer_tag_from_project(project: str, content: str) -> str:
    """Map dump `project` header + entry text to a single controlled vocabulary tag."""
    p = (project or "").strip().lower()
    c = (content or "").lower()

    if p in ("his portfolio", "profile", "skinjester.com work", "garyboodhooworld"):
        return "Portfolio"
    if p == "spirit animal":
        if any(
            k in c
            for k in (
                "image garden",
                "imagegarden",
                "workshop",
                "codame",
                "handout",
                "participant",
                "inseec",
                "github hq",
                "neural style",
                "torch",
                "instance limit",
            )
        ):
            return "Image Garden"
        return "deepdreamvisionquest"
    if p in ("futureworld", "cinechamber"):
        return "xoholo"
    if p == "eso":
        if any(
            k in c
            for k in (
                "kestrel",
                "sketchbox",
                "quest tracker",
                "inventory nav",
                "gaze",
                "worldspace",
                "hud overlay",
                "level sequencer",
                "equipment dashboard",
                "quest log",
                "2.5d projection",
            )
        ):
            return "KESTREL"
        if any(
            k in c
            for k in (
                "studio site",
                "recruiting",
                "careers page",
                "career list",
                "career post",
                "employee profile",
                "department profile",
                "about us location",
            )
        ):
            return "ESO-Studio Site"
        if any(
            k in c
            for k in (
                "contentful",
                "elderscrollsonline",
                "marketing",
                "web team",
                "cms",
                "chapter page",
                "buy now",
                "promo",
                "zos-platform",
                "website",
                "squarespace",
            )
        ):
            return "ESO-Platform"
        if "crown" in c or "crown store" in c:
            if any(k in c for k in ("web", "marketing", "cms", "elderscrollsonline", "browser")):
                return "ESO-Platform"
            return "ESO"
        return "ESO"

    direct = {
        "ops": "OPS",
        "project ansible": "Project Ansible",
        "skinjestercorp": "skinjestercorp",
        "deepdreamvisionquest": "deepdreamvisionquest",
        "image garden": "Image Garden",
        "xoholo": "xoholo",
        "iveda": "iveda",
        "rpvr": "RPVR",
    }
    return direct.get(p, "OPS")


def _tag_bullet_line(tag: str, sentence: str) -> str:
    s = (sentence or "").strip()
    s = re.sub(r"^\-\s*", "", s)
    s = re.sub(r"^\*\*\[[^\]]+\]\*\*\s*", "", s)
    return f"- **[{tag}]** {s}"


@dataclass
class SynthesizedReport:
    """Monthly report: tagged bullets + optional closing narrative."""
    year_month: str
    total_entries: int
    projects: List[str]
    sections: Dict[str, List[str]]
    people: List[str]
    closing_narrative: str = ""


class JournalCategorizor:
    """Categorizes entries and builds summaries using local heuristics only."""

    def __init__(self, config: Dict):
        self.config = config
        self.template_sections = config.get("template_sections", [])
        self.batch_size = config.get("processing", {}).get("batch_size", 20)

    def categorize_entries(self, entries: List[JournalEntry]) -> List[CategorizedEntry]:
        categorized: List[CategorizedEntry] = []
        for i in range(0, len(entries), self.batch_size):
            batch = entries[i : i + self.batch_size]
            print(f"Categorizing batch {i // self.batch_size + 1} ({len(batch)} entries)...")
            categorized.extend(self._rule_based_categorization(batch))
        return categorized

    def synthesize_monthly_report(
        self, entries: List[JournalEntry], year_month: str
    ) -> SynthesizedReport:
        projects = sorted(set(entry.project for entry in entries))
        return self._rule_based_synthesis(entries, year_month, projects)

    def _rule_based_categorization(self, entries: List[JournalEntry]) -> List[CategorizedEntry]:
        categorized = []
        for entry in entries:
            content_lower = entry.content.lower()
            categories: List[str] = []
            people: List[str] = []

            name_patterns = [
                r"\b(?:spoke with|talked to|met with|from|asked|told)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)",
                r"\b([A-Z][a-z]+)\s+(?:suggested|mentioned|said|asked)",
            ]
            for pattern in name_patterns:
                for match in re.finditer(pattern, entry.content):
                    people.append(match.group(1))

            if any(
                word in content_lower
                for word in [
                    "goal",
                    "plan",
                    "objective",
                    "target",
                    "want to",
                    "need to",
                    "will",
                ]
            ):
                categories.append("Goals")

            if any(
                word in content_lower
                for word in [
                    "implementing",
                    "working on",
                    "building",
                    "developing",
                    "coding",
                    "writing",
                    "fixing",
                    "debugging",
                ]
            ):
                categories.append("Workstream")

            if any(
                word in content_lower
                for word in [
                    "completed",
                    "finished",
                    "delivered",
                    "released",
                    "deployed",
                    "shipped",
                    "done",
                    "✅",
                ]
            ):
                categories.append("Artifacts Delivered")

            if any(
                word in content_lower
                for word in ["test", "qa", "bug", "fix", "issue", "crash", "error"]
            ):
                categories.append("Coverage")

            if any(
                word in content_lower
                for word in ["decided", "decision", "chose", "architecture", "approach", "strategy"]
            ):
                categories.append("Key Decisions")

            if any(
                word in content_lower
                for word in ["spoke", "talked", "met", "meeting", "discussed", "feedback"]
            ):
                categories.append("Collaboration and Inputs")

            if any(
                word in content_lower
                for word in ["question", "?", "unclear", "unknown", "need to figure", "blocker", "waiting"]
            ):
                categories.append("Open Questions / Follow Ups")

            if not categories:
                categories = ["Workstream"]

            categorized.append(
                CategorizedEntry(
                    entry=entry,
                    categories=categories,
                    summary=None,
                    people=list(set(people)),
                )
            )

        return categorized

    def _rule_based_synthesis(
        self,
        entries: List[JournalEntry],
        year_month: str,
        projects: List[str],
    ) -> SynthesizedReport:
        categorized: List[CategorizedEntry] = []
        for i in range(0, len(entries), self.batch_size):
            batch = entries[i : i + self.batch_size]
            categorized.extend(self._rule_based_categorization(batch))

        canon_map = {
            "Goals": "Goals",
            "Workstream": "Workstream",
            "Artifacts Delivered": "Artifacts Delivered",
            "Coverage": "Workstream",
            "Key Decisions": "Key Decisions",
            "Collaboration and Inputs": "Workstream",
            "Open Questions / Follow Ups": "Open Questions / Follow Ups",
        }
        sections: Dict[str, List[str]] = {s: [] for s in SYNTHESIS_SECTION_ORDER}
        all_people: set = set()
        seen: Dict[str, set] = {s: set() for s in SYNTHESIS_SECTION_ORDER}

        for cat_entry in categorized:
            all_people.update(cat_entry.people)
            text = self._clean_entry_text(cat_entry.entry.content)
            if len(text) < 12:
                continue
            tag = infer_tag_from_project(cat_entry.entry.project, cat_entry.entry.content)
            line = _tag_bullet_line(tag, text)
            for cat in cat_entry.categories or ["Workstream"]:
                dest = canon_map.get(cat)
                if dest not in sections or len(sections[dest]) >= 10:
                    continue
                key = line[:220]
                if key in seen[dest]:
                    continue
                seen[dest].add(key)
                sections[dest].append(line)

        if entries and not any(sections[s] for s in SYNTHESIS_SECTION_ORDER):
            e = entries[0]
            t = infer_tag_from_project(e.project, e.content)
            sections["Workstream"] = [_tag_bullet_line(t, self._clean_entry_text(e.content))]

        narrative = (
            f"{len(entries)} entries across {len(set(projects))} source labels — "
            "rule-based draft. For editorial synthesis, use Cursor with "
            "CURSOR_SYNTHESIS_INSTRUCTIONS.md and this month’s dump."
        )
        return SynthesizedReport(
            year_month=year_month,
            total_entries=len(entries),
            projects=projects,
            sections={k: v for k, v in sections.items() if v},
            people=sorted(all_people),
            closing_narrative=narrative,
        )

    def _clean_entry_text(self, content: str) -> str:
        text = " ".join(content.split())
        text = re.sub(r"TODO:?\s*", "", text)
        text = re.sub(r"-\s*\[[ x]\]\s*#todo\s*", "", text)
        text = re.sub(r"📅\s*\d{4}-\d{2}-\d{2}", "", text)
        text = re.sub(r"✅\s*\d{4}-\d{2}-\d{2}", "", text)
        if len(text) > 250:
            text = text[:247] + "..."
        if text:
            text = text[0].upper() + text[1:]
        return text.strip()


# Backward compatibility for imports
AICategorizor = JournalCategorizor
