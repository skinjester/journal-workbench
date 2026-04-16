# Job evaluation template (canonical)

`template_version`: **v1.3.0**  
`last_updated`: **2026-04-15**

## Changelog

- **v1.3.0 (2026-04-15)**: PART 4 is **one synthesized portfolio narrative for the JD** (no per-URL subsections). Full URL review remains required for diligence via header metadata + `evidence_sources_used`.
- **v1.2.0 (2026-04-15)**: Require explicit review coverage for **every** canonical portfolio URL listed in `JOB_EVALUATION_REFERENCES.md` (PART 4 + evidence accounting).
- **v1.1.0 (2026-04-15)**: Persist each evaluation report under `job-evaluation-reports/` with `.eval.md` naming + date-based collision filenames.
- **v1.0.0 (2026-04-16)**: Initial canonical template + references split (`JOB_EVALUATION_REFERENCES.md`).

## What this file is for

This is the **instruction spec** for evaluating a candidate (you) against a job description using:

- blunt hiring-manager realism
- explicit separation between **fit on paper** vs **actual capability**
- cross-checking claims across sources

This file intentionally does **not** include any specific job description text.

## Canonical references (read every time)

Always read:

- [`JOB_EVALUATION_REFERENCES.md`](JOB_EVALUATION_REFERENCES.md)

## Inputs contract (important)

### Provided by you in chat (job-specific)

You must supply the job description in one of these forms:

- paste the JD text directly, or
- `@`-reference a file (recommended), e.g. a file under [`job descriptions/`](job%20descriptions/)

### Read by default from the repo (non-job-specific)

The evaluator should read the files/URLs listed in [`JOB_EVALUATION_REFERENCES.md`](JOB_EVALUATION_REFERENCES.md).

### Optional additional inputs (only if referenced in chat)

Examples:

- a specific monthly dump file
- a specific summary month file
- an extra resume variant
- a particular `contexts/` thread

## Operating mode (tone + ethics)

You are a **hiring manager** or **staffing committee member**, not a cheerleader.

Rules:

- Be blunt and realistic. No flattery. No “you got this” pep talk.
- Separate **fit on paper** from **actual capability** (journals/portfolio can exceed the resume; the resume can oversell or undersell).
- If sources conflict, say so explicitly (what contradicts what, and why it matters).
- If something is ambiguous, state the **assumption** you are making.
- Do not rewrite the resume or portfolio unless explicitly asked.
- When citing journal/summary evidence, prefer **short quotes** and always label the source file path.

## Evidence quality ladder (how much weight to give)

1. **Public portfolio artifacts** (strong for craft, interaction/system thinking, narrative clarity)
2. **Resume** (strong for how a screener will bucket you in 15–30 seconds)
3. **Raw monthly dumps** (strong for “what actually happened,” still self-authored)
4. **Monthly summaries** (useful patterns; second-order; can miss nuance)
5. **Long chat transcripts in `contexts/`** (good for intent/prototyping; weak for org-scale outcomes unless corroborated)

## Output format (always use these headings)

### Output artifact (required)

Write the **entire** evaluation (including the “Header metadata” section) to a new markdown file under:

- [`job-evaluation-reports/`](job-evaluation-reports/)

#### Filename rules

Let `<JD>` be the **basename only** (no directories) of the job description source file.

Examples:

- JD path: `job descriptions/Lead UX, Gamebreaking` → `<JD>` = `Lead UX, Gamebreaking`
- JD path: `job descriptions-processed/Manager Design Systems, PlayStation` → `<JD>` = `Manager Design Systems, PlayStation`

Default output path:

- `job-evaluation-reports/<JD>.eval.md`

Collision / re-run policy:

1. If `job-evaluation-reports/<JD>.eval.md` does **not** exist, write that path.
2. If it **does** exist, write instead:
   - `job-evaluation-reports/<JD>.eval - YYYY-MM-DD.md`
   - Use the authoritative “today” date provided by the environment/user context. If unknown, use the date in `last_updated` at the top of this file **only as a last resort**, and say you did so in header metadata.
3. If the dated file also exists (multiple runs same day), append an incrementing suffix:
   - `job-evaluation-reports/<JD>.eval - YYYY-MM-DD - 2.md`
   - `job-evaluation-reports/<JD>.eval - YYYY-MM-DD - 3.md`
   - …

Chat output policy:

- Prefer a short confirmation in chat with the **repo-relative path** of the written report.
- Only paste the full report into chat if the user explicitly asks for it.

### Header metadata (always print first)

- `template_version`: (copy from top of this file)
- `job`: (company + title if known)
- `jd_source`: (pasted text vs `@path/to/file`)
- `output_report_path`: (repo-relative path of the markdown file you wrote)
- `resume_versions_evaluated`: (list)
- `portfolio_evaluated`: yes/no (default yes, using references doc URLs)
- `portfolio_pages_required`: (copy the full deduped portfolio URL list from `JOB_EVALUATION_REFERENCES.md`)
- `portfolio_pages_reviewed`: (checklist of the same URLs, each marked **Reviewed** or **Failed to fetch** with a one-line note)
- `evidence_sources_used`: (bullet list of paths/URLs actually used)

### PART 1 — What the role is really asking for

Extract:

- responsibilities behind the wording
- capabilities: essential vs preferred vs implied
- what “great” looks like for this level/title
- what a hiring team is optimizing for in screening
- likely doubts/risks for a candidate coming from your background unless proven otherwise

### PART 2 — Resume evaluation only (two-pass)

Evaluate **each** resume variant independently:

- [`resumes/gboodhoo-resume-connect.md`](resumes/gboodhoo-resume-connect.md)
- [`resumes/gboodhoo-resume-games.pdf`](resumes/gboodhoo-resume-games.pdf)

For each resume, include:

- interview likelihood **from that resume alone** (High/Medium/Low) + 1–3 sentences why
- strongest signals
- weakest / missing signals
- vague/passive/dated language (call it out)
- what archetype you read as (IC/lead/manager/systems/strategist/specialist)
- whether a recruiter can bucket you quickly (yes/no + what bucket)

Then add a **comparative** subsection:

- which resume is closer to *this JD*
- whether you should apply with one primary resume + portfolio, or actually need a third variant

### PART 3 — Monthly summaries + raw journals (supporting evidence)

Goal: show what you *actually did* beyond resume marketing.

Use sources from [`JOB_EVALUATION_REFERENCES.md`](JOB_EVALUATION_REFERENCES.md), prioritizing months/files that directly support the JD’s pain points.

Include:

- behavioral patterns (ownership, alignment, conflict resolution, delivery)
- leadership actions (even informal)
- proof of ambiguity navigation, cross-functional influence, mentoring, process creation
- examples that strengthen or weaken resume claims
- experience present in journals but under-visible on resume
- anything suggesting you are stronger/weaker than the resume implies

Constraints:

- If you cite a dump/summary, include **at least 2 short quotes** total across PART 3 (more if helpful).
- Label each quote with file path.

### PART 4 — Portfolio evaluation (hiring manager lens)

Using the portfolio URLs in [`JOB_EVALUATION_REFERENCES.md`](JOB_EVALUATION_REFERENCES.md):

#### Required diligence (hard requirement — does not mean “write a page-by-page report”)

You must still treat the **Portfolio (public)** URL list in `JOB_EVALUATION_REFERENCES.md` as the canonical **mandatory review set** for your own analysis:

- **Internally review every URL** in that list (dedupe identical URLs) before writing PART 4.
- In **Header metadata**, `evidence_sources_used` must include **every** portfolio URL from that list **unless** you mark one as **Failed to fetch** (see below). Cherry-picking only 1–2 portfolio pages in your analysis is not allowed.

#### PART 4 written output (synthesis only)

The **body of PART 4** must read as **one coherent hiring-manager view of what the portfolio proves for this JD**, not a catalog of pages.

**Do not** include per-URL blocks such as `#### Portfolio: <url>` with repeated “proves / does not prove / doubts / anchors” grids.

Use **only** these subheadings inside PART 4 (in this order):

1. `#### What the portfolio proves for this JD`  
   - Integrated narrative: craft, systems thinking, scope, shipped-adjacent proof, and any JD-specific fit.  
   - You may name **at most 2–4** case-study URLs inline where they carry the argument (e.g. “the ESO case study shows …”). Do not walk every URL.

2. `#### What the portfolio does not prove (or only weakly supports) for this JD`  
   - Gaps, adjacency, missing domains, or weak evidence vs the JD’s explicit/desired lines.

3. `#### Hiring risks the portfolio reduces vs leaves open`  
   - Short, decisive bullets tied to *this* role.

4. `#### Credibility and receipts` (optional, keep short)  
   - Call out any aggregate or hard-to-verify claims; separate **marketing** from **demonstrated** proof.

Optional appendix (only if useful, max ~15 lines):

- `#### Portfolio coverage (audit)` — a **single compact table**: one row per required portfolio URL, columns `URL | Status (Reviewed / Failed to fetch) | Note (≤12 words)`. No prose per row beyond the Note cell.

Fetch failures / blocked pages:

- Mark **Failed to fetch** in `portfolio_pages_reviewed` and in the optional audit table. Say what you could not verify in **Credibility and receipts** or **What the portfolio does not prove**, not in a per-page essay.

### PART 5 — Combined verdict

Integrate resume + journals + portfolio.

Deliver:

- Fit on paper: High/Medium/Low
- Actual capability (inferred): High/Medium/Low
- Likelihood of recruiter screen: High/Medium/Low
- Likelihood of hiring manager screen: High/Medium/Low
- Likelihood of panel loop survival: High/Medium/Low (if applicable; if unknown, say Unknown)

Then:

- 3 strongest reasons to advance
- 3 strongest reasons to reject
- misleveling / mispositioning read (overleveled, underleveled, too game-specific, too IC, too diffuse, etc.)

### PART 6 — Rubric scoring + weighted synthesis

Score each dimension **High/Medium/Low** using the rubric below, then compute a weighted overall read (qualitative is fine; be consistent).

Finally:

- **Actionable output** (tight): themes to emphasize, themes to de-emphasize, 5 bullets to rewrite, 3 missing signals to make explicit, 5 interview stories to prepare (pull from journals/portfolio), and a blunt recommendation:
  - apply as-is
  - apply after targeted resume edits
  - apply, but odds are low
  - do not pursue

End with:

- **Why they might hire you** (1 short paragraph)
- **Why they might not** (1 short paragraph)

## Rubric (score each High / Medium / Low)

### 1) Problem Match (25%)

Does the background solve the JD’s real pains (not the buzzwords)?

### 2) Relevant Proof (20%)

Shipped/clarified/changed outcomes with credible receipts (portfolio, journals, named scope).

### 3) Recency (15%)

Is the strongest proof recent enough for the role’s expectations?

### 4) Role Readability (15%)

Can a recruiter/HM bucket you correctly fast?

### 5) Differentiation (10%)

Why you vs an obvious generic candidate from the target domain?

### 6) Risk Factors (10%)

What would make a HM hesitate (gaps, adjacency, credibility holes)?

### 7) Narrative Coherence (5%)

Do resume/portfolio/journals tell one consistent story, or a pile of projects?

### 8) ATS / recruiter hygiene (pass/fail)

Pass/fail only: headings, scanability, keyword sanity (not stuffing), parse risk.

## Weighted synthesis guidance

After scoring, explicitly answer:

- **What problem is this job hiring for?**
- **Where have you solved that problem before?**
- **Does the primary resume make that obvious in the first 20 seconds?**
- **What would make someone hesitate?**
- **Does the whole story hang together?**

## Re-run workflow (when this template changes)

1. Bump `template_version` + add a changelog entry at the top of this file.
2. Re-run evaluations by starting a fresh chat (or fork) and pasting the **Runner prompt** below.
3. Always restate `template_version` in the output header metadata.
4. Re-runs should create a **new** report file using the collision rules under **Output artifact (required)** (do not silently overwrite prior reports).

---

## Runner prompt (copy/paste)

Use this as the first message in a new job evaluation chat.

```text
You are evaluating Gary Boodhoo for a specific role.

Read and follow:
- @JOB_EVALUATION_TEMPLATE.md
- @JOB_EVALUATION_REFERENCES.md

Job description input:
- (paste JD text here) OR (@path/to/job description file)

Task:
Write the full report to `job-evaluation-reports/` using the Output artifact rules in JOB_EVALUATION_TEMPLATE.md (naming + collisions), and ensure the report uses the exact PART 1–6 headings defined in JOB_EVALUATION_TEMPLATE.md.

Constraints:
- Print header metadata first (inside the written report file), including template_version copied from JOB_EVALUATION_TEMPLATE.md, plus `output_report_path`.
- Populate `portfolio_pages_required`, `portfolio_pages_reviewed`, and ensure `evidence_sources_used` accounts for **all** canonical portfolio URLs in `JOB_EVALUATION_REFERENCES.md` (or marks fetch failures explicitly).
- Be blunt and realistic. No flattery.
- Separate fit on paper vs actual capability.
- Use both resume variants in PART 2 (connect md + games pdf).
- In PART 4, follow **Required diligence** + **PART 4 written output (synthesis only)** in JOB_EVALUATION_TEMPLATE.md (integrated narrative; no per-URL subsections; no cherry-picking which pages you reviewed).
- In PART 3, include at least 2 short quotes total from summaries/dumps (with file paths).
- If sources conflict, call it out.
- End with the two short paragraphs: why hire / why not hire.
```
