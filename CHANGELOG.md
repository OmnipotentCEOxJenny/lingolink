# Changelog

## 1.0.4 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.3 (2026-10-23)
- Search keywords: 34 to 40 (added AutoSap, KeepTone, IdiomFlags, RightToLeft, NativeLanguage, AnyLanguage), per Rob's keyword rules.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.2 (2026-10-22)
- `scripts/check_preserved.py` now reports version 1.0.2 (`--version`), matching the plugin version (it said 1.0.0).
- `.gitignore` added: ignores Python cache folders (`__pycache__/`, `*.pyc`).

## 1.0.1 (2026-10-21)
- Added `tests/check_frontmatter.py`: a strict YAML front-matter check (PyYAML `safe_load`) for every SKILL.md and rules .mdc file, plus a plugin.json JSON check. Run `python3 tests/check_frontmatter.py` from the repo root; it catches the unquoted-colon bug fixed in PluginPulse 1.0.2.
- No behavior changes to skills or rules.

## 1.0.0 (2026-10-20)
- First release: translate-text, back-translation-check and auto-sap-mode skills; pillars and translation rule; check_preserved.py (standard library only); worked examples; logo; title, description and specific limits in 23 languages (machine-made, not native-reviewed).
