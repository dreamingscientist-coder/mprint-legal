# MPrint help and legal pages

Published by GitHub Pages from `main` at https://dreamingscientist-coder.github.io/mprint-legal/.

All five pages provide English, French and Vietnamese tabs. Links carry `?lang=en`, `?lang=fr` or `?lang=vi`; the browser also remembers the last choice when local storage is available. Keyboard users can switch tabs with arrow keys, Home and End. Without JavaScript, all three translations remain readable.

Edit `content.json`, then regenerate the static pages:

```sh
python3 tools/build_site.py
python3 tools/check_site.py
node --check language.js
```

The How to use content and release notes match MPrint 1.0.2. Keep the website guide in sync with the app when behavior changes. The English legal clauses have been preserved, with corresponding French and Vietnamese translations.
