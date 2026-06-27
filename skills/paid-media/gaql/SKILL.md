---
name: gaql
description: |
  Write, debug, and validate Google Ads Query Language (GAQL) queries for the
  Google Ads API. Use when: (1) constructing GAQL queries for GoogleAdsService
  Search/SearchStream, (2) debugging GAQL validation errors (field compatibility,
  date range, segment rules), (3) replicating Google Ads UI screens via API.
  Covers grammar, clause rules, operators, date ranges, and cookbook queries.
---

# Google Ads Query Language (GAQL)

## Formal Grammar

```
Query            -> SelectClause FromClause WhereClause? OrderByClause?
                    LimitClause? ParametersClause?
SelectClause     -> SELECT FieldName (, FieldName)*
FromClause       -> FROM ResourceName
WhereClause      -> WHERE Condition (AND Condition)*
OrderByClause    -> ORDER BY Ordering (, Ordering)*
LimitClause      -> LIMIT PositiveInteger
ParametersClause -> PARAMETERS Literal = Value (, Literal = Value)*

Condition        -> FieldName Operator Value
Operator         -> = | != | > | >= | < | <= | IN | NOT IN |
                    LIKE | NOT LIKE | CONTAINS ANY | CONTAINS ALL |
                    CONTAINS NONE | IS NULL | IS NOT NULL | DURING |
                    BETWEEN | REGEXP_MATCH | NOT REGEXP_MATCH
Value            -> Literal | LiteralList | Number | NumberList | String |
                    StringList | Function
Ordering         -> FieldName (ASC | DESC)?

FieldName        -> [a-z] ([a-zA-Z0-9._])*
ResourceName     -> [a-z] ([a-zA-Z_])*
String           -> (' Char* ') | (" Char* ")
Number           -> -? [0-9]+ (. [0-9]+)?
PositiveInteger  -> [1-9] ([0-9])*
Literal          -> [a-zA-Z0-9_]*

Function         -> LAST_14_DAYS | LAST_30_DAYS | LAST_7_DAYS |
                    LAST_BUSINESS_WEEK | LAST_MONTH | LAST_WEEK_MON_SUN |
                    LAST_WEEK_SUN_SAT | THIS_MONTH | THIS_WEEK_MON_TODAY |
                    THIS_WEEK_SUN_TODAY | TODAY | YESTERDAY
```

## Clauses

### SELECT (required)

Comma-separated list of resource fields, segment fields, and/or metrics.

```sql
SELECT campaign.id, campaign.name, metrics.clicks, segments.device
FROM campaign
```

**Restrictions:**
- Cannot select fields with `Selectable = false`
- Cannot select repeated fields (`isRepeated = true`)
- Fields must be available for the FROM resource
- Segments and metrics must be compatible with each other (check via `GoogleAdsFieldService`)

### FROM (required for GoogleAdsService)

Single resource name. Determines which fields are available in all other clauses.

```sql
FROM campaign        -- campaign resource
FROM ad_group        -- ad group resource
FROM keyword_view    -- keyword metrics view
```

**Attributed resources** are implicitly joined. Select their fields directly:

```sql
SELECT campaign.id, ad_group.id, bidding_strategy.name
FROM ad_group
```

The `resource_name` of the FROM resource is always returned, even if not selected.

**No FROM clause** when querying `GoogleAdsFieldService` for field metadata.

### WHERE (optional)

One or more conditions joined by AND. Pattern: `field_name Operator value`.

```sql
WHERE campaign.status != 'REMOVED'
  AND metrics.impressions > 1000
  AND segments.date DURING LAST_30_DAYS
```

**Segment rule:** Segments in WHERE must also be in SELECT, EXCEPT core date segments:
- `segments.date`
- `segments.week`
- `segments.month`
- `segments.quarter`
- `segments.year`

**Core date segment rule:** If ANY core date segment is in SELECT, a finite date range
using a core date segment MUST appear in WHERE.

### ORDER BY (optional)

```sql
ORDER BY metrics.clicks DESC, campaign.name ASC
```

Default direction is ASC. Multiple fields comma-separated.

### LIMIT (optional)

```sql
LIMIT 50
```

Truncates results. Use `GoogleAdsService.Search` (paginated) for large result sets.

### PARAMETERS (optional)

```sql
PARAMETERS include_drafts = true
PARAMETERS omit_unselected_resource_names = true
```

- `include_drafts` — include draft entities (default: false)
- `omit_unselected_resource_names` — suppress auto-returned resource_name fields (default: false). Warning: resources without resource_name cannot be used in mutate operations.

## Operators

### Comparison
`=`, `!=`, `>`, `>=`, `<`, `<=`

### Set membership
`IN (val1, val2)`, `NOT IN (val1, val2)`

### Pattern matching
`LIKE 'pattern%'`, `NOT LIKE 'pattern%'`
- `%` = wildcard (any chars), `_` = single char
- Escape literal `[`, `]`, `%`, `_` by wrapping in square brackets: `'[[]Earth[_]to[_]Mars[]]%'`
- Only works on string fields, not arrays

### Array operators
`CONTAINS ANY (val1, val2)`, `CONTAINS ALL (val1, val2)`, `CONTAINS NONE (val1, val2)`

### Null checks
`IS NULL`, `IS NOT NULL`

### Date operators
`DURING LAST_30_DAYS`, `BETWEEN '2024-01-01' AND '2024-01-31'`

### Regex
`REGEXP_MATCH "pattern"`, `NOT REGEXP_MATCH "pattern"`
- Uses RE2 syntax
- Case sensitive by default; prefix with `(?i)` for case insensitive

## Case Sensitivity

| Operator | Case |
|----------|------|
| `=`, `!=` | Sensitive |
| `IN`, `NOT IN` | Sensitive |
| `LIKE`, `NOT LIKE` | **Insensitive** |
| `CONTAINS ANY/ALL/NONE` | Sensitive |
| `REGEXP_MATCH` | Sensitive (use `(?i)` for insensitive) |

## Date Ranges

### Custom dates (ISO 8601)

```sql
segments.date BETWEEN '2024-01-01' AND '2024-01-31'
segments.date >= '20240101' AND segments.date <= '20240131'
```

### Predefined date ranges (use with DURING)

| Range | Meaning |
|-------|---------|
| `TODAY` | Today only |
| `YESTERDAY` | Yesterday only |
| `LAST_7_DAYS` | Last 7 days, not including today |
| `LAST_14_DAYS` | Last 14 days, not including today |
| `LAST_30_DAYS` | Last 30 days, not including today |
| `LAST_BUSINESS_WEEK` | Mon-Fri of previous business week |
| `THIS_MONTH` | All days in current month |
| `LAST_MONTH` | All days in previous month |
| `THIS_WEEK_SUN_TODAY` | Previous Sunday to today |
| `THIS_WEEK_MON_TODAY` | Previous Monday to today |
| `LAST_WEEK_SUN_SAT` | 7-day period starting previous Sunday |
| `LAST_WEEK_MON_SUN` | 7-day period starting previous Monday |

### Predefined time periods

`segments.week`, `segments.month`, `segments.quarter` — filter with `=` using first day of period:

```sql
segments.month = '2024-05-01'
```

Using a date that isn't the first day of the period returns `MISALIGNED_DATE_FOR_FILTER`.

## Field Metadata Queries

Query `GoogleAdsFieldService` (no FROM clause) to discover field compatibility:

```sql
SELECT name, category, selectable, filterable, sortable,
  selectable_with, data_type, is_repeated
WHERE name = "campaign"
```

Replace `"campaign"` with any resource or field name (e.g., `"metrics.impressions"`, `"ad_group.id"`).

## Common Gotchas

1. **Selecting incompatible segments/metrics** — use `GoogleAdsFieldService` to check `selectable_with`
2. **Missing date range** — if you SELECT a core date segment, you MUST filter on one in WHERE
3. **Filtering on unselected segments** — non-date segments in WHERE must also be in SELECT
4. **Enum values are strings** — `campaign.status = 'PAUSED'` not `campaign.status = PAUSED` (except for `REMOVED` which works both ways in practice; use quotes to be safe)
5. **cost_micros** — all cost values are in micros (divide by 1,000,000 for actual currency)
6. **resource_name always returned** — the FROM resource's resource_name is always in results
7. **No OR operator** — only AND between conditions. Use IN for OR-like behavior on same field
8. **If resource is listed as a segment** — selecting its attributes acts as segmentation
9. **Use SearchStream for large results** — Search is paginated, SearchStream streams all results

## Quick Examples

**Campaign performance last 30 days:**
```sql
SELECT campaign.id, campaign.name, campaign.status,
  metrics.impressions, metrics.clicks, metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

**Keywords with low quality score:**
```sql
SELECT ad_group_criterion.keyword.text,
  ad_group_criterion.quality_info.quality_score,
  metrics.impressions, metrics.clicks
FROM keyword_view
WHERE ad_group_criterion.quality_info.quality_score < 5
  AND segments.date DURING LAST_30_DAYS
```

**Search terms report:**
```sql
SELECT search_term_view.search_term,
  segments.keyword.info.match_type,
  campaign.name, ad_group.name,
  metrics.clicks, metrics.impressions, metrics.cost_micros
FROM search_term_view
WHERE segments.date DURING LAST_7_DAYS
```

**Case-insensitive campaign name search:**
```sql
SELECT campaign.id, campaign.name
FROM campaign
WHERE campaign.name REGEXP_MATCH "(?i).*brand.*"
```

For ready-made queries that replicate Google Ads UI screens, see [references/cookbook.md](references/cookbook.md).
