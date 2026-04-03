# Synthesis workflow

This project **does not** use OpenAI, Anthropic, or any other external inference API.

1. **Python (local)** — `summarizer.py` produces **rule-based, tagged drafts** from journals or `monthly_dumps/*.md`.
2. **Cursor (in-editor)** — For editorial synthesis (merged themes, tone, closing paragraph), use **`CURSOR_SYNTHESIS_INSTRUCTIONS.md`** with the monthly dump file in a Cursor chat.

There is nothing to configure for paid APIs in `config.yaml`.
