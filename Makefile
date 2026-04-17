# Job evaluation pipeline (Stage 1 batch + Stage 2 overview). Requires Cursor Agent CLI for Stage 1.
.PHONY: job-eval job-eval-fresh job-eval-overview job-eval-overview-html

job-eval:
	./run-job-eval-pipeline.sh

job-eval-fresh:
	./run-job-eval-pipeline.sh --no-skip-existing

job-eval-overview:
	./run-job-eval-pipeline.sh --stage2-only

job-eval-overview-html:
	./run-job-eval-pipeline.sh --stage2-only --html
