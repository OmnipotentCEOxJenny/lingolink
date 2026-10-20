---
name: translate-text
description: "Translate text between languages honestly: keep meaning, tone, names, code, URLs and numbers, flag idioms, legal or medical text and low-confidence passages, and mark the result as machine translation. Use when a user asks to translate text."
---

# Translate text

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language; keep commands, file names and status labels unchanged.

1. **Identify** the source language (say "Detected: <language>"; if unsure, say so and ask) and the target language.
2. **Protect** before translating: names, brands, code spans and blocks, URLs, e-mail addresses, numbers, dates, units, hashtags and @handles stay exactly as written. Right-to-left text (Arabic, Hebrew, Persian, Urdu) keeps embedded Latin items and numbers in their original form.
3. **Translate** meaning and tone (formal stays formal, casual stays casual). Do not add, drop or soften content.
4. **Flag** below the translation, one line each:
   - `FLAG idiom:` idioms, wordplay, cultural references, with the literal meaning.
   - `FLAG legal/medical/financial/immigration:` and recommend a qualified human translator; for official use a certified translation is usually required.
   - `FLAG LOW-CONFIDENCE:` ambiguous, unclear, slang or garbled passages, and why.
5. **Label** the output: "Machine translation (LingoLink, host AI). Not certified or official."
6. **Offer** the back-translation check (`skills/back-translation-check`). Optional local check: `python3 scripts/check_preserved.py source.txt translation.txt`.
