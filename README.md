# Reverse Face Search API (FaceCheck.ID)

**Reverse Face Search API is an unofficial Apify Actor that runs a reverse face search on [FaceCheck.ID](https://facecheck.id) from a photo or image URL and returns the web pages where that face appears, each with a 0–100 confidence score and a face thumbnail.**

▶ **Run it on Apify:** https://apify.com/d4rknode/facecheck-reverse-face-search

> Unofficial and community-built. Not affiliated with, endorsed by, or connected to FaceCheck.ID. I'm the author of the Actor.

This repo contains copy-paste examples for calling the Actor from curl, Python and JavaScript.

## Quick facts

| | |
|---|---|
| **Input** | One face image: base64 string **or** public image URL (JPEG, PNG, WebP, max 10 MB) |
| **Output** | JSON: matching pages (domain or full URL), confidence 0–100, face thumbnail (base64) |
| **Fast mode** | $0.02 per search, domain-level matches (e.g. `https://instagram.com`) |
| **Deep mode** | $0.29 per search, full source URL of every match, sorted by confidence |
| **Billing** | Flat price per search via Apify: all matches included, no start or per-result fees. Charged only for successful searches. |
| **Account needed** | An Apify account only. No FaceCheck.ID account, credits or crypto. |

## Examples

Set your Apify API token first (Apify Console → Settings → API & Integrations):

```bash
export APIFY_TOKEN=your_token_here
```

| File | What it does |
|---|---|
| [`examples/curl.sh`](examples/curl.sh) | One HTTP call that runs a search and returns the results |
| [`examples/search.py`](examples/search.py) | Python (`pip install apify-client`) |
| [`examples/search.js`](examples/search.js) | Node.js (`npm install apify-client`) |

### curl

```bash
curl -X POST "https://api.apify.com/v2/acts/d4rknode~facecheck-reverse-face-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"imageUrl": "https://example.com/photo.jpg", "mode": "fast"}'
```

### Output

```json
[
  {
    "success": true,
    "total": 1,
    "matches": [
      { "url": "https://example-social.com", "confidence": 92, "thumbnail": "UklGRl..." }
    ],
    "note": "Fast mode shows the domain only. Run deep mode for full source URLs."
  }
]
```

Errors come back as `{"success": false, "message": "..."}` and are not charged.

## Fast vs. deep

Fast mode ($0.02) tells you **which websites** a face appears on: it keeps matches scoring 70+, or up to 6 matches scoring 50–69 if there are none. Deep mode ($0.29) gives you **the exact pages**: the full URL of every match FaceCheck.ID finds. A cheap pattern is to screen many photos in fast mode, then run deep mode only on photos with matches.

## How it compares to the official FaceCheck.ID API

FaceCheck.ID has its own [official REST API](https://facecheck.id/Face-Search/API), priced at 3 credits per search at $0.10 per credit (about $0.30), paid in Bitcoin or Litecoin (as stated on that page in November 2026). This Actor is an unofficial alternative that bills by card through Apify, charges only for successful searches, and adds a $0.02 domain-only fast mode.

## Use it from Claude, Cursor or other MCP clients

Point an MCP client at Apify's MCP server with this Actor enabled:

```
https://mcp.apify.com?actors=d4rknode/facecheck-reverse-face-search
```

## Responsible use

- Use it lawfully. Face images count as biometric data in some jurisdictions.
- Don't use it to stalk or harass anyone, or for employment, tenant, credit or insurance decisions.
- A match means visual similarity, not proof of identity. Verify before acting.

## License

Examples in this repo are MIT-licensed. The Actor itself runs on Apify and is billed there.
