# MPrint help and legal pages

Published by GitHub Pages from `main` at https://dreamingscientist-coder.github.io/mprint-legal/.

All five pages provide English, French and Vietnamese tabs. Links carry `?lang=en`, `?lang=fr` or `?lang=vi`; the browser also remembers the last choice when local storage is available. Keyboard users can switch tabs with arrow keys, Home and End. Without JavaScript, all three translations remain readable.

Edit `content.json`, then regenerate the static pages:

```sh
python3 tools/build_site.py
python3 tools/check_site.py
node --check language.js
```

Gift card configuration and signing tools live under `gift-card-tools/`. `gift-card-rules.json` supplies per-merchant OCR label phrases; `gift-card-merchants.csv` has columns `merchant,aliases`, with multiple aliases separated by `|`. Add rows and observed label variants there to adapt supported formats without a new app build. After any change, run `gift-card-tools/sign-files.sh /path/to/private.pem`, then commit the changed data and `.sig` sidecars together. The app accepts updates only when both files verify against its pinned public key. Keep the private signing key offline and never commit it. The built-in OCR and rule interpreter run locally; document contents are never uploaded. mPrint checks these files at app startup and whenever the Gift Cards section opens, and uses previously verified cache data offline. New extraction behavior still requires an app update.

The How to use content and release notes match MPrint 1.0.2. Keep the website guide in sync with the app when behavior changes. The English legal clauses have been preserved, with corresponding French and Vietnamese translations.
