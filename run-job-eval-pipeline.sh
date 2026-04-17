#!/usr/bin/env bash
# One command: Stage 1 (batch evals) + Stage 2 (overview). Run from anywhere; uses repo root.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$ROOT/journal_summarizer/scripts/run_job_eval_pipeline.py" "$@"
