# Job evaluation reports

This folder stores **one markdown file per evaluation run**.

## Naming

Let `<JD>` be the basename of the job description file (no directory), e.g.:

- JD file: `job descriptions/Lead UX, Gamebreaking`
- Basename: `Lead UX, Gamebreaking`

### Default output filename

`job-evaluation-reports/<JD>.eval.md`

Example:

- `job-evaluation-reports/Lead UX, Gamebreaking.eval.md`

## Re-runs / collisions

If `job-evaluation-reports/<JD>.eval.md` already exists, write a dated variant:

- `job-evaluation-reports/<JD>.eval - YYYY-MM-DD.md`

If that dated file also exists (multiple runs the same day), append an increment:

- `job-evaluation-reports/<JD>.eval - YYYY-MM-DD - 2.md`
- `job-evaluation-reports/<JD>.eval - YYYY-MM-DD - 3.md`
- …

## Source of truth

The canonical rules live in:

- `JOB_EVALUATION_TEMPLATE.md`
- `JOB_EVALUATION_REFERENCES.md`

## Batch workflow (many JDs)

### One command (Stage 1 + Stage 2)

From the **repository root**, the default is: **skip JDs that already have eval reports**, then **write a new collated overview** with a **timestamped filename** that includes the **job count** (see below).

```bash
./run-job-eval-pipeline.sh
```

Or:

```bash
make job-eval
```

| Make target | What it runs |
| --- | --- |
| `make job-eval` | Same as `./run-job-eval-pipeline.sh` (skip existing reports, then collate). |
| `make job-eval-fresh` | Re-run the agent for **every** JD (`--no-skip-existing`), then collate. |
| `make job-eval-overview` | **Stage 2 only** — collate from existing reports into a new timestamped overview. |

Pipeline flags (see `python3 journal_summarizer/scripts/run_job_eval_pipeline.py --help`): `--dry-run` (Stage 1 preview only; **no** new overview file), `--only GLOB`, `--stage1-only`, `--stage2-only`, `--no-skip-existing`, `--model MODEL`, `--heartbeat-sec SEC`, `--out`, etc.

If Stage 1 has partial failures, Stage 2 still runs so your overview stays in sync with whatever reports exist.

### Stage 1 — Automated evaluations (Cursor Agent CLI)

Prerequisites:

- [Cursor Agent CLI](https://cursor.com/docs/cli) installed so `agent` is on your `PATH` (or set `CURSOR_AGENT_BIN` to the executable).
- Authenticated for non-interactive runs: e.g. `agent login` / `agent status`, or `CURSOR_API_KEY` per [CLI parameters](https://cursor.com/docs/cli/reference/parameters).
- Run from the **repo root** (or pass `--repo`).

The driver invokes `agent --print --force --trust --workspace <repo> "<prompt>"` once per job-description file under `job descriptions/`. If you pass `--model MODEL`, the driver also forwards `agent --model MODEL`. Each prompt instructs the agent to read the template, references, chat command, that JD file, and to **write** the full report here using the same naming rules as a manual run.

`--force` and `--trust` grant the agent broad approval to run tools and modify files in the workspace. Use only on a **trusted** checkout.

After each successful `agent` exit, the driver checks that some report under `job-evaluation-reports/` for that JD basename was **created or updated** (mtime). If not, the run is treated as a failure and `output_verified: false` is recorded in the JSONL log.

From the repo root:

```bash
python3 journal_summarizer/scripts/batch_job_evaluations.py
```

Useful flags:

| Flag | Meaning |
| --- | --- |
| `--dry-run` | List what would run; do not call `agent`. |
| `--skip-existing` | Skip JDs that already have **any** well-formed eval report for that `<JD>` basename (including dated collision names like `<JD>.eval - YYYY-MM-DD.md`). |
| `--only 'GLOB'` | Limit to basename patterns (repeatable), e.g. `--only '*Riot*'`. |
| `--log PATH` | JSONL run log (default: `_batch_runs.jsonl` in this folder). |
| `--timeout SEC` | Per-JD timeout (default 2400). |
| `--agent-bin PATH` | Use a specific `agent` binary. |
| `--model MODEL` | Force a specific Cursor Agent model for Stage 1, e.g. `--model gpt-5.4-medium`. |
| `--heartbeat-sec SEC` | Print a **still running** line every `SEC` seconds while each agent invocation runs (default **30**; use **0** to disable). The agent often buffers output until completion; this makes long runs visible. |

Exit codes: `0` all JD steps succeeded and output was verified; `1` one or more agent failures or “exit 0 but no report written” cases; `2` bad `--repo` / `--jd-dir` or JD path outside repo; `3` no job-description files matched; `127` `agent` not found on `PATH`.

JSONL log lines include `output_verified` (`true` / `false` / `null` on skip or non-zero agent exit) when an agent run finished.

Example (one role, dry run):

```bash
python3 journal_summarizer/scripts/batch_job_evaluations.py --dry-run --only '*Riot*'
```

Example (full rerun with an explicit model):

```bash
./run-job-eval-pipeline.sh --no-skip-existing --model gpt-5.4-medium
```

### Stage 2 — Collated overview

After reports exist in this folder, run the collator (below). Each run creates a **new** markdown file so you can keep history.

## Collated overview files (`_OVERVIEW-*.md`)

Script:

- `journal_summarizer/scripts/collate_job_evaluations.py`

**Default output name** (when you omit `--out`):

`job-evaluation-reports/_OVERVIEW-<YYYYMMDD-HHMMSS>(<n>).md`

Examples:

- `job-evaluation-reports/_OVERVIEW-20260417-183045(1).md`
- `job-evaluation-reports/_OVERVIEW-20260417-183045(3).md`

`<n>` is the number of distinct JD rows in the summary table (one row per deduped eval report). If that exact name already exists (same second, same count), the filename gets `-1`, `-2`, … before `.md` (for example `_OVERVIEW-20260417-183045(3)-1.md`). Older runs may use other patterns such as `OVERVIEW-*_N-records.md`.

Run from the repo root:

```bash
python3 journal_summarizer/scripts/collate_job_evaluations.py
```

### Plotly HTML dashboard (optional)

Same data as the summary table, as an interactive **standalone HTML** file (six views: heatmap, grouped bars, radar, parallel coordinates, dot plots, bump chart). Requires `plotly` (see `journal_summarizer/requirements.txt`).

```bash
pip install -r journal_summarizer/requirements.txt
python3 journal_summarizer/scripts/collate_job_evaluations.py --html
```

Writes `_OVERVIEW-<timestamp>(<n>).html` next to the markdown when `--out` is omitted, or `<your-out>.html` if you used `--out path.md`. Use `--html-out path/to/custom.html` to set the HTML path explicitly.

The **radar** view can get crowded with many jobs; use the Plotly **legend** to toggle traces. The markdown overview remains the canonical text artifact.

To include HTML from the full pipeline (Stage 2 only or after Stage 1):

```bash
./run-job-eval-pipeline.sh --stage2-only --html
```

To pin a **fixed** path (overwrites that file each time), pass `--out` (optional; most runs should omit this so each collate run keeps a new timestamped file):

```bash
python3 journal_summarizer/scripts/collate_job_evaluations.py --out job-evaluation-reports/_OVERVIEW-latest.md
```

What it does:

- Scans this folder for `*.eval*.md` reports (skips `README.md`, collated `_OVERVIEW*.md` / legacy `OVERVIEW-*.md`, `_QUEUE*.md`).
- **Dedupes** multiple reports for the same `<JD>` basename by picking the **latest file modification time** (`mtime`).
- Extracts:
  - `` `job` `` from the header metadata
  - the **PART 5 verdict lines only** (the five “likelihood / fit / narrative” bullets), with a link to the full report

Filename contract (important for dedupe):

- Reports must match: `<JD>.eval.md` or `<JD>.eval - YYYY-MM-DD.md` (optional `- N` same-day suffix).
- The dedupe key is the `<JD>` basename before `.eval`.

Cross-check:

- If `` `jd_source` `` implies a different JD basename than the filename key, the overview will include a **mismatch warning** for that row.
