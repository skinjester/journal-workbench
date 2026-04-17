# Journal Summarizer

Automatically collate timestamped work journals and generate monthly summary reports.

## Overview

This tool scans your work journals (markdown and text files), extracts timestamped entries, categorizes them with **local heuristics**, and writes monthly summaries with a **controlled project-tag** vocabulary. **Editorial** synthesis is meant to be done in **Cursor** (see `CURSOR_SYNTHESIS_INSTRUCTIONS.md`); no OpenAI or Anthropic API is used.

## Quick Start

```bash
# Setup (first time only)
cd journal_summarizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generate a single month
python3 summarizer.py --month 2024-08

# Generate all months
python3 summarizer.py --all
```

See [QUICKSTART.md](QUICKSTART.md) for detailed usage instructions.

## Features

- **Multi-format timestamp detection**: Handles various timestamp formats across different journals
- **Rule-based categorization**: Keyword heuristics only (no external LLM APIs)
- **Cursor-friendly**: Dumps + instructions for in-editor editorial synthesis
- **Flexible date filtering**: Generate reports for specific months, years, or date ranges
- **Combined project view**: Consolidates all project journals into unified monthly reports
- **People extraction**: Automatically identifies collaborators mentioned in entries
- **Batch processing**: Efficiently handles large journals with thousands of entries

## Configuration

Edit `config.yaml` to customize:
- Journal directory location (in this vault, `journals_directory` is the **`journal-workbench`** folder: it contains `journals/` and `journal_summarizer/` as siblings, and the summarizer excludes its own tree via `exclude_patterns`)
- (No AI provider — use Cursor for narrative synthesis)
- File inclusion/exclusion patterns
- Output directory for summaries
- Processing options

## Usage

### Generate all monthly summaries
```bash
python summarizer.py --all
```

### Generate for a specific month
```bash
python summarizer.py --month 2024-08
```

### Generate for a date range
```bash
python summarizer.py --from 2024-01 --to 2024-12
```

### Generate for an entire year
```bash
python summarizer.py --year 2024
```

### Preview without generating (dry run)
```bash
python summarizer.py --all --dry-run
```

## Output

Reports are generated in the `summaries/` directory (configurable) as `YYYY-MM.md`.

Each synthesized report includes:
- **Goals**, **Workstream**, **Artifacts Delivered**, **Key Decisions**, **Open Questions / Follow Ups** (bullets use `- **[TAG]** …` with the controlled vocabulary)
- **People Involved**
- Horizontal rule and optional *closing paragraph* (see `CURSOR_SYNTHESIS_INSTRUCTIONS.md`)

## Supported Journal Formats

The parser detects multiple timestamp formats:
- `# ✎ 2024-08-11 05:14`
- `### 2024-08-11 05:14`
- `2024-08-11 05:14:32`
- `2024-08-11 05:14`

## Requirements

- Python 3.9 or higher
- Journal files in markdown or text format

## Troubleshooting

**No entries found:**
- Check that `journals_directory` in `config.yaml` points to the correct location
- Verify your journal files contain supported timestamp formats

**Missing categories:**
- Entries without clear categorization default to "Workstream"
- Adjust keyword rules in `categorizer.py` if needed

## Example Output

```markdown
### Goals
None identified

### Workstream
- **[OPS]** Mirrored HD-4TB Users/Gary branch to NVMe and relocated Win11 desktop folders to the faster drive after discovering the profile had landed on spinning rust.

### People Involved
None identified

---
*Closing paragraph after editorial pass in Cursor…*
```

## Tests

From `journal_summarizer/` (with dev dependencies installed: `pip install -r requirements.txt`):

```bash
python3 -m pytest
```

Includes `tests/test_collate_job_evaluations.py` for the job-evaluation overview collator.

## Notes

- Large journals are processed in batches for memory; there is no external inference API.
- Re-running overwrites `summaries/YYYY-MM.md`; originals are never modified.
