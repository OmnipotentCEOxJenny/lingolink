---
name: auto-sap-mode
description: "Auto-SAP mode, like the SAP button on a TV: the user sets a native language once, then any content in another language that the user shares or the host AI reads is detected and translated into the native language automatically. Use when a user turns on auto-translate, sets a native language, or says Auto-SAP."
---

# Auto-SAP mode

Follow `rules/scope.mdc`. Answer in the user's language; keep commands, file names and status labels unchanged.

1. **Set the native language once.** Use the language the user states. If none is stated, infer it from the language the user writes in and confirm: "Auto-SAP: native language = <language>. Correct?" Do not start until confirmed. The setting lasts for this conversation (or the host's memory, if the host offers it); say which.
2. **Automatic from then on.** For every piece of content the user shares or the host AI reads (pasted text, files, web pages or tool results the host AI loads):
   - Detect its language. If it is the native language, pass it through unchanged, with no translation note.
   - Otherwise translate it into the native language with `skills/translate-text` (same protection of names, code, URLs, numbers; same FLAG lines), headed `Auto-SAP: detected <language> -> <native language>. Machine translation.`
3. **Mixed-language text:** split into segments (sentence or clause), detect each, translate only the non-native segments, and mark each translated segment with its detected language, for example `[fr]`.
4. **Short or ambiguous snippets** (a few words, names, words shared by several languages): say `LOW-CONFIDENCE detection` with the likely candidates, give the best translation, and ask if needed.
5. **Original on request:** keep the original text; show it when the user asks "show original". Offer the back-translation check for anything important.
6. **Off switch:** "Auto-SAP off" stops it; "Auto-SAP <language>" changes the native language.
7. Honest limits: only content the host AI handles in this conversation; it cannot translate other apps, videos, audio or the whole screen.
