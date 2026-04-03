"""Journal entry parsing module."""

import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field

from utils import parse_timestamp, get_project_name, should_exclude_file


@dataclass
class JournalEntry:
    """Represents a single timestamped journal entry."""
    timestamp: datetime
    content: str
    project: str
    source_file: str
    line_number: int = 0
    
    @property
    def year_month(self) -> str:
        """Return YYYY-MM format for grouping."""
        return self.timestamp.strftime("%Y-%m")
    
    @property
    def formatted_date(self) -> str:
        """Return formatted date for display."""
        return self.timestamp.strftime("%Y-%m-%d %H:%M")


class JournalParser:
    """Parser for extracting timestamped entries from journal files."""
    
    def __init__(self, config: Dict):
        """
        Initialize parser with configuration.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.journals_dir = Path(config['journals_directory'])
        self.include_patterns = config.get('include_patterns', ['*.md', '*.txt'])
        self.exclude_patterns = config.get('exclude_patterns', [])
        self.timestamp_patterns = config.get('timestamp_patterns', [])
    
    def find_journal_files(self) -> List[Path]:
        """
        Find all journal files matching include patterns.
        
        Returns:
            List of Path objects for journal files
        """
        journal_files = []
        
        for pattern in self.include_patterns:
            for file_path in self.journals_dir.rglob(pattern):
                if file_path.is_file():
                    # Check if file is in excluded path
                    relative_path = str(file_path.relative_to(self.journals_dir))
                    
                    # Check exclusion patterns
                    excluded = False
                    for exclude_pattern in self.exclude_patterns:
                        # Simple pattern matching
                        if exclude_pattern.startswith('**/') and exclude_pattern.endswith('/**'):
                            # Directory pattern like **/venv/**
                            dir_name = exclude_pattern[3:-3]
                            if f"/{dir_name}/" in f"/{relative_path}/" or relative_path.startswith(f"{dir_name}/"):
                                excluded = True
                                break
                        elif should_exclude_file(file_path, [exclude_pattern]):
                            excluded = True
                            break
                    
                    if not excluded:
                        journal_files.append(file_path)
        
        return sorted(journal_files)
    
    def parse_file(self, file_path: Path) -> List[JournalEntry]:
        """
        Parse a single journal file and extract all entries.
        
        Args:
            file_path: Path to journal file
        
        Returns:
            List of JournalEntry objects
        """
        entries = []
        current_entry: Optional[Dict] = None
        project_name = get_project_name(file_path, self.journals_dir)
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return entries
        
        for line_num, line in enumerate(lines, start=1):
            timestamp = parse_timestamp(line, self.timestamp_patterns)
            
            if timestamp:
                # Save previous entry if exists
                if current_entry and current_entry['content'].strip():
                    entries.append(JournalEntry(
                        timestamp=current_entry['timestamp'],
                        content=current_entry['content'].strip(),
                        project=project_name,
                        source_file=str(file_path.relative_to(self.journals_dir)),
                        line_number=current_entry['line_number']
                    ))
                
                # Start new entry
                current_entry = {
                    'timestamp': timestamp,
                    'content': '',
                    'line_number': line_num
                }
            elif current_entry is not None:
                # Append to current entry content
                current_entry['content'] += line
        
        # Save last entry
        if current_entry and current_entry['content'].strip():
            entries.append(JournalEntry(
                timestamp=current_entry['timestamp'],
                content=current_entry['content'].strip(),
                project=project_name,
                source_file=str(file_path.relative_to(self.journals_dir)),
                line_number=current_entry['line_number']
            ))
        
        return entries
    
    def parse_all_journals(self) -> List[JournalEntry]:
        """
        Parse all journal files and return all entries.
        
        Returns:
            List of all JournalEntry objects across all journals
        """
        all_entries = []
        journal_files = self.find_journal_files()
        
        print(f"Found {len(journal_files)} journal files to process")
        
        for file_path in journal_files:
            print(f"Parsing {file_path.name}...")
            entries = self.parse_file(file_path)
            all_entries.extend(entries)
            print(f"  Found {len(entries)} entries")
        
        # Sort all entries by timestamp
        all_entries.sort(key=lambda e: e.timestamp)
        
        return all_entries
    
    def group_by_month(self, entries: List[JournalEntry]) -> Dict[str, List[JournalEntry]]:
        """
        Group entries by year-month.
        
        Args:
            entries: List of journal entries
        
        Returns:
            Dictionary mapping YYYY-MM to list of entries for that month
        """
        grouped = {}
        
        for entry in entries:
            month_key = entry.year_month
            if month_key not in grouped:
                grouped[month_key] = []
            grouped[month_key].append(entry)
        
        # Sort each month's entries chronologically
        for month_key in grouped:
            grouped[month_key].sort(key=lambda e: e.timestamp)
        
        return dict(sorted(grouped.items()))


# Header used in monthly_dumps/*.md (see summarizer.py --dump-mode)
_DUMP_SECTION_RE = re.compile(
    r"^## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+(.+?)\s*$",
    re.MULTILINE,
)


def parse_monthly_dump(dump_path: Path) -> List[JournalEntry]:
    """
    Parse a collated monthly dump file into JournalEntry objects.

    Expects sections like: ## [YYYY-MM-DD HH:MM] project-name
    """
    dump_path = Path(dump_path)
    text = dump_path.read_text(encoding="utf-8", errors="replace")
    matches = list(_DUMP_SECTION_RE.finditer(text))
    if not matches:
        return []

    rel = str(dump_path)
    entries: List[JournalEntry] = []

    for i, m in enumerate(matches):
        ts_raw, project = m.group(1), m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        # Drop trailing --- separators / whitespace
        content = block.strip()
        content = re.sub(r"\n---\s*$", "", content).strip()

        try:
            ts = datetime.strptime(ts_raw, "%Y-%m-%d %H:%M")
        except ValueError:
            continue

        entries.append(
            JournalEntry(
                timestamp=ts,
                content=content,
                project=project,
                source_file=rel,
                line_number=0,
            )
        )

    entries.sort(key=lambda e: e.timestamp)
    return entries


def load_monthly_dumps(dumps_dir: Path) -> Dict[str, List[JournalEntry]]:
    """
    Load all YYYY-MM.md files from dumps_dir; return month -> entries sorted by time.
    """
    dumps_dir = Path(dumps_dir)
    grouped: Dict[str, List[JournalEntry]] = {}
    for path in sorted(dumps_dir.glob("*.md")):
        stem = path.stem
        if not re.match(r"^\d{4}-\d{2}$", stem):
            continue
        grouped[stem] = parse_monthly_dump(path)
    return dict(sorted(grouped.items()))
