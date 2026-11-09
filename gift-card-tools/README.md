# Gift card rules

The app downloads these public data files and accepts them only when their RSA/SHA-256 sidecar signatures match the public key pinned in mPrint:

- `gift-card-rules.json` and `gift-card-rules.json.sig`
- `gift-card-merchants.csv` and `gift-card-merchants.csv.sig`

Edit the JSON label arrays or the CSV merchant rows. Keep CSV aliases pipe-separated in the `aliases` column. Then sign both files with the private key kept outside this repository:

```sh
./gift-card-tools/sign-files.sh /Users/khacmuoivu/Developer/Apps/mprint-giftcard-signing/private.pem
git add gift-card-tools
git commit -m "Update gift card tools"
git push origin main
```

Never commit or share `private.pem`. The app contains only the matching public key. Installing the app version that adds signature verification is required once; future signed merchant and label updates do not require a new build. Changing the signing key requires an app update to pin the replacement public key.
