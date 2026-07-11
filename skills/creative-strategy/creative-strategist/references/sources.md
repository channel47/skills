# Source Playbook

## Access reality

These access notes are starting points, not guarantees. Sites change their
rendering and bot controls; record the method that worked during the current
run.

- A direct page-fetch tool may work for Trustpilot (`trustpilot.com/review/[domain]`), ConsumerAffairs, SiteJabber, BBB, older forums (vBulletin/phpBB), and review-roundup articles.
- If Reddit, Amazon, Quora, or Walmart returns 429/403/CAPTCHA, continue at step 2 below.
- For sources unavailable to the configured tools, look for attributable articles that quote them and cite the article as the source.

## Fallback chain — a 403 means "next tool", not "next source"

1. Use an available page-fetch tool on the direct URL (Reddit: `old.reddit.com`; Amazon: `amazon.com/product-reviews/[ASIN]`)
2. Use an available browser-automation tool on blocked or JavaScript-heavy sources
3. Use web search with `site:` to discover candidate source pages:
   - `site:reddit.com [product] "doesn't work" OR "waste of money" OR "I've tried everything"`
   - `site:reddit.com [product] "game changer" OR "finally found"`
   - `site:amazon.com [product] review "I bought" OR "is it worth"`
4. Search for articles quoting the platform (`"reddit recommends" [category]`, `[product] review site:wirecutter.com`) and fetch those.

Search snippets are discovery hints only. Do not assign a quote ID until the
wording and attribution are verified on the source page or an attributable
secondary page.

Only mark a platform exhausted after multiple URLs × the whole chain. Record which step succeeded in the coverage log.

## Edge cases

- Product too niche for reviews → search the pain, not the product ("hard water stains toilet", not the brand name).
- Pre-launch product → research the category and nearest competitors; flag everything as category-level.
- 500+ reviews available → read 1-star and 5-star first (strongest signal), then 3-star (trade-offs). 40 high-signal quotes beat 150 generic ones.
- Reviews dominated by shipping complaints → filter them out, but note the pattern as a buyer-expectation signal.
- Sources contradict each other → don't reconcile; report the tension as a
  non-obvious supported finding.
