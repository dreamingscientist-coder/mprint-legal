#!/bin/bash
set -euo pipefail

if [[ $# -ne 1 || ! -f "$1" ]]; then
  echo "Usage: $0 /path/to/private.pem" >&2
  exit 2
fi
key="$1"
script_dir="$(cd "$(dirname "$0")" && pwd)"
for name in gift-card-rules.json gift-card-merchants.csv; do
  file="$script_dir/$name"
  temp="$file.sig.bin"
  openssl dgst -sha256 -sign "$key" -out "$temp" "$file"
  openssl base64 -A -in "$temp" -out "$file.sig"
  rm -f "$temp"
done
echo "Signed gift card rules and merchant list."
