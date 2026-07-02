# Source Playbook

## Access reality

- Direct WebFetch works: Trustpilot (`trustpilot.com/review/[domain]`), ConsumerAffairs, SiteJabber, BBB, older forums (vBulletin/phpBB), and review-roundup articles (Wirecutter, Tom's Guide, BuzzFeed). Roundups quote Amazon and Reddit verbatim — they're the backdoor into blocked platforms.
- Blocked for bots (429/403/CAPTCHA): Reddit, Amazon, Quora, Walmart — start at step 2 below.
- Indirect only: YouTube comments, Facebook groups — find articles that quote them.

## Fallback chain — a 403 means "next tool", not "next source"

1. WebFetch the direct URL (Reddit: `old.reddit.com`; Amazon: `amazon.com/product-reviews/[ASIN]`)
2. Browser automation (Playwright / Claude in Chrome) — second attempt on any blocked source, not a last resort
3. WebSearch with `site:` and mine the snippets. Emotional phrases surface the richest results:
   - `site:reddit.com [product] "doesn't work" OR "waste of money" OR "I've tried everything"`
   - `site:reddit.com [product] "game changer" OR "finally found"`
   - `site:amazon.com [product] review "I bought" OR "is it worth"`
4. Search for articles quoting the platform (`"reddit recommends" [category]`, `[product] review site:wirecutter.com`) and fetch those.

Only mark a platform exhausted after multiple URLs × the whole chain. Record which step succeeded in the coverage log.

## Edge cases

- Product too niche for reviews → search the pain, not the product ("hard water stains toilet", not the brand name).
- Pre-launch product → research the category and nearest competitors; flag everything as category-level.
- 500+ reviews available → read 1-star and 5-star first (strongest signal), then 3-star (trade-offs). 40 high-signal quotes beat 150 generic ones.
- Reviews dominated by shipping complaints → filter them out, but note the pattern as a buyer-expectation signal.
- Sources contradict each other → don't reconcile; report the tension as a surprising finding.
