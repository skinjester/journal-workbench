# Job evaluation template (canonical)

`template_version`: **v1.7.0**  
`last_updated`: **2026-04-19**

## Changelog

- **v1.7.0 (2026-04-19)**: Add **Narrative coherence (for this JD)** as the fifth PART 5 headline verdict—whether **primary resume + portfolio** tell one coherent application story for this posting (distinct from fit-on-paper match and from proof depth). Collated overview/charts use **five** verdict columns. HTML dashboards use a **wider chart encoding** of ordinals plus an optional **within-batch rank** view for comparing roles in one overview.
- **v1.6.0 (2026-04-19)**: Remove **Likelihood of panel loop survival** from PART 5 headline verdicts. It is too process-dependent and speculative to score from resume/portfolio/JD; interview-loop nuance belongs in PART 6 **Actionable output** if useful. Collated overview now uses **four** verdict columns.
- **v1.5.0 (2026-04-18)**: After PART 2, select a **primary resume** for PART 5–6. **Headline verdict tiers (PART 5) and rubric scores tied to “the application package”** must be derived from **that primary resume + portfolio only**—what a candidate submits. Journals/summaries (PART 3) inform **resume/portfolio tuning** and honesty; they **must not** upgrade PART 5 headline tiers unless the same claim is supportable from resume+portfolio. Redefine PART 5 **Actual capability (inferred)** as capability **verifiable from primary resume + portfolio**, not private logs.
- **v1.4.0 (2026-04-16)**: Add scanability defaults for report writing, require clearer internal substructure in dense sections, and fix stale `resumes/gboodhoo-resume-games.pdf` references to `resumes/gboodhoo-resume-games.md`.
- **v1.3.1 (2026-04-15)**: Update canonical games resume reference from `resumes/gboodhoo-resume-games.pdf` to `resumes/gboodhoo-resume-games.md`.
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
- Separate **fit on paper** from **verifiable capability from submittable materials** (primary resume + portfolio). Journals may show more than the page shows—call that out in PART 3 / PART 6 tuning, not as hidden upgrades to PART 5 headline tiers.
- If sources conflict, say so explicitly (what contradicts what, and why it matters).
- If something is ambiguous, state the **assumption** you are making.
- Do not rewrite the resume or portfolio unless explicitly asked.
- When citing journal/summary evidence, prefer **short quotes** and always label the source file path.

## Writing style defaults (important)

The report should be easy to scan quickly by a tired human reader.

Defaults:

- Prefer **short paragraphs** over long dense blocks.
- Use **real subheadings** inside each PART when they improve scanability.
- Turn repeated evaluative labels into **bullets with bold labels** or `####` subheads.
- In dense sections, start with a **one-line takeaway** when helpful.
- Use bullets for lists of strengths, risks, gaps, and recommendations.
- Keep the tone blunt, but keep the formatting clean and readable.
- Do **not** pad the report with filler transitions or repetitive restatement.

## Evidence quality ladder (how much weight to give)

### For PART 5 headline verdicts and collated overview scoring

Use **only** what employers can see from an application: **primary resume** (see PART 2) **+ portfolio URLs** in `JOB_EVALUATION_REFERENCES.md`. Do not let private journal detail **raise** those headline tiers unless the same proof appears on resume or portfolio.

### For narrative depth, patterns, and resume/portfolio fine-tuning (PART 3, PART 6 actionable output)

1. **Public portfolio artifacts** (strong for craft, interaction/system thinking, narrative clarity)
2. **Resume** (strong for how a screener will bucket you in 15–30 seconds)
3. **Raw monthly dumps** (strong for “what actually happened,” still self-authored)
4. **Monthly summaries** (useful patterns; second-order; can miss nuance)
5. **Long chat transcripts in `contexts/`** (good for intent/prototyping; weak for org-scale outcomes unless corroborated)

## Output format (always use these headings)

### Global formatting expectations

Keep the required PART 1-6 headings exactly as written below. Within those parts, you may add short subheadings and bullets to improve readability, but do not add extra top-level PART sections or convert the report into a giant wall of prose.

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
- `resume_versions_evaluated`: (list both `resumes/gboodhoo-resume-connect.md` and `resumes/gboodhoo-resume-games.md` when evaluated in PART 2)
- `primary_resume_for_verdict`: (single repo-relative path—the resume selected in PART 2 as authoritative for PART 5–6 headline scoring; must be one of the two resume paths above)
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

Preferred internal structure for readability:

- `#### The explicit asks`
- `#### The implied asks`
- `#### What "great" looks like for this role`
- `#### What a hiring team is optimizing for in screening`
- `#### Likely doubts unless proven otherwise`

### PART 2 — Resume evaluation only (two-pass)

Evaluate **each** resume variant independently:

- [`resumes/gboodhoo-resume-connect.md`](resumes/gboodhoo-resume-connect.md)
- [`resumes/gboodhoo-resume-games.md`](resumes/gboodhoo-resume-games.md)

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

Then add **`#### Primary resume for PART 5–6 (authoritative)`** (required):

- Set **`primary_resume_for_verdict`** to exactly one path: `resumes/gboodhoo-resume-connect.md` **or** `resumes/gboodhoo-resume-games.md`.
- **Selection rules** (apply in order; state which step decided it):
  1. Prefer the resume **closer to this JD** (from the comparative subsection above).
  2. If still tied, prefer the higher **Interview likelihood from this resume alone** (High beats Medium beats Low).
  3. If still tied, state the tie-break in one explicit sentence (no silent pick).
- One short line: this choice is the **application-facing** resume for headline scoring in PART 5–6; the other resume remains in PART 2 for comparison only.

Formatting preference:

- For each resume block, prefer bold lead labels such as `**Interview likelihood from this resume alone:**`, `**Strongest signals:**`, `**Weakest / missing signals:**`, and so on, instead of burying everything in plain text.

### PART 3 — Monthly summaries + raw journals (supporting evidence)

**Purpose boundary:** PART 3 supports **alignment with the JD**, behavioral honesty, and **resume/portfolio fine-tuning** (what to add, cite, or surface publicly). It is **not** an alternate scoring track: do **not** use journal strength to justify higher PART 5 headline tiers unless the same claim is supportable from **primary resume + portfolio**.

Goal: show what you *actually did* beyond resume marketing, and what is **under-visible** until you update the resume or site.

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
- Prefer subheads such as `#### Behavioral patterns`, `#### Leadership and influence evidence`, `#### Direct ambiguity-navigation evidence`, `#### Evidence that strengthens the resume`, `#### Evidence that weakens or complicates the resume story`, and `#### Net read from journals`.

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

**Scoring basis:** The **five** verdict lines below are the **headline tiers** used for overview/collate. They must reflect **only the submittable application package**: **`primary_resume_for_verdict` + portfolio** (public case studies and proof on the site). **PART 3 journals/summaries do not increase these tiers** unless the same capability is **verifiable** from resume or portfolio (e.g. named shipped work on the resume, demos on the site).

Before the five bullets, add a short intro paragraph stating: (a) which resume is primary, (b) that headline verdicts are **resume+portfolio-grounded**, (c) that extra depth from journals appears in PART 3 / PART 6 tuning, not as a parallel “hidden” score.

**Definitions:**

- **Fit on paper:** High/Medium/Low for **`primary_resume_for_verdict` only** (the non-primary resume stays in PART 2 only—do **not** emit a second `Fit on paper` line for it).
- **Actual capability (inferred):** High/Medium/Low for capability **inferred from primary resume + portfolio evidence employers can verify**—not “stronger in private logs than on the page.” If journals suggest more than public materials show, say that under PART 3 / **Credibility gap** style notes in PART 6, not as inflating this line.
- **Narrative coherence (for this JD):** High/Medium/Low for whether **primary resume + portfolio** present **one coherent application story for this specific JD**—not scattershot proof or a story that fits a different role better. (Related to rubric **Narrative Coherence**; this headline is the verdict-tier summary for the package-as-story.)
- **Recruiter / HM screen likelihoods:** As a hiring team would read you from **resume + portfolio**, not from journals they never receive. (Do **not** add a separate “panel loop survival” headline—process varies too much to score from materials alone; if useful, discuss onsite/panel/design-test risk briefly under PART 6 **Actionable output** or **mispositioning**.)

Deliver **exactly one** line per dimension using these labels (so downstream collation can parse):

- Fit on paper: High/Medium/Low
- Actual capability (inferred): High/Medium/Low
- Narrative coherence (for this JD): High/Medium/Low
- Likelihood of recruiter screen: High/Medium/Low
- Likelihood of hiring manager screen: High/Medium/Low

Do **not** duplicate the five verdict labels for the non-primary resume. Optional: `#### Non-primary resume (reference only)` in prose without repeating `**Fit on paper:**` etc.

Then:

- 3 strongest reasons to advance
- 3 strongest reasons to reject
- misleveling / mispositioning read (overleveled, underleveled, too game-specific, too IC, too diffuse, etc.)

Formatting preference:

- Use subheads for these three blocks so the verdict is easy to skim.

### PART 6 — Rubric scoring + weighted synthesis

Score each dimension **High/Medium/Low** using the rubric below. **Base rubric cells on primary resume + portfolio** for anything about proof, coherence of the *application story*, and role readability. Use PART 3 journal evidence in **Actionable output** (what to add to resume/site, stories to prepare) and in narrative notes—not to inflate rubric scores beyond what resume+portfolio support.

Finally:

- **Actionable output** (tight): themes to emphasize, themes to de-emphasize, 5 bullets to rewrite, 3 missing signals to make explicit, 5 interview stories to prepare (pull from **portfolio + journals** for *preparation*; journals inform **tuning**, not headline PART 5 tiers), and a blunt recommendation:
  - apply as-is
  - apply after targeted resume edits
  - apply, but odds are low
  - do not pursue

End with:

- **Why they might hire you** (1 short paragraph)
- **Why they might not** (1 short paragraph)

Formatting preference:

- Prefer a `#### Weighted synthesis` subhead followed by concise question-and-answer bullets.
- Prefer a `#### Actionable output` subhead.
- Under `Actionable output`, prefer short subheads for themes to emphasize, themes to de-emphasize, bullets to rewrite, missing signals, interview stories, and blunt recommendation.

## Rubric (score each High / Medium / Low)

### 1) Problem Match (25%)

Does the background solve the JD’s real pains (not the buzzwords)?

### 2) Relevant Proof (20%)

Shipped/clarified/changed outcomes with credible receipts **on the primary resume and/or portfolio**. Journals may list additional work to **surface publicly** later; they do not substitute for missing resume/portfolio proof in this cell.

### 3) Recency (15%)

Is the strongest proof recent enough for the role’s expectations?

### 4) Role Readability (15%)

Can a recruiter/HM bucket you correctly fast?

### 5) Differentiation (10%)

Why you vs an obvious generic candidate from the target domain?

### 6) Risk Factors (10%)

What would make a HM hesitate (gaps, adjacency, credibility holes)?

### 7) Narrative Coherence (5%)

Do **primary resume + portfolio** tell one coherent application story for this JD? (You may note journal-vs-public gaps in PART 3 / Actionable output—this cell scores the **submittable** story.)

### 8) ATS / recruiter hygiene (pass/fail)

Pass/fail only: headings, scanability, keyword sanity (not stuffing), parse risk.

## Weighted synthesis guidance

After scoring, explicitly answer:

- **What problem is this job hiring for?**
- **Where does resume + portfolio show you solving that problem** (employer-visible proof)?
- **Does the primary resume make that obvious in the first 20 seconds?**
- **What would make someone hesitate** based only on resume + portfolio?
- **Does the submittable story hang together?** (If journals add nuance, put under tuning/actions, not as a second “true” score.)

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
- Print header metadata first (inside the written report file), including template_version copied from JOB_EVALUATION_TEMPLATE.md, plus `output_report_path`, `resume_versions_evaluated`, and **`primary_resume_for_verdict`**.
- Populate `portfolio_pages_required`, `portfolio_pages_reviewed`, and ensure `evidence_sources_used` accounts for **all** canonical portfolio URLs in `JOB_EVALUATION_REFERENCES.md` (or marks fetch failures explicitly).
- Be blunt and realistic. No flattery.
- Use both resume variants in PART 2 (connect md + games md); then select **`primary_resume_for_verdict`** per PART 2 rules.
- PART 5 headline verdict lines (**five** bullets, including **Narrative coherence (for this JD)**) must be grounded in **primary resume + portfolio only**; PART 3 journals inform tuning, not tier inflation. See PART 5 definitions for **Actual capability (inferred)** and **Narrative coherence (for this JD)**.
- In PART 4, follow **Required diligence** + **PART 4 written output (synthesis only)** in JOB_EVALUATION_TEMPLATE.md (integrated narrative; no per-URL subsections; no cherry-picking which pages you reviewed).
- In PART 3, include at least 2 short quotes total from summaries/dumps (with file paths); keep PART 3 in the “tuning / honesty” lane per template.
- If sources conflict, call it out.
- End with the two short paragraphs: why hire / why not hire.
- Prefer readable internal formatting: short paragraphs, bullets where natural, and subheads inside dense sections.
```
