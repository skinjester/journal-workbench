# Job evaluation references (canonical)

This file is the **stable input list** for evaluations. It should not contain job-specific text.

If a path moves, update it here and bump `JOB_EVALUATION_TEMPLATE.md`’s `template_version`.

## Resume(s)

Every file listed here is read for **PART 2** (compare). For **PART 5 headline verdicts** and rubric scoring tied to the application package, the evaluator selects **one** `primary_resume_for_verdict` per `JOB_EVALUATION_TEMPLATE.md` (v1.5.0+). Headline tiers are grounded in **that resume + portfolio**—not private journals.

- [`resumes/gboodhoo-resume-connect.md`](resumes/gboodhoo-resume-connect.md)
  - Primary “platform / systems / trust moments” positioning.
- [`resumes/gboodhoo-resume-games.md`](resumes/gboodhoo-resume-games.md)
  - Alternate positioning (more game-forward). Use when evaluating game roles, or when you want the evaluator to sanity-check framing mismatch.
- [`resumes/gboodhoo-resume-31st-union.md`](resumes/gboodhoo-resume-31st-union.md)
  - Role-tuned variant for **Sr UX Designer, 31st Union** (and similar postings); compare explicitly against connect/games in PART 2 when this file is in the list.
- [`resumes/gboodhoo-resume-riot.md`](resumes/gboodhoo-resume-riot.md)
  - Role-tuned variant for **Riot-style** senior game UX / player-experience–forward roles; compare explicitly against connect/games (and other tailored variants) in PART 2 when this file is in the list.
- [`resumes/gboodhoo-resume-11th-hour.md`](resumes/gboodhoo-resume-11th-hour.md)
  - Role-tuned merge (31st-union + Riot sources) for **Eleventh Hour–style** senior game UX: systems, menus, commerce, ARPG/Kestrel, Fireworks **token** line on ESO; compare explicitly against other game variants in PART 2 when this file is in the list.

## Portfolio (public)

Use the live site as the primary craft/proof surface (case studies, artifacts, narrative).

Canonical portfolio pages (deduped). Treat as the mandatory review set **unless** you explicitly add more URLs in chat. The evaluator must **review all of these** for diligence; the written PART 4 in `JOB_EVALUATION_TEMPLATE.md` is a **single synthesized narrative** for the JD (v1.3.0+), not a page-by-page report.

- [`https://www.garyb.design/`](https://www.garyb.design/)
- [`https://www.garyb.design/products/elderscrollsonline`](https://www.garyb.design/products/elderscrollsonline)
- [`https://www.garyb.design/products/madden`](https://www.garyb.design/products/madden)
- [`https://www.garyb.design/products/sims3`](https://www.garyb.design/products/sims3)
- [`https://www.garyb.design/products/starwars`](https://www.garyb.design/products/starwars)
- [`https://www.garyb.design/products/xoholo`](https://www.garyb.design/products/xoholo)
- [`https://www.garyb.design/products/deepdream`](https://www.garyb.design/products/deepdream)
- [`https://www.garyb.design/research/circular-buffer`](https://www.garyb.design/research/circular-buffer)
- [`https://www.garyb.design/research/deepdream-gdc`](https://www.garyb.design/research/deepdream-gdc)
- [`https://www.garyb.design/research/quest-tracker`](https://www.garyb.design/research/quest-tracker)

## Monthly summaries (derived)

These are **second-order evidence** (good for behavioral patterns; weaker as “shipping proof” unless corroborated).

- [`summaries 2026-04/`](summaries%202026-04/)
  - Monthly markdown summaries (broad year coverage in this workspace folder).

## Raw journals (primary-ish evidence)

These are closer to contemporaneous work logs (stronger for “what you actually did,” still not external validation).

- [`journal_summarizer/monthly_dumps/`](journal_summarizer/monthly_dumps/)
  - Raw monthly dump markdown files.

## “Product notes” / long-running threads (optional)

Use selectively. Good for recent building/prototyping thinking; easy to over-weight.

- [`contexts/chatGPT thread-1 MIDI OSC product`](contexts/chatGPT%20thread-1%20MIDI%20OSC%20product)
- [`contexts/chatGPT thread-2 MIDIOSC product`](contexts/chatGPT%20thread-2%20MIDIOSC%20product)

## Job description inputs (pointers only)

Job-specific JD text should be pasted in chat **or** referenced via a workspace file at evaluation time.

- Typical location: [`job descriptions/`](job%20descriptions/)
- Optional processed notes: [`job descriptions-processed/`](job%20descriptions-processed/)

## Evaluation outputs (generated)

Each evaluation run should write a standalone markdown report here:

- [`job-evaluation-reports/`](job-evaluation-reports/)

See [`job-evaluation-reports/README.md`](job-evaluation-reports/README.md) for naming and collision rules.

## Evidence rules (short)

- **Portfolio**: strongest for craft, systems narrative, artifacts, and “what you claim you can do.”
- **Resume**: strongest for role framing, titles, chronology, and scannability.
- **Monthly dumps / summaries**: strongest for patterns, collaboration, decision-making, delivery cadence; always label as journal-derived.
- **Chat threads (`contexts/`)**: strongest for intent and iteration; weakest for org-scale shipping claims unless backed elsewhere.
