// Reverse face search with the Apify JavaScript client.
// Usage:
//   npm install apify-client
//   APIFY_TOKEN=... node search.js https://example.com/photo.jpg [fast|deep]
import { ApifyClient } from 'apify-client';

const [imageUrl, mode = 'fast'] = process.argv.slice(2);
if (!imageUrl) {
    console.error('usage: node search.js <image-url> [fast|deep]');
    process.exit(1);
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('d4rknode/facecheck-reverse-face-search').call({ imageUrl, mode });
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    if (!item.success) {
        console.log('Search failed (not charged), retry:', item.message);
        continue;
    }
    console.log(`${item.total} match(es)`);
    for (const m of item.matches) console.log(`  ${String(m.confidence).padStart(3)}  ${m.url}`);
}
