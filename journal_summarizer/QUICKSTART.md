# Quick Start Guide

## First Time Setup

1. **Navigate to the journal_summarizer directory:**
   ```bash
   cd journal_summarizer
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

No API keys are required. Summaries use **local rule-based** tagging and categorization.

## Common Usage

### From live journals (parsed from `journals_directory` in config)

```bash
python3 summarizer.py --dry-run --all
python3 summarizer.py --month 2024-08
python3 summarizer.py --all
```

### From collated `monthly_dumps/*.md` (recommended for Cursor workflow)

```bash
python3 summarizer.py --from-dumps --dry-run --all
python3 summarizer.py --from-dumps --month 2024-08
python3 summarizer.py --from-dumps --all
```

### Regenerate raw dumps only (no summaries)

```bash
python3 summarizer.py --dump-mode --all
```

## Output

- Summaries: `summaries/YYYY-MM.md` (controlled vocabulary tags on bullets).
- Raw months: `monthly_dumps/YYYY-MM.md` from `--dump-mode`.

## Editorial polish in Cursor

Open **`CURSOR_SYNTHESIS_INSTRUCTIONS.md`** in Cursor together with `monthly_dumps/YYYY-MM.md` and ask for a rewritten `summaries/YYYY-MM.md` following that spec.

## Customization

Edit `config.yaml` for paths, globs, and processing options. Tag routing logic lives in `categorizer.py` (`infer_tag_from_project`).
