# Ad Library Playbook

> URL patterns verified 2026-07. Libraries redesign without notice — if patterns 404, search for the library's current entry point before declaring a source dead.

## Where the ads are

- **Meta Ad Library** — active Facebook/Instagram ads returned for a page or search: `facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[brand]&search_type=keyword_unordered`, or `view_all_page_id=[id]` once you have the page. Shows start date, platforms, and variant count. EU reach ranges appear only for ads delivered in the EU; they are not spend or profitability data.
- **Google Ads Transparency Center** — Search, YouTube, and Display ads returned by advertiser or domain: `adstransparency.google.com/?region=US&domain=[domain]`. Shows available formats and date ranges.
- **TikTok** — `library.tiktok.com` (EU transparency, searchable by advertiser) for a specific brand; TikTok Creative Center "Top Ads" for a TikTok-selected set of high-performing examples, not comprehensive category coverage or proof of profitability.
- **LinkedIn Ad Library** — `linkedin.com/ad-library/search?accountOwner=[company]`. Primarily useful for B2B research; skip when LinkedIn activity is outside the research scope.
- **The funnel behind the ads** — library entries often link the landing page. Also try `site:[domain] "advertorial"`, `/pages/` paths on Shopify stores, and the brand's own UTM'd links surfaced by web search.

## Access reality — the libraries are JavaScript-heavy; a blank page means "next tool", not "next source"

1. Try a direct page fetch — some views server-render enough to inspect.
2. Use an available browser-automation tool for JavaScript-heavy views; render, scroll to load more cards, and read or screenshot them.
3. Search the web for the library entry: `site:facebook.com/ads/library [brand]`, `[brand] "ads transparency"`. Use snippets to discover sources, not as captured ad evidence.
4. Third-party coverage: marketing teardowns, swipe-file roundups, and newsletters quoting the ads verbatim — the same backdoor the research stage uses for Amazon and Reddit.

Only assign an ad ID after verifying the copy and attribution on the library
page or an attributable secondary page.

Record which step worked per platform in the coverage log. If no ads are found
after the full chain, report that no active ads were observed through the
available sources; do not treat absence from the library as proof that the
competitor is not advertising.

## Reading the library

- Filter to active ads and note the observed count per competitor before
  sampling. Label it active inventory; measuring creative velocity requires
  repeated observations over time.
- Treat the displayed start date as first-seen data. Long-running ads and
  clusters of near-identical variants are persistence signals, not proof of
  spend, profitability, or performance.
- Capture verbatim: first line of primary text, headline, CTA. Describe the visual in one line (talking head, UGC testimonial, before/after, product-on-white).
- Coverage floor: attempt 2+ platforms per competitor through the full chain; aim for 10+ ads per major competitor when they're active at all.

## Edge cases

- **Huge advertisers (hundreds of active ads)** → sample three slices: 10 newest, 10 longest-running, and ads with outlier EU reach where available.
- **Whitelabel / dropship categories** → brand names are noise; keyword-search the library for the product category and recon the most visible active advertisers instead.
- **No active ads anywhere** → check for past ads via source-discovery searches and attributable teardowns; report the angle or channel as not observed in the sampled coverage.
- **Ads in another language/market** → capture verbatim in the original plus a bracketed translation; the angle classification still applies.
