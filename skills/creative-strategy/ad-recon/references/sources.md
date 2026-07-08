# Ad Library Playbook

> URL patterns verified 2026-07. Libraries redesign without notice — if patterns 404, search for the library's current entry point before declaring a source dead.

## Where the ads are

- **Meta Ad Library** — every active Facebook/Instagram ad for any page: `facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[brand]&search_type=keyword_unordered`, or `view_all_page_id=[id]` once you have the page. Shows start date, platforms, and variant count. Set an EU country (`country=NL`) to unlock reach ranges under EU transparency rules — the closest thing to public spend data.
- **Google Ads Transparency Center** — Search, YouTube, and Display ads by advertiser or domain: `adstransparency.google.com/?region=US&domain=[domain]`. Shows formats and date ranges; the YouTube coverage is the part nothing else gives you.
- **TikTok** — `library.tiktok.com` (EU transparency, searchable by advertiser) for a specific brand; TikTok Creative Center "Top Ads" for what's winning in the category regardless of brand.
- **LinkedIn Ad Library** — `linkedin.com/ad-library/search?accountOwner=[company]`. B2B only; skip for pure D2C.
- **The funnel behind the ads** — library entries often link the landing page. Also try `site:[domain] "advertorial"`, `/pages/` paths on Shopify stores, and the brand's own UTM'd links surfaced by WebSearch.

## Access reality — the libraries are JavaScript-heavy; a blank page means "next tool", not "next source"

1. WebFetch the direct URL anyway — some views server-render enough to mine.
2. Browser automation (Playwright / Claude in Chrome) — the reliable path for Meta and Google; render, scroll to load more cards, read or screenshot them.
3. WebSearch the library from outside: `site:facebook.com/ads/library [brand]`, `[brand] "ads transparency"` — mine snippets and cached copies.
4. Third-party coverage: marketing teardowns, swipe-file roundups, and newsletters quoting the ads verbatim — the same backdoor the research stage uses for Amazon and Reddit.

Record which step worked per platform in the coverage log. A genuinely empty library after the full chain is a finding — the competitor is dark on that channel — not a failure.

## Reading the library

- Filter to active ads and note the total count per competitor before sampling — creative velocity is itself intelligence.
- Start date ≈ first seen. 90+ days active = proven. A cluster of near-identical variants = the angle they're actively testing right now.
- Capture verbatim: first line of primary text, headline, CTA. Describe the visual in one line (talking head, UGC testimonial, before/after, product-on-white).
- Coverage floor: attempt 2+ platforms per competitor through the full chain; aim for 10+ ads per major competitor when they're active at all.

## Edge cases

- **Huge advertisers (hundreds of active ads)** → sample three slices: 10 newest, 10 longest-running, anything with outlier EU reach. The longest-running slice is the one that matters.
- **Whitelabel / dropship categories** → brand names are noise; keyword-search the library for the product category and recon the top spenders instead.
- **No active ads anywhere** → check for past ads via search snippets and teardowns; report whether the category ever sustained paid before calling the channel open.
- **Ads in another language/market** → capture verbatim in the original plus a bracketed translation; the angle classification still applies.
