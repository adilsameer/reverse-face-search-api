#!/usr/bin/env bash
# Reverse face search via the Apify API: runs the Actor and returns results in one call.
# Usage: APIFY_TOKEN=... ./curl.sh https://example.com/photo.jpg [fast|deep]
set -euo pipefail

IMAGE_URL="${1:?usage: ./curl.sh <image-url> [fast|deep]}"
MODE="${2:-fast}"

curl -sS -X POST \
  "https://api.apify.com/v2/acts/d4rknode~facecheck-reverse-face-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN:?set APIFY_TOKEN first}" \
  -H "Content-Type: application/json" \
  -d "{\"imageUrl\": \"${IMAGE_URL}\", \"mode\": \"${MODE}\"}"
echo
