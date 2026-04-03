#!/usr/bin/env python3
"""
Journal Summarizer - Generate monthly summaries from timestamped work journals.

Parses timestamped entries, applies local rule-based categorization and
controlled-vocabulary tags, and writes markdown reports. Editorial synthesis
is intended to be done in Cursor (see CURSOR_SYNTHESIS_INSTRUCTIONS.md); no
external LLM API keys are used.
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from utils import load_config, format_month_name
from parsers import JournalParser, load_monthly_dumps
from categorizer import JournalCategorizor
from report_generator import ReportGenerator


console = Console()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate monthly summaries from work journals',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all                    Generate summaries for all months
  %(prog)s --month 2024-08          Generate summary for August 2024
  %(prog)s --from 2024-01 --to 2024-12  Generate summaries for 2024
  %(prog)s --year 2024              Generate summaries for all of 2024
        """
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate summaries for all months with journal entries'
    )
    
    parser.add_argument(
        '--month',
        type=str,
        metavar='YYYY-MM',
        help='Generate summary for specific month (e.g., 2024-08)'
    )
    
    parser.add_argument(
        '--from',
        type=str,
        dest='from_month',
        metavar='YYYY-MM',
        help='Start month for range (inclusive)'
    )
    
    parser.add_argument(
        '--to',
        type=str,
        dest='to_month',
        metavar='YYYY-MM',
        help='End month for range (inclusive)'
    )
    
    parser.add_argument(
        '--year',
        type=str,
        metavar='YYYY',
        help='Generate summaries for all months in specific year'
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config.yaml',
        help='Path to configuration file (default: config.yaml)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Parse journals and show statistics without generating reports'
    )
    
    parser.add_argument(
        '--dump-mode',
        action='store_true',
        help='Create raw monthly dumps for manual synthesis in Cursor (no AI API needed)'
    )

    parser.add_argument(
        '--from-dumps',
        action='store_true',
        help='Read inputs from monthly_dumps/*.md instead of parsing live journals'
    )
    
    return parser.parse_args()


def filter_by_date_range(
    monthly_entries: dict,
    from_month: Optional[str] = None,
    to_month: Optional[str] = None
) -> dict:
    """Filter monthly entries by date range."""
    if not from_month and not to_month:
        return monthly_entries
    
    filtered = {}
    for year_month, entries in monthly_entries.items():
        if from_month and year_month < from_month:
            continue
        if to_month and year_month > to_month:
            continue
        filtered[year_month] = entries
    
    return filtered


def main():
    """Main execution function."""
    args = parse_arguments()
    
    try:
        # Load configuration
        console.print("\n[bold blue]Journal Summarizer[/bold blue]")
        console.print("=" * 50)
        
        config = load_config(args.config)
        console.print(f"[green]✓[/green] Loaded configuration from {args.config}")
        
        # Initialize components
        parser = JournalParser(config)
        categorizer = JournalCategorizor(config)
        generator = ReportGenerator(config)
        
        console.print(f"[green]✓[/green] Initialized components")
        console.print()
        
        summarizer_root = Path(__file__).resolve().parent

        if args.from_dumps:
            dumps_dir = summarizer_root / "monthly_dumps"
            console.print(f"[bold]Loading monthly dumps from[/bold] {dumps_dir}")
            monthly_entries = load_monthly_dumps(dumps_dir)
            monthly_entries = {k: v for k, v in monthly_entries.items() if v}
            if not monthly_entries:
                console.print("[yellow]No entries found in monthly_dumps[/yellow]")
                return 0
            console.print(f"[green]✓[/green] Loaded {len(monthly_entries)} month files from dumps")
            console.print()
        else:
            # Parse all journals
            console.print("[bold]Parsing journal files...[/bold]")
            all_entries = parser.parse_all_journals()

            if not all_entries:
                console.print("[yellow]No journal entries found![/yellow]")
                return 0

            console.print(f"[green]✓[/green] Found {len(all_entries)} total entries")

            # Group by month
            monthly_entries = parser.group_by_month(all_entries)
            console.print(f"[green]✓[/green] Grouped into {len(monthly_entries)} months")
            console.print()
        
        # Apply filters based on arguments
        if args.month:
            monthly_entries = {args.month: monthly_entries.get(args.month, [])}
            if not monthly_entries[args.month]:
                console.print(f"[yellow]No entries found for {args.month}[/yellow]")
                return 0
        
        elif args.year:
            year_prefix = args.year
            monthly_entries = {
                k: v for k, v in monthly_entries.items() 
                if k.startswith(year_prefix)
            }
            if not monthly_entries:
                console.print(f"[yellow]No entries found for year {args.year}[/yellow]")
                return 0
        
        elif args.from_month or args.to_month:
            monthly_entries = filter_by_date_range(
                monthly_entries, 
                args.from_month, 
                args.to_month
            )
            if not monthly_entries:
                console.print("[yellow]No entries found in specified range[/yellow]")
                return 0
        
        # Show statistics
        console.print("[bold]Month Overview:[/bold]")
        for year_month, entries in monthly_entries.items():
            month_name = format_month_name(year_month)
            projects = set(e.project for e in entries)
            console.print(f"  {month_name}: {len(entries)} entries from {len(projects)} projects")
        console.print()
        
        # Dry run: stop here
        if args.dry_run:
            console.print("[yellow]Dry run complete. No reports generated.[/yellow]")
            return 0
        
        # Dump mode: create raw monthly files for manual synthesis
        if args.dump_mode:
            console.print("[bold]Creating raw monthly dumps for Cursor synthesis...[/bold]")
            dump_dir = Path("monthly_dumps")
            dump_dir.mkdir(exist_ok=True)
            
            for year_month, entries in monthly_entries.items():
                dump_file = dump_dir / f"{year_month}.md"
                with open(dump_file, 'w', encoding='utf-8') as f:
                    f.write(f"# Raw Entries for {format_month_name(year_month)}\n\n")
                    f.write(f"**Total Entries:** {len(entries)}\n")
                    projects = sorted(set(e.project for e in entries))
                    f.write(f"**Projects:** {', '.join(projects)}\n\n")
                    f.write("---\n\n")
                    
                    for entry in entries:
                        f.write(f"## [{entry.formatted_date}] {entry.project}\n\n")
                        f.write(f"{entry.content}\n\n")
                        f.write("---\n\n")
                
                console.print(f"  Created: {dump_file}")
            
            console.print()
            console.print(f"[bold green]✓ Created {len(monthly_entries)} monthly dump files in monthly_dumps/[/bold green]")
            console.print()
            console.print("[cyan]Next steps:[/cyan]")
            console.print("1. Open CURSOR_SYNTHESIS_INSTRUCTIONS.md in Cursor with a monthly dump")
            console.print("2. Ask Cursor to write summaries/YYYY-MM.md per that spec")
            console.print("3. No external API keys — uses your Cursor subscription for wording")
            return 0
        
        # Generate reports
        console.print("[bold]Generating monthly reports...[/bold]")
        generated_reports = generator.generate_all_reports(monthly_entries, categorizer)
        
        console.print()
        console.print(f"[bold green]✓ Successfully generated {len(generated_reports)} reports[/bold green]")
        console.print()
        console.print("[bold]Generated reports:[/bold]")
        for report_path in generated_reports:
            console.print(f"  - {report_path}")
        
        return 0
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        return 130
    
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
