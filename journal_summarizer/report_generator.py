"""Report generation module."""

from datetime import datetime
from pathlib import Path
from typing import List, Dict
from collections import defaultdict

from parsers import JournalEntry
from categorizer import CategorizedEntry, SynthesizedReport, SYNTHESIS_SECTION_ORDER
from utils import format_month_name, truncate_text


class ReportGenerator:
    """Generates monthly summary reports from categorized entries."""
    
    def __init__(self, config: Dict):
        """
        Initialize report generator with configuration.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.template_sections = config.get('template_sections', [])
        self.output_dir = Path(config.get('output_directory', 'summaries'))
        self.max_entry_length = config.get('processing', {}).get('max_entry_length', 500)
    
    def generate_monthly_report(
        self, 
        year_month: str, 
        categorized_entries: List[CategorizedEntry]
    ) -> str:
        """
        Generate a single monthly report.
        
        Args:
            year_month: Month in YYYY-MM format
            categorized_entries: List of categorized entries for the month
        
        Returns:
            Path to generated report file
        """
        # Group entries by category
        entries_by_category = self._group_by_category(categorized_entries)
        
        # Generate report content
        report_content = self._build_report_content(year_month, categorized_entries, entries_by_category)
        
        # Write to file
        output_path = self.output_dir / f"summary-{year_month}.md"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return str(output_path)
    
    def _group_by_category(
        self, 
        categorized_entries: List[CategorizedEntry]
    ) -> Dict[str, List[CategorizedEntry]]:
        """Group categorized entries by their assigned categories."""
        grouped = defaultdict(list)
        
        for cat_entry in categorized_entries:
            if not cat_entry.categories:
                # Entries without categories go to "Workstream" as default
                grouped["Workstream"].append(cat_entry)
            else:
                for category in cat_entry.categories:
                    grouped[category].append(cat_entry)
        
        return grouped
    
    def _build_report_content(
        self, 
        year_month: str, 
        all_entries: List[CategorizedEntry],
        entries_by_category: Dict[str, List[CategorizedEntry]]
    ) -> str:
        """Build the markdown content for the report."""
        month_name = format_month_name(year_month)
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Calculate statistics
        total_entries = len(all_entries)
        projects = set(entry.entry.project for entry in all_entries)
        project_count = len(projects)
        
        # Collect all unique people
        all_people = set()
        for cat_entry in all_entries:
            all_people.update(cat_entry.people)
        
        # Build report
        lines = []
        lines.append(f"# Monthly Summary: {month_name}")
        lines.append(f"**Generated:** {today}")
        lines.append(f"**Entries:** {total_entries} from {project_count} projects")
        lines.append(f"**Projects:** {', '.join(sorted(projects))}")
        lines.append("")
        
        # Add each section
        for section in self.template_sections:
            lines.append(f"### {section}")
            lines.append("")
            
            if section == "People Involved":
                # Special handling for people section
                if all_people:
                    for person in sorted(all_people):
                        lines.append(f"- {person}")
                lines.append("")
                continue
            
            # Regular sections
            if section in entries_by_category:
                section_entries = entries_by_category[section]
                
                for cat_entry in section_entries:
                    entry = cat_entry.entry
                    date_str = entry.formatted_date
                    project = entry.project
                    
                    # Use summary if available, otherwise truncate content
                    content = cat_entry.summary if cat_entry.summary else entry.content
                    if len(content) > self.max_entry_length:
                        content = truncate_text(content, self.max_entry_length)
                    
                    # Format as bullet point with metadata
                    # Remove newlines from content for cleaner display
                    content_clean = ' '.join(content.split('\n'))
                    lines.append(f"- **[{date_str}]** *({project})* {content_clean}")
                
                lines.append("")
            else:
                lines.append("")
        
        return '\n'.join(lines)
    
    def generate_synthesized_report(
        self,
        synthesized: SynthesizedReport
    ) -> str:
        """
        Generate a synthesized monthly report (editorial style).
        
        Args:
            synthesized: SynthesizedReport with editorial summaries
        
        Returns:
            Path to generated report file
        """
        def norm_bullet(b: str) -> str:
            b = (b or "").strip()
            if b.startswith("- "):
                return b
            return f"- {b}"

        lines: List[str] = []
        for section in SYNTHESIS_SECTION_ORDER:
            lines.append(f"### {section}")
            lines.append("")
            bullets = synthesized.sections.get(section, [])
            if bullets:
                for bullet in bullets:
                    lines.append(norm_bullet(bullet))
            else:
                lines.append("None identified")
            lines.append("")

        lines.append("### People Involved")
        lines.append("")
        people = [p for p in (synthesized.people or []) if str(p).strip()]
        if people:
            for p in sorted(set(people), key=str.lower):
                lines.append(f"- {p}")
        else:
            lines.append("None identified")
        lines.append("")
        lines.append("---")
        lines.append("")
        narrative = (synthesized.closing_narrative or "").strip()
        if narrative:
            lines.append(f"*{narrative}*")

        # Write to file
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = self.output_dir / f"{synthesized.year_month}.md"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return str(output_path)
    
    def generate_all_reports(
        self,
        monthly_entries: Dict[str, List[JournalEntry]],
        categorizer
    ) -> List[str]:
        """
        Generate reports for all months.
        
        Args:
            monthly_entries: Dictionary mapping YYYY-MM to entries
            categorizer: JournalCategorizor (or AICategorizor alias) for synthesis
        
        Returns:
            List of paths to generated report files
        """
        generated_reports = []
        
        for year_month, entries in monthly_entries.items():
            print(f"\nGenerating report for {format_month_name(year_month)}...")
            print(f"  Processing {len(entries)} entries...")
            
            # Synthesize entries into editorial summary
            synthesized = categorizer.synthesize_monthly_report(entries, year_month)
            
            # Generate report
            report_path = self.generate_synthesized_report(synthesized)
            generated_reports.append(report_path)
            
            print(f"  Report saved to: {report_path}")
        
        return generated_reports
