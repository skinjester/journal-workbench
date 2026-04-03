# Monthly summaries in Cursor (no external API)

This repo does **not** call OpenAI, Anthropic, or any other paid API. The Python tools only:

- Parse journals or `monthly_dumps/*.md`
- Emit **tagged** draft summaries via rule-based grouping (`summarizer.py --from-dumps`)

For **editorial** synthesis (concise bullets, merged themes, closing paragraph), open a chat in **Cursor** and attach:

1. `monthly_dumps/YYYY-MM.md` for the month you want  
2. This file (or paste the rules below)

## Output file

- Path: `summaries/YYYY-MM.md`
- Sections in order: `Goals`, `Workstream`, `Artifacts Delivered`, `Key Decisions`, `Open Questions / Follow Ups`, `People Involved`, then `---`, then one short closing paragraph in *italics*.

## Closing paragraph style

- Write the final italicized paragraph in plain spoken English, as if explaining the month to another person.
- Keep it grounded in what actually happened that month.
- Prefer 1-2 direct sentences.
- Avoid poetic framing, metaphors, and vague mood-setting language.
- Do not repeat the bullet wording verbatim, but do summarize the main throughline of the month clearly.

## Bullet format

Every bullet under the first five sections must be exactly:

```markdown
- **[TAG]** One complete sentence.
```

**Exception — Artifacts Delivered:** use the project **[TAG]** plus one `` `deliv:…` `` slug (see below), then the sentence.

Use **only** these `TAG` values (verbatim):

`ESO`, `ESO-Platform`, `ESO-Studio Site`, `KESTREL`, `OPS`, `Portfolio`, `Project Ansible`, `skinjestercorp`, `Image Garden`, `deepdreamvisionquest`, `xoholo`, `iveda`, `RPVR`

### Tagging rules (short)

- **ESO** — shipped game client (all platforms). In-game Crown Store → **ESO**.
- **ESO-Platform** — elderscrollsonline.com, marketing/CMS web. Web Crown / purchase surfaces → **ESO-Platform**.
- **ESO-Studio Site** — studio / recruiting site.
- **KESTREL** — Kestrel program (HUD, quest, inventory/NAV, Kestrel delivery), not generic live ESO UI unless clearly Kestrel.
- **Portfolio** — portfolio, antimeme, `His Portfolio` / `profile` / `skinjester.com work` / `garyboodhooworld`.
- **OPS** — personal infra (NAS, keyboards, network, workstations).
- **Project Ansible** — Ansible rack / studio rack project.
- **skinjestercorp** — business admin for that entity.
- **Image Garden** — workshop series, syllabus, participant flows.
- **deepdreamvisionquest** — live installation / neural pipeline; logs under filename `spirit animal` that are *not* workshop-focused → here or **Image Garden** by content.
- **xoholo** — includes work formerly logged as `futureworld` or `cinechamber`.
- **iveda** — Iveda product design.
- **RPVR** — RedPill VR.

Do **not** emit tags: `spirit animal`, `His Portfolio`, `profile`, `ESO-PC`, `ESO-Console`, `futureworld`, `cinechamber`.

`People Involved` may list names or `None identified` (no **[TAG]** on those lines).

## Artifacts Delivered — deliverable tags (`deliv:*`)

Each bullet in **Artifacts Delivered** uses the project **[TAG]** above, then **exactly one** deliverable tag in backticks (orthogonal to project tags), then the sentence:

```markdown
- **[ESO-Platform]** `deliv:documentation` Confluence hub for Buy Now with export timestamps.
```

Use **only** these deliverable slugs (verbatim):

| Slug | Use for |
|------|---------|
| `deliv:audit` | Audits, comparisons, capture-based reviews, surveys |
| `deliv:documentation` | Written specs, Confluence, diagrams-as-spec, matrices, JIRA writeups, copy-as-deliverable, handoff notes |
| `deliv:design-system` | Styleguides, UI kits, reusable pattern libraries |
| `deliv:visuals` | Stills and motion outputs that are not interactive prototypes (wireframes, comps, exports, AE/renders/GIFs, compositor output) |
| `deliv:prototype` | Interactive web or engine builds (Axure, HTML demos, CMS staging, Unreal/HTML5, runnable drops) |
| `deliv:presentation` | Deck-first deliverables (PowerPoint, Keynote, show-and-tell) |
| `deliv:operations` | Invoices, DNS, backups, rack, domains, hardware logs, migrations |

If a line mixes artifact types, pick the **primary** deliverable or split into two bullets. Do **not** emit a second `deliv:*` on the same line.

Heuristic tagging for bulk updates lives in `scripts/tag_artifacts_deliv.py`.

---

Ask Cursor: *Synthesize this dump into `summaries/YYYY-MM.md` following the rules above, and make the closing paragraph plain spoken and direct.*
