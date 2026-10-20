# LingoLink

LingoLink is a free translation plugin. It gives your AI assistant clear rules and skills for translating text between languages honestly: it keeps meaning and tone, leaves names, code, URLs and numbers exactly as written, flags idioms, legal, medical and low-confidence passages, offers a back-translation check, and labels every result as machine translation.

It uses no paid service, API or key: the host AI does the translating. It includes Auto-SAP mode (set your native language once and foreign-language content is translated automatically, like the SAP button on a TV), works with any language on request, and ships a small optional Python script (standard library only) that checks a translation kept every URL, number and code span.

Invented by Rob Domaine / Omnipotent Media LLC.

![LingoLink logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-20: v1.0.0 repo checks and host-AI test runs (English to Spanish, Japanese to English, Arabic right-to-left, a text with a URL, number and code, Auto-SAP mode, Welsh and Yoruba on request), each with a back-translation check and `check_preserved.py`.

**Pending**
- In-app load test in Cursor or Grok Build: not done; the build computer has neither app.
- Native-speaker review of the test translations and of TRANSLATIONS.md.
- Marketplace submission: not submitted.

**Uncertain**
- Whether Grok Build reads the `.cursor-plugin/plugin.json` manifest format (UNVERIFIED).

## Quick start
1. Install from https://github.com/OmnipotentCEOxJenny/lingolink (copy to `~/.cursor/plugins/local/lingolink` and reload).
2. Ask: "Translate to Spanish: The meeting is at 3:30 PM, see https://example.com/agenda."
3. Ask: "Back-translate that and check it."
4. Say: "Auto-SAP: my native language is English."

## Auto-SAP mode
Like the SAP (second audio program) button on a TV. Set your native language once, by saying it or by confirming the language LingoLink infers from how you write. From then on, any content in another language that you share or that the AI reads is detected and translated into your native language automatically. You don't need to switch anything by hand.
- Content already in your native language passes through unchanged.
- Each translation shows the detected source language, for example `Auto-SAP: detected French -> English. Machine translation.`
- The original stays available: say "show original".
- Mixed-language text is handled segment by segment, and each translated segment is tagged with its language.
- Short or ambiguous snippets are marked `LOW-CONFIDENCE detection`.
- "Auto-SAP off" stops it.

## Any language on request
LingoLink never refuses a language because it is not one of the 23. Those 23 are only the languages of the plugin's own documentation. The host AI does the translating, and it covers many more languages. For a new language, LingoLink:
- attempts the translation and labels it machine translation pending native review
- warns that quality may be lower for lower-resource languages and offers a back-translation check
- records the language in the user-editable `languages.json` file, under `"added"`, so it counts as available in later sessions while the host keeps that file

Nothing is downloaded and no language packs are installed.

## Testing
1. Ask: "Translate to Spanish: Run `npm test` before 5 PM; details at https://example.com/docs (ticket 4821)."
2. Expected result: a Spanish translation in which `npm test`, the URL, 5 PM and 4821 are unchanged, a machine-translation label and an offer to back-translate.
3. Optional: save both texts and run `python3 scripts/check_preserved.py source.txt translation.txt`. Expect `PASS`.
4. Ask in Japanese. LingoLink answers in Japanese.

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- LingoLink is independent and is not endorsed by xAI or Anysphere (Cursor).

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never invent; anything unchecked is marked UNVERIFIED.
2. Use only legitimate means: legitimate, proven sources and methods; unreliable sources rejected.
3. Double-check everything: every finding is confirmed by two independent checks, and the report shows both.
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/translate-text`: honest translation with protected items and FLAG lines.
- `skills/back-translation-check`: back-translation comparison and a check of preserved items.
- `skills/auto-sap-mode`: automatic translation into the user's native language.
- `skills/add-language`: any language on request; updates `languages.json`.
- `rules/pillars-and-scope.mdc`: Rob Domaine's four pillars, translation rules and language rules.
- `languages.json`: 23 documented languages and the languages users have added (user-editable).
- `scripts/check_preserved.py`: Python 3 standard library only; checks URLs, numbers and code spans.
- `TRANSLATIONS.md`: title, description and specific limits in 23 languages (machine-made).

## Requirements
- A host AI that loads Cursor-format plugins. The optional script needs only Python 3 and installs nothing.

## Languages
The AI answers in the user's language and keeps commands, file names and status labels unchanged. Title, description and honest-assessment summaries in 23 languages are in TRANSLATIONS.md: Español, Français, Português, Deutsch, Italiano, Nederlands, Polski, Русский, Українська, Türkçe, العربية, עברית, فارسی, हिन्दी, বাংলা, اردو, 简体中文, 日本語, 한국어, Bahasa Indonesia, Tiếng Việt, Kiswahili, Tagalog / Filipino. They are machine translations, not yet reviewed by native speakers; the English text is authoritative.

## Feedback
Open an issue for a wrong translation or a feature idea, or use Discussions. Native speakers are very welcome.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
Written to be fully transparent. If something here is wrong or out of date, please open an issue.

- All output is machine translation by the host AI. It is not a certified, sworn, notarized or official translation, and it can be wrong. For legal, medical, immigration or other high-stakes documents, use a qualified human translator.
- Translation quality depends on the host AI and varies by language. Lower-resource languages and some scripts may come out poorly.
- A back-translation by the same AI is only a sanity check. It is not proof of accuracy, because it can repeat the same mistake.
- `check_preserved.py` only checks that URLs, numbers and code spans appear in exactly the same form. It cannot judge meaning. It reports localized numbers, like 1.000 written for 1,000, as missing, so a person needs to look at them.
- Auto-SAP mode only works on content the host AI handles in the conversation. It cannot translate other apps, videos, audio, images it cannot read, or the whole screen.
- Language detection can be wrong, especially for short or mixed-language text.
- How long the native-language setting and any added languages last depends on the host. Added languages persist only while the host keeps `languages.json`. Nothing is downloaded, and no language packs are installed.
- The test translations have not yet been reviewed by native speakers. The plugin has not been loaded inside the Cursor app or Grok Build yet.
- Marketplace status: not submitted yet. Once submitted, it stays pending until approved.
- It collects no data and needs no account or API key. Don't paste confidential documents unless your host AI's own terms allow it.
- Translations: the 23 translated summaries in TRANSLATIONS.md are machine-made and have not been reviewed by native speakers. The English text is authoritative.
- It is not legal advice and cannot guarantee that any particular use is lawful; you remain responsible for how you use it.
- Rules and compliance: it is built to follow all local, county, state and federal laws and every platform's rules. It uses no paid services, never bypasses logins, paywalls, CAPTCHAs or access controls, and never claims a feature it does not have.
