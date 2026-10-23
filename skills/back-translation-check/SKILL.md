---
name: back-translation-check
description: "Check a translation by translating it back into the source language and comparing meaning, plus a check that URLs, numbers and code spans were preserved. Use when a user wants to verify a translation."
---

# Back-translation check

Follow `rules/scope.mdc`. Answer in the user's language; keep commands, file names and status labels unchanged.

1. Translate the translation back into the source language without looking at the original wording.
2. Compare sentence by sentence; report MATCH, SHIFT (meaning or tone changed, with detail) or LOSS (content missing).
3. Preserved items: list every URL, number and code span in the source and confirm each appears unchanged in the translation. If files are available, run `python3 scripts/check_preserved.py source.txt translation.txt` (Python 3 standard library only, no install).
4. Say honestly: a back-translation by the same AI is a sanity check, not proof; it can miss shared mistakes. For anything important, ask a native speaker or professional.
