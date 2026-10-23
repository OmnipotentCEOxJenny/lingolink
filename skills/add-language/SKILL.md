---
name: add-language
description: "Handle a request for any language, including ones outside the 23 documented languages: attempt the translation, label it, warn about lower-resource languages and record the language in languages.json for later sessions. Use when a user asks for a language not listed in languages.json."
---

# Any language on request

Follow `rules/scope.mdc`. Answer in the user's language; keep commands, file names and status labels unchanged.

1. **Do not refuse.** Explain once, briefly: the 23 languages are only the plugin's own documentation; the translation is done by the host AI, which covers many more languages.
2. **Translate** with `skills/translate-text` and label it: "Machine translation (LingoLink, host AI), pending native review. Not certified or official."
3. **Lower-resource languages** (for example Welsh, Yoruba, Quechua, Hawaiian, many regional languages and rare scripts): warn "Quality may be lower for this language" and offer `skills/back-translation-check`.
4. **Record it** in `languages.json` under `"added"` as `{"code": "<ISO 639 code>", "name": "<name in that language>", "added": "<YYYY-MM-DD>", "status": "machine translation, pending native review", "resource": "lower" or "standard"}`. Skip it if already present. If you cannot write files, give the user the JSON line to add. The file is user-editable.
5. **Be honest:** nothing is downloaded or installed; the language stays available only while the host keeps `languages.json`.
