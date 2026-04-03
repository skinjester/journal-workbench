# Example: Using the Journal Summarizer

This example demonstrates the complete workflow of using the journal summarizer.

## Sample Run: Generating 2024 Summaries

```bash
$ cd journal_summarizer
$ source venv/bin/activate
$ python3 summarizer.py --year 2024

Journal Summarizer
==================================================
✓ Loaded configuration from config.yaml
✓ Initialized components

Parsing journal files...
Found 30 journal files to process
Parsing OPS journal.md...
  Found 44 entries
Parsing His Portfolio.md...
  Found 282 entries
Parsing skinjestercorp journal.md...
  Found 26 entries
...
✓ Found 12542 total entries
✓ Grouped into 118 months

Month Overview:
  May 2024: 2 entries from 1 projects
  July 2024: 3 entries from 1 projects
  August 2024: 1 entries from 1 projects

Generating monthly reports...

Generating report for May 2024...
  Processing 2 entries...
Categorizing batch 1 (2 entries)...
  Report saved to: summaries/summary-2024-05.md

Generating report for July 2024...
  Processing 3 entries...
Categorizing batch 1 (3 entries)...
  Report saved to: summaries/summary-2024-07.md

Generating report for August 2024...
  Processing 1 entries...
Categorizing batch 1 (1 entries)...
  Report saved to: summaries/summary-2024-08.md

✓ Successfully generated 3 reports

Generated reports:
  - summaries/summary-2024-05.md
  - summaries/summary-2024-07.md
  - summaries/summary-2024-08.md
```

## Generated Report Example

**File:** `summaries/summary-2024-05.md`

```markdown
# Monthly Summary: May 2024
**Generated:** 2026-04-01
**Entries:** 2 from 1 projects
**Projects:** skinjestercorp

### Goals


### Workstream

- **[2024-05-17 11:36]** *(skinjestercorp)* I'm following up on the tax voucher I paid in April, maybe around 2024-04-22

### Artifacts Delivered


### Coverage


### Key Decisions


### Collaboration and Inputs


### Open Questions / Follow Ups

- **[2024-05-18 04:13]** *(skinjestercorp)* I'm not seeing a record of that payment. Did I simply not submit it after all?

### People Involved

```

## Statistics from Real Data

Testing with the actual journal collection:

- **Total entries found:** 12,542 entries
- **Time span:** 2013-2026 (118 months)
- **Projects identified:** 
  - eso (game development journal)
  - deepdreamvisionquest (AI/ML project)
  - His Portfolio (portfolio work)
  - garyboodhooworld (personal site)
  - OPS (operations/infrastructure)
  - skinjestercorp (business)
  - spirit animal
  - xoholo
  - And more...

- **Largest months:**
  - February 2018: 515 entries from 3 projects
  - May 2018: 388 entries from 3 projects
  - January 2018: 355 entries from 3 projects

## Advanced Examples

### Generate summaries for a specific quarter
```bash
python3 summarizer.py --from 2021-01 --to 2021-03
```

### Preview statistics before generating
```bash
python3 summarizer.py --all --dry-run
```

### Generate for recent activity
```bash
python3 summarizer.py --year 2024
```

## What Gets Categorized Where

Based on testing with real journal data:

**Goals:**
- Entries mentioning plans, objectives, "need to", "want to", "will"
- Example: "I need to setup video input to the container"

**Workstream:**
- Active development work, implementations, building
- Example: "working on tooltip layout update"

**Artifacts Delivered:**
- Completed tasks, finished work, deliverables with ✅
- Example: "completed first pass of planning"

**Coverage:**
- Testing, QA, bugs, fixes, crashes
- Example: "crashed. unable to recover"

**Key Decisions:**
- Architecture choices, decisions made, approaches chosen
- Example: "decided against creating wireframe"

**Collaboration and Inputs:**
- Mentions of speaking with people, meetings, discussions
- Example: "Spoke with James Wells from IT"

**Open Questions / Follow Ups:**
- Questions, blockers, unknowns, things to figure out
- Example: "I'm not seeing a record of that payment?"

**People Involved:**
- Auto-extracted from all entries where people are mentioned
- Example: Chris, Katie, Dan, Matt F., etc.

## Performance

- **Small months (1-10 entries):** ~1 second
- **Medium months (50-100 entries):** ~2 seconds  
- **Large months (150+ entries):** ~2-3 seconds
- **Full year (12 months):** ~15-30 seconds depending on entry count

Processing speed is primarily limited by batch categorization, not parsing.
