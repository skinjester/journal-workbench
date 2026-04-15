# Journal Workbench

**Journal Workbench** is a small toolkit for turning timestamped work journals into structured monthly summaries. Parsing, tagging, and first-pass categorization run locally with rule-based heuristics; narrative polish is meant to happen in the editor (for example with [Cursor](https://cursor.com)) using the included synthesis instructions—no LLM API keys are required for the pipeline itself.

## Repository layout

| Path | Role |
|------|------|
| `journals/` | Place markdown or text journal files here (or point `journals_directory` in config at a vault that contains them). |
| `journal_summarizer/` | Python CLI, config, parsers, and generated outputs (`summaries/`, optional dumps and visualizations). |
| `reporting-template.md` | Section headings aligned with generated reports (Goals, Workstream, Artifacts Delivered, etc.). |

Full feature list, journal timestamp formats, troubleshooting, and advanced flags (`--dry-run`, `--dump-mode`, `--from-dumps`) are documented in [`journal_summarizer/README.md`](journal_summarizer/README.md).

## Quick start

1. **Configure** — In `journal_summarizer/config.yaml`, set `journals_directory` to the folder that contains your journal files (often the repo root or an Obsidian vault path that includes `journals/`). Adjust `include_patterns` / `exclude_patterns` if needed.

2. **Install and run** (from `journal_summarizer/`):

   ```bash
   cd journal_summarizer
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python3 summarizer.py --month YYYY-MM   # or --all, --year YYYY, --from/--to
   ```

3. **Outputs** — Monthly markdown files are written under `journal_summarizer/summaries/` as `YYYY-MM.md` (path configurable via `output_directory` in `config.yaml`).

For step-by-step usage and Cursor-oriented synthesis, see [`journal_summarizer/QUICKSTART.md`](journal_summarizer/QUICKSTART.md) and `journal_summarizer/CURSOR_SYNTHESIS_INSTRUCTIONS.md`.

## Project matrix visualization

After you have tagged summaries under `journal_summarizer/summaries/`, you can rebuild the data for the bundled HTML view:

```bash
cd journal_summarizer
python3 build_project_matrix.py
```

Optional: `--html path/to.html` or `--summaries summaries/ --stdout` to inspect JSON only. Details are in the docstring at the top of [`journal_summarizer/build_project_matrix.py`](journal_summarizer/build_project_matrix.py).

## Requirements

- **Python** 3.9+  
- Dependencies: `journal_summarizer/requirements.txt` (`PyYAML`, `rich`, `python-dateutil`)

## Resume To Google Doc

If you want to turn a local Markdown resume into a Google Doc, use:

```bash
cd journal_summarizer
pip install -r requirements.txt
python3 scripts/resume_to_google_doc.py \
  --input ../resumes/gboodhoo-resume-connect.md \
  --title "Gary Boodhoo Resume" \
  --credentials ../google-docs-credentials.json
```

On first run the script opens a browser for Google OAuth, caches a token locally, and prints the new Google Doc URL.

---

This repository is private; keep `config.yaml` paths and any journal content out of commits if they reference machines or accounts you do not intend to share.
