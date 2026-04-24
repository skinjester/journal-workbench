# Job evaluation template (canonical)

`template_version`: **v1.14.3**  
`last_updated`: **2026-04-23**

## Changelog

- **v1.14.3 (2026-04-23)**: **References: 11th Hour–tuned resume.** `JOB_EVALUATION_REFERENCES.md` now lists `resumes/gboodhoo-resume-11th-hour.md`; PART 2 / `primary_resume_for_verdict` behavior is unchanged.
- **v1.14.2 (2026-04-22)**: **References: Riot-tuned resume.** `JOB_EVALUATION_REFERENCES.md` now lists `resumes/gboodhoo-resume-riot.md` alongside other variants; PART 2 / `primary_resume_for_verdict` behavior is unchanged.
- **v1.14.1 (2026-04-21)**: **Resume list from references.** PART 2 evaluates every repo-relative resume path under `JOB_EVALUATION_REFERENCES.md` → **Resume(s)** (not a fixed pair). `primary_resume_for_verdict` must be **one of those paths**. Optional tailored resumes (e.g. studio-specific) live in the same section.
- **v1.14.0 (2026-04-20)**: **Imperative cleanup.** Removed redundant restatements of core rules (journals do not inflate PART 5 tiers; submittable package = primary resume + portfolio; signal strength is not interview odds; balanced specificity; mitigation pairing; Risk Factors is not permission for bleak prose) — each rule now has one canonical location. Added **symmetric scoring notes** on Problem Match, Relevant Proof, and Narrative Coherence so High requires direct evidence (previously only Risk Factors had a tier-moderation note). Made **mitigation pairing conditional** on visible evidence. Added a **PART 5 ↔ PART 6 self-check**. Added a neutral **"hold"** option to the direct recommendation list. Updated sample rubric to demonstrate the seven-step scale. Compressed changelog and shrank the runner prompt.
- **v1.13.0 (2026-04-20)**: Canonical seven-step ordinals with ASCII hyphens. See PART 5 ordinal tiers note.
- **v1.12.0 (2026-04-20)**: Header metadata adds `model_used`.
- **v1.11.0 (2026-04-20)**: Optional seven-step ordinal scale for PART 5 / PART 6 (superseded by v1.13.0 vocabulary).
- **v1.10.0 (2026-04-20)**: Machine-readable `#### Rubric` subsection required in PART 6 for collation.
- **v1.9.0 (2026-04-20)**: Rename last two PART 5 verdict lines to `Signal strength: Recruiter` / `Signal strength: HM`.
- **v1.8.0 (2026-04-20)**: Balanced risk tone — see "Risk acknowledgment vs risk overweighting."
- **v1.7.0 (2026-04-19)**: Add `Narrative coherence (for this JD)` as fifth PART 5 headline.
- **v1.6.0 (2026-04-19)**: Remove `Likelihood of panel loop survival` from PART 5 headlines.
- **v1.5.0 (2026-04-18)**: Select a primary resume after PART 2; PART 5 tiers grounded in that resume + portfolio only.
- **v1.4.0 (2026-04-16)**: Scanability defaults for report writing; fix stale `.pdf` references.
- **v1.3.1 (2026-04-15)**: Canonical games resume path updated to `.md`.
- **v1.3.0 (2026-04-15)**: PART 4 is one synthesized portfolio narrative; no per-URL subsections.
- **v1.2.0 (2026-04-15)**: Every canonical portfolio URL must be reviewed.
- **v1.1.0 (2026-04-15)**: Persist reports under `job-evaluation-reports/` with `.eval.md` naming.
- **v1.0.0 (2026-04-16)**: Initial canonical template + references split.

## What this file is for

This is the **instruction spec** for evaluating a candidate (you) against a job description using:

- **direct, evidence-bound hiring realism** (honest constraints; not catastrophizing)
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

- Be **direct and realistic**. No flattery. No “you got this” pep talk. **Direct ≠ doom:** do not maximize fear, stack the same downside in every PART, or use maximal negative prose when the evidence only supports a narrower concern.
- **Direct realism cuts both ways:** refuse High when proof is adjacent, dated, or inferred. A generous default is as much a failure as a harsh default.
- Separate **fit on paper** from **verifiable capability from submittable materials**. Journal depth belongs in PART 3 / PART 6 tuning (see PART 3 purpose boundary).
- If sources conflict, say so explicitly (what contradicts what, and why it matters).
- If something is ambiguous, state the **assumption** you are making.
- Do not rewrite the resume or portfolio unless explicitly asked.

### Risk acknowledgment vs risk overweighting

- **Acknowledge** risks that resume/portfolio plausibly raise for a skeptical screener; do **not inflate** them beyond what those materials support, and do not treat JD copy as infallible truth—especially in **games/AAA**, where postings often mix **must-haves**, **nice-to-haves**, and boilerplate. **Flag assumptions** when inferring how strict a line is.
- **Mitigation pairing is conditional.** When the primary resume or portfolio **names** a direct mitigation (clear adjacent proof, credible scope match, strong anchor project), say so in the same breath or the next sentence. When no mitigation is visible in submittable materials, **leave the concern bare**—do not manufacture a softener.
- Avoid **repetitive downside stacking** across PART 1 / 4 / 5 / 6 that restates the same fear with different wording.
- Keep **comparable depth** between reasons to advance and screening concerns: do not write three thin positives and three dense, specific negatives.

## Writing style defaults (important)

The report should be easy to scan quickly by a tired human reader.

Defaults:

- Prefer **short paragraphs** over long dense blocks.
- Use **real subheadings** inside each PART when they improve scanability.
- Turn repeated evaluative labels into **bullets with bold labels** or `####` subheads.
- In dense sections, start with a **one-line takeaway** when helpful.
- Use bullets for lists of strengths, risks, gaps, and recommendations.
- Keep the tone **direct and readable**, not sycophantic; keep the formatting clean and readable.
- Do **not** pad the report with filler transitions or repetitive restatement.

## Evidence quality ladder (how much weight to give)

### For PART 5 headline verdicts and collated overview scoring

Use **only** what employers can see from an application: **primary resume + portfolio URLs** (see PART 5 scoring basis and PART 3 purpose boundary for how journals relate).

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
- `model_used`: (which AI model produced this report—e.g. product + model name as shown in the chat UI, or `unknown` if not tracked)
- `job`: (company + title if known)
- `jd_source`: (pasted text vs `@path/to/file`)
- `output_report_path`: (repo-relative path of the markdown file you wrote)
- `resume_versions_evaluated`: (list every resume path under **Resume(s)** in `JOB_EVALUATION_REFERENCES.md` that you evaluated in PART 2)
- `primary_resume_for_verdict`: (single repo-relative path—the resume selected in PART 2 as authoritative for PART 5–6 headline scoring; must be one of the paths in `resume_versions_evaluated`)
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

### PART 2 — Resume evaluation only (multi-pass)

Evaluate **each** resume variant independently (every repo-relative `.md` path listed under **Resume(s)** in [`JOB_EVALUATION_REFERENCES.md`](JOB_EVALUATION_REFERENCES.md); reproduce that list as linked bullets here):

For each resume, include:

- interview likelihood **from that resume alone** (High/Medium/Low) + 1–3 sentences why
- strongest signals
- weakest / missing signals
- vague/passive/dated language (call it out)
- what archetype you read as (IC/lead/manager/systems/strategist/specialist)
- whether a recruiter can bucket you quickly (yes/no + what bucket)

Then add a **comparative** subsection:

- which listed resume is closest to *this JD* (short rationale)
- whether any other listed resume is redundant for this application or still worth keeping in rotation

Then add **`#### Primary resume for PART 5–6 (authoritative)`** (required):

- Set **`primary_resume_for_verdict`** to exactly one path from the **Resume(s)** list in `JOB_EVALUATION_REFERENCES.md` (the same set you evaluated above).
- **Selection rules** (apply in order; state which step decided it):
  1. Prefer the resume **closer to this JD** (from the comparative subsection above).
  2. If still tied, prefer the higher **Interview likelihood from this resume alone** (High beats Medium beats Low).
  3. If still tied, state the tie-break in one explicit sentence (no silent pick).
- One short line: this choice is the **application-facing** resume for headline scoring in PART 5–6; non-primary resume(s) remain in PART 2 for comparison only.

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

The body of PART 4 is **one coherent hiring-manager view of what the portfolio proves for this JD**. Do **not** write per-URL blocks or repeated "proves / does not prove" grids.

Use **only** these subheadings inside PART 4 (in this order):

1. `#### What the portfolio proves for this JD` — integrated narrative; name case-study URLs inline where they carry the argument.
2. `#### What the portfolio does not prove (or only weakly supports) for this JD` — gaps vs the JD's explicit / desired lines.
3. `#### Hiring risks the portfolio reduces vs leaves open` — short, decisive bullets tied to *this* role.
4. `#### Credibility and receipts` (optional, keep short) — separate **marketing** from **demonstrated** proof.

Optional appendix (only if useful, max ~15 lines):

- `#### Portfolio coverage (audit)` — a **single compact table**: one row per required portfolio URL, columns `URL | Status (Reviewed / Failed to fetch) | Note (≤12 words)`. No prose per row beyond the Note cell.

Fetch failures / blocked pages:

- Mark **Failed to fetch** in `portfolio_pages_reviewed` and in the optional audit table. Say what you could not verify in **Credibility and receipts** or **What the portfolio does not prove**, not in a per-page essay.

### PART 5 — Combined verdict

**Scoring basis:** The **five** verdict lines below are the **headline tiers** used for overview/collate. They are **comparative fit diagnostics** across jobs — **not** predictions of interviews, screens, or offers. They must reflect **only the submittable application package**: **`primary_resume_for_verdict` + portfolio**. Journals do not raise these tiers (see PART 3 purpose boundary).

**Ordinal tiers:** Use either **High / Medium / Low** or the seven-step scale (weakest → strongest): **very low**, **low**, **medium-low**, **medium**, **medium-high**, **high**, **very high**. Use **ASCII hyphens** in `medium-high` / `medium-low`.

Before the five bullets, add a short intro paragraph stating: (a) which resume is primary, (b) that headline verdicts are resume+portfolio-grounded, (c) that extra depth from journals appears in PART 3 / PART 6 tuning, not as a parallel score.

**Definitions:**

- **Fit on paper:** JD match from the primary resume's first-pass read.
- **Actual capability (inferred):** capability verifiable from primary resume + portfolio (not from private logs).
- **Narrative coherence (for this JD):** whether the package tells one coherent application story for this JD, not a scattershot set of proofs.
- **Signal strength: Recruiter:** how strong the JD fit signal is on a recruiter-style read (keywords, bucket, obvious relevance, red flags).
- **Signal strength: HM:** how strong the JD fit signal is on a hiring-manager-style read (depth of proof, seniority/scope match, story credibility).

(Do **not** add a separate "panel loop survival" headline — too process-dependent to score from materials alone.)

Deliver **exactly one** line per dimension using these labels (so downstream collation can parse):

- Fit on paper: \<tier\>
- Actual capability (inferred): \<tier\>
- Narrative coherence (for this JD): \<tier\>
- Signal strength: Recruiter: \<tier\>
- Signal strength: HM: \<tier\>

Use this markdown shape (bold the full label so the colon before the tier is unambiguous):

- `- **Signal strength: Recruiter**: High`
- `- **Signal strength: HM**: Medium-High`

Do **not** duplicate the five verdict labels for the non-primary resume. Optional: `#### Non-primary resume (reference only)` in prose without repeating `**Fit on paper:**` etc.

Then use these **three** subsections (exact `####` headings):

- `#### 3 strongest reasons to advance` — concrete, JD-specific strengths grounded in primary resume + portfolio.
- `#### 3 main screening concerns or gaps` — what a skeptical recruiter/HM might fixate on. (See "Risk acknowledgment vs risk overweighting" for how to handle mitigations.)
- `#### Misleveling / mispositioning read` — overleveled, underleveled, too game-specific, too IC, too diffuse, etc.

Formatting preference: keep advance and concern subsections **balanced in specificity and length**.

#### PART 5 ↔ PART 6 self-check (required before finalizing)

Before writing the final report, verify the five headline tiers are consistent with the PART 6 rubric you are about to score:

- If **Problem Match**, **Relevant Proof**, **Role Readability**, or **Narrative Coherence** (rubric) lands at **Medium** or lower, the corresponding PART 5 headline(s) **cannot exceed Medium-High**. Reconcile by either adjusting the tier down or adding one sentence in PART 5 prose that explains why the headline can stay higher despite the rubric cell (e.g. the rubric penalty is about recency, not fit).
- If **Risk Factors** lands at **High** (material hiring risk), **Signal strength: HM** cannot exceed **Medium-High**. Reconcile the same way.
- If you cannot reconcile, downgrade the headline. Prose overrides are the exception, not the default.

### PART 6 — Rubric scoring + weighted synthesis

Score each dimension using **High / Medium / Low** or the seven-step scale (see PART 5 ordinal note). Rubric cells reflect the submittable package; journal evidence belongs in **Actionable output**, not in these cells.

Finally:

- **Actionable output** (tight): themes to emphasize, themes to de-emphasize, **up to 5** bullets to rewrite, **up to 3** missing signals to make explicit, **up to 5** interview stories to prepare, and a **direct** recommendation (pick one; avoid melodrama):
  - apply as-is
  - apply after targeted resume edits
  - apply, but odds are low
  - **hold — watch for better-fit postings in the same track** (use when the package is strong but this JD specifically asks for capabilities the package does not prove)
  - do not pursue

End with:

- **Why they might hire you** (1 short paragraph)
- **Why they might not** (1 short paragraph)

Formatting preference:

- Prefer a `#### Weighted synthesis` subhead followed by concise question-and-answer bullets.
- Prefer a `#### Actionable output` subhead.
- Under `Actionable output`, prefer short subheads for themes to emphasize, themes to de-emphasize, bullets to rewrite, missing signals, interview stories, and direct recommendation.

**Collation (required):** Include a `#### Rubric` subsection **before** `#### Weighted synthesis` with **exactly one bullet per row**, in this order, using these **bold label prefixes** (percentages optional but recommended). The **seventh** row must use **Narrative Coherence (5%)** as the label (collated charts show it as **Narrative Coherence (rubric)** to distinguish it from PART 5 narrative coherence). **ATS / recruiter hygiene** must be **Pass** or **Fail** only.

Sample shape (values illustrative — mix of three-step and seven-step tiers demonstrates both scales are accepted):

```text
#### Rubric

- **Problem Match (25%):** High
- **Relevant Proof (20%):** Medium-High
- **Recency (15%):** Medium
- **Role Readability (15%):** High
- **Differentiation (10%):** Medium-High
- **Risk Factors (10%):** Medium
- **Narrative Coherence (5%):** High
- **ATS / recruiter hygiene:** Pass
```

## Rubric (score each High / Medium / Low, or use the seven-step scale)

### 1) Problem Match (25%)

Does the background solve the JD's real pains (not the buzzwords)?

**Scoring note:** **High** means the JD's core asks are named directly on primary resume or portfolio in current, submittable form. If the match is **adjacent** (related domain, related scale, related tools) or **inferred** (supported by journal detail but not visible on the page), cap this cell at **Medium**. If a JD-named required ask is absent from the evaluated resume set and portfolio, cap at **Medium-Low**.

### 2) Relevant Proof (20%)

Shipped / clarified / changed outcomes with credible receipts **on the primary resume and/or portfolio**. Journals may list additional work to surface publicly later; they do not substitute for missing resume/portfolio proof in this cell.

**Scoring note:** **High** requires direct, unambiguous, date-appropriate receipts on resume or portfolio. If the strongest proof is **older than typical recency expectations for this role**, or is **adjacent to** (not directly named as) the JD's asks, cap at **Medium-High**. Bare claims without portfolio backing cap at **Medium**.

### 3) Recency (15%)

Is the strongest proof recent enough for the role's expectations?

### 4) Role Readability (15%)

Can a recruiter/HM bucket you correctly fast?

### 5) Differentiation (10%)

Why you vs an obvious generic candidate from the target domain?

### 6) Risk Factors (10%)

What would make a HM hesitate (gaps, adjacency, credibility holes)?

**Scoring note:** **High / Medium / Low** here describes **relative material risk** among rubric cells — not permission for maximal negative prose. A **High** score means "meaningful hiring risk on evidence," not "write the bleakest possible paragraph." Keep the cell's language **proportional** to the tier.

### 7) Narrative Coherence (5%)

Do **primary resume + portfolio** read as one internally consistent application — headings, section ordering, claim/proof alignment, no contradictions between summary and work history? (This scores the **local consistency** of the submittable story. The PART 5 headline `Narrative coherence (for this JD)` scores the broader question of whether the whole package reads as one candidate for **this specific JD**. The two can diverge: a well-ordered resume can still be the wrong resume for a particular posting.)

### 8) ATS / recruiter hygiene (pass/fail)

Pass/fail only: headings, scanability, keyword sanity (not stuffing), parse risk.

## Weighted synthesis guidance

After scoring, explicitly answer:

- **What problem is this job hiring for?**
- **Where does resume + portfolio show you solving that problem?**
- **Does the primary resume make that obvious in the first 20 seconds?**
- **What would make someone hesitate** based only on resume + portfolio?
- **What already mitigates those hesitations?** (See "Risk acknowledgment vs risk overweighting" — mitigation pairing is conditional on visible evidence. If nothing in the submittable materials addresses a hesitation, say so; do not invent a softener.)
- **Does the submittable story hang together?**

## Re-run workflow (when this template changes)

1. Bump `template_version` + add a changelog entry at the top of this file.
2. Re-run evaluations by starting a fresh chat (or fork) and pasting the **Runner prompt** below.
3. Always restate `template_version` and `model_used` in the output header metadata.
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
Write the full report to `job-evaluation-reports/` using the rules defined in JOB_EVALUATION_TEMPLATE.md (Header metadata first, then PART 1–6 with the exact headings and subheadings, then the `#### Rubric` block, then Weighted synthesis and Actionable output). Follow the Output artifact naming + collision rules. Honor "Operating mode (tone + ethics)" and "Risk acknowledgment vs risk overweighting"; complete the PART 5 ↔ PART 6 self-check before finalizing.

Confirm the written file path in chat; do not paste the full report unless asked.
```
