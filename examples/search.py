"""Reverse face search with the Apify Python client (apify-client v3+).

Usage:
    pip install apify-client
    APIFY_TOKEN=... python search.py https://example.com/photo.jpg [fast|deep]
    APIFY_TOKEN=... python search.py ./photo.jpg deep      # local file, sent as base64
"""

import base64
import os
import sys

from apify_client import ApifyClient

ACTOR = "d4rknode/facecheck-reverse-face-search"


def build_input(source: str, mode: str) -> dict:
    if source.startswith(("http://", "https://")):
        return {"imageUrl": source, "mode": mode}
    with open(source, "rb") as f:
        return {"image": base64.b64encode(f.read()).decode(), "mode": mode}


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: python search.py <image-url-or-path> [fast|deep]")
    source = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "fast"

    client = ApifyClient(os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR).call(run_input=build_input(source, mode))

    for item in client.dataset(run.default_dataset_id).iterate_items():
        if not item["success"]:
            print("Search failed (not charged), retry:", item["message"])
            continue
        print(f"{item['total']} match(es)")
        for match in item["matches"]:
            print(f"  {match['confidence']:>3}  {match['url']}")


if __name__ == "__main__":
    main()
