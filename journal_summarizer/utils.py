"""Utility functions for journal summarizer."""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any
import yaml


def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file."""
    config_file = Path(__file__).parent / config_path
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def parse_timestamp(line: str, patterns: List[Dict[str, str]]) -> Optional[datetime]:
    """
    Parse timestamp from line using multiple patterns.
    
    Args:
        line: Line of text potentially containing a timestamp
        patterns: List of dicts with 'pattern' (regex) and 'format' (strptime format)
    
    Returns:
        datetime object if timestamp found, None otherwise
    """
    for pattern_config in patterns:
        pattern = pattern_config['pattern']
        date_format = pattern_config['format']
        
        match = re.match(pattern, line.strip())
        if match:
            timestamp_str = match.group(1)
            try:
                return datetime.strptime(timestamp_str, date_format)
            except ValueError:
                continue
    
    return None


def get_project_name(file_path: Path, base_dir: Path) -> str:
    """
    Extract project name from file path.
    
    Args:
        file_path: Path to journal file
        base_dir: Base directory for journals
    
    Returns:
        Project name derived from filename
    """
    # Remove common suffixes
    name = file_path.stem
    for suffix in [' journal', ' notes', ' work journal']:
        name = name.replace(suffix, '')
    
    return name.strip() or file_path.stem


def should_exclude_file(file_path: Path, exclude_patterns: List[str]) -> bool:
    """
    Check if file should be excluded based on patterns.
    
    Args:
        file_path: Path to check
        exclude_patterns: List of glob patterns to exclude
    
    Returns:
        True if file should be excluded
    """
    file_name = file_path.name
    for pattern in exclude_patterns:
        if Path(file_name).match(pattern.replace('**/', '')):
            return True
    return False


def truncate_text(text: str, max_length: int) -> str:
    """
    Truncate text to max_length, preserving word boundaries.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
    
    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length].rsplit(' ', 1)[0]
    return truncated + '...'


def format_month_name(year_month: str) -> str:
    """
    Format YYYY-MM to readable month name.
    
    Args:
        year_month: String in format "YYYY-MM"
    
    Returns:
        Formatted string like "January 2024"
    """
    try:
        date = datetime.strptime(year_month, "%Y-%m")
        return date.strftime("%B %Y")
    except ValueError:
        return year_month
