# GAQL Cookbook — Replicate Google Ads UI Screens

Ready-to-use queries matching default Google Ads UI views. All dated queries
default to LAST_7_DAYS. Adjust date range as needed.

## Table of Contents

- [Campaigns](#campaigns)
- [Ad Groups](#ad-groups)
- [Ads](#ads)
- [Search Keywords](#search-keywords)
- [Search Terms](#search-terms)
- [Audiences](#audiences)
- [Age Demographics](#age-demographics)
- [Gender Demographics](#gender-demographics)
- [Locations](#locations)
- [Geo Constant Lookups](#geo-constant-lookups)

## Campaigns

```sql
SELECT campaign.name, campaign_budget.amount_micros, campaign.status,
  campaign.optimization_score, campaign.advertising_channel_type,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros,
  campaign.bidding_strategy_type
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status != 'REMOVED'
```

## Ad Groups

```sql
SELECT ad_group.name, campaign.name, ad_group.status, ad_group.type,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros
FROM ad_group
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group.status != 'REMOVED'
```

## Ads

Fetches individual ad components (headlines, descriptions, final URLs).

```sql
SELECT ad_group_ad.ad.expanded_text_ad.headline_part1,
  ad_group_ad.ad.expanded_text_ad.headline_part2,
  ad_group_ad.ad.expanded_text_ad.headline_part3,
  ad_group_ad.ad.final_urls,
  ad_group_ad.ad.expanded_text_ad.description,
  ad_group_ad.ad.expanded_text_ad.description2,
  campaign.name, ad_group.name,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.ad.type,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros
FROM ad_group_ad
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_ad.status != 'REMOVED'
```

## Search Keywords

```sql
SELECT ad_group_criterion.keyword.text,
  campaign.name, ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.approval_status,
  ad_group_criterion.final_urls,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros
FROM keyword_view
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_criterion.status != 'REMOVED'
```

## Search Terms

```sql
SELECT search_term_view.search_term,
  segments.keyword.info.match_type,
  search_term_view.status,
  campaign.name, ad_group.name,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros,
  campaign.advertising_channel_type
FROM search_term_view
WHERE segments.date DURING LAST_7_DAYS
```

## Audiences

Audience criterion IDs map to display names in the
[Codes and formats](https://developers.google.com/google-ads/api/data/codes-formats) reference.
Use `ad_group_criterion.type` to determine which criteria type table to look up.

```sql
SELECT ad_group_criterion.resource_name, ad_group_criterion.type,
  campaign.name, ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros,
  campaign.advertising_channel_type
FROM ad_group_audience_view
WHERE segments.date DURING LAST_7_DAYS
```

## Age Demographics

```sql
SELECT ad_group_criterion.age_range.type,
  campaign.name, ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros,
  campaign.advertising_channel_type
FROM age_range_view
WHERE segments.date DURING LAST_7_DAYS
```

## Gender Demographics

```sql
SELECT ad_group_criterion.gender.type,
  campaign.name, ad_group.name,
  ad_group_criterion.system_serving_status,
  ad_group_criterion.bid_modifier,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros,
  campaign.advertising_channel_type
FROM gender_view
WHERE segments.date DURING LAST_7_DAYS
```

## Locations

Location criterion IDs map to display names via
[geo target data](https://developers.google.com/google-ads/api/data/geotargets)
or by querying `geo_target_constant`.

```sql
SELECT campaign_criterion.location.geo_target_constant,
  campaign.name, campaign_criterion.bid_modifier,
  metrics.clicks, metrics.impressions, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros
FROM location_view
WHERE segments.date DURING LAST_7_DAYS
  AND campaign_criterion.status != 'REMOVED'
```

## Geo Constant Lookups

### By resource name

```sql
SELECT geo_target_constant.canonical_name, geo_target_constant.country_code,
  geo_target_constant.id, geo_target_constant.name,
  geo_target_constant.status, geo_target_constant.target_type
FROM geo_target_constant
WHERE geo_target_constant.resource_name = 'geoTargetConstants/1014044'
```

### By display name

```sql
SELECT geo_target_constant.canonical_name, geo_target_constant.country_code,
  geo_target_constant.id, geo_target_constant.name,
  geo_target_constant.status, geo_target_constant.target_type
FROM geo_target_constant
WHERE geo_target_constant.name = 'Mountain View'
  AND geo_target_constant.country_code = 'US'
  AND geo_target_constant.target_type = 'City'
  AND geo_target_constant.status = 'ENABLED'
```
