# MPrint help and legal pages

Published by GitHub Pages from `main` at https://dreamingscientist-coder.github.io/mprint-legal/.

All five pages provide English, French and Vietnamese tabs. Links carry `?lang=en`, `?lang=fr` or `?lang=vi`; the browser also remembers the last choice when local storage is available. Keyboard users can switch tabs with arrow keys, Home and End. Without JavaScript, all three translations remain readable.

Edit `content.json`, then regenerate the static pages:

```sh
python3 tools/build_site.py
python3 tools/check_site.py
node --check language.js
```

`gift-card-rules.json` is the public, declarative gift-card import ruleset used by mPrint. Increment `rulesVersion` for every published change. It supplies merchant names/aliases and per-merchant label phrases for balance, expiry, card number, and PIN. The app applies its built-in OCR engine and rule interpreter locally; rules cannot execute code, and document contents are never uploaded here. Add observed label variants to the relevant arrays to adapt supported formats without a new app build. Keep field names within the current schema; genuinely new extraction behavior requires an app update. mPrint caches the last valid version and keeps manual entry available if this file cannot be fetched.

The How to use content and release notes match MPrint 1.0.2. Keep the website guide in sync with the app when behavior changes. The English legal clauses have been preserved, with corresponding French and Vietnamese translations.
