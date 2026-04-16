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
