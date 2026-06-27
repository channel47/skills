# Kit V4 API Reference

Quick reference for the Kit (formerly ConvertKit) V4 REST API. Use this when you need exact endpoint details, field names, or response shapes beyond what SKILL.md covers.

## Authentication

All requests require the `X-Kit-Api-Key` header. The key is generated in Kit > Settings > Developer.

```
X-Kit-Api-Key: your-api-key-here
```

Rate limit: **120 requests per rolling 60 seconds** for API key auth.

## Base URL

```
https://api.kit.com/v4
```

## Pagination

Cursor-based. Response includes a `pagination` object:

```json
{
  "pagination": {
    "has_previous_page": false,
    "has_next_page": true,
    "start_cursor": "abc123",
    "end_cursor": "xyz789",
    "per_page": 50
  }
}
```

Query params: `after` (cursor), `before` (cursor), `per_page` (1-500, default varies).

## Endpoints

### Account

| Method | Path | Description |
|--------|------|-------------|
| GET | `/account` | Current account info (name, plan, email) |

### Subscribers

| Method | Path | Description |
|--------|------|-------------|
| GET | `/subscribers` | List subscribers. Filterable by `email_address`, `state`, `created_after`, `created_before`, `updated_after`, `updated_before`, `sort_field`, `sort_order` |
| GET | `/subscribers/:id` | Get single subscriber |
| POST | `/subscribers` | Create or update (upsert by email). Body: `email_address` (required), `first_name`, `state`, `fields` |
| PUT | `/subscribers/:id` | Update subscriber |
| GET | `/subscribers/:id/tags` | List subscriber's tags |

**Subscriber states:** `active`, `inactive`, `bounced`, `complained`, `cancelled`

**Upsert behavior:** If a subscriber with the email already exists, their `first_name` is updated. No duplicate is created.

### Tags

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tags` | List all tags |
| GET | `/tags/:id` | Get tag details |
| POST | `/tags` | Create tag. Body: `name` |
| PUT | `/tags/:id` | Update tag name |
| DELETE | `/tags/:id` | Delete tag |
| GET | `/tags/:id/subscribers` | List subscribers with tag |
| POST | `/tags/:id/subscribers` | Tag a subscriber. Body: `email_address` |
| DELETE | `/tags/:tag_id/subscribers/:subscriber_id` | Remove tag from subscriber |

### Broadcasts

| Method | Path | Description |
|--------|------|-------------|
| GET | `/broadcasts` | List broadcasts |
| GET | `/broadcasts/:id` | Get broadcast details |
| POST | `/broadcasts` | Create broadcast |
| PUT | `/broadcasts/:id` | Update draft broadcast |
| DELETE | `/broadcasts/:id` | Delete draft broadcast |
| GET | `/broadcasts/:id/stats` | Get send stats |

**Create broadcast body fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `content` | string (HTML) | Yes | Email body content |
| `subject` | string | Yes | Email subject line |
| `description` | string | No | Internal description |
| `public` | boolean | No | If true, creates a web-viewable version |
| `published_at` | ISO 8601 | No | Web publish date |
| `preview_text` | string | No | Email preview/preheader text |
| `send_at` | ISO 8601 | No | Schedule send time. If null → creates as draft |
| `email_template_id` | integer | No | Which template to wrap content in |
| `subscriber_filter` | object | No | Filter which subscribers receive it |
| `email_address` | string | No | From address override |
| `thumbnail_url` | string | No | Thumbnail for web version |
| `thumbnail_alt` | string | No | Alt text for thumbnail |

**Safety:** Broadcasts are created as **drafts** by default. They are NOT sent unless `send_at` is explicitly set. This is safe for automation.

### Sequences (Automations)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/sequences` | List sequences |
| GET | `/sequences/:id` | Get sequence details |
| POST | `/sequences/:id/subscribers` | Add subscriber to sequence. Body: `email_address` |

### Forms & Landing Pages

| Method | Path | Description |
|--------|------|-------------|
| GET | `/forms` | List all forms and landing pages |
| GET | `/forms/:id` | Get form details |
| POST | `/forms/:id/subscribers` | Add subscriber via form. Body: `email_address`, `first_name` |

### Custom Fields

| Method | Path | Description |
|--------|------|-------------|
| GET | `/custom_fields` | List custom fields |
| POST | `/custom_fields` | Create field. Body: `label` |
| PUT | `/custom_fields/:id` | Update field |
| DELETE | `/custom_fields/:id` | Delete field |

### Email Templates

| Method | Path | Description |
|--------|------|-------------|
| GET | `/email_templates` | List email templates |

### Webhooks

| Method | Path | Description |
|--------|------|-------------|
| GET | `/webhooks` | List webhooks |
| POST | `/webhooks` | Create webhook. Body: `target_url`, `event` |
| DELETE | `/webhooks/:id` | Delete webhook |

**Webhook events:** `subscriber.subscriber_activate`, `subscriber.subscriber_unsubscribe`, `subscriber.subscriber_bounce`, `subscriber.subscriber_complain`, `subscriber.form_subscribe`, `subscriber.course_subscribe`, `subscriber.course_complete`, `subscriber.link_click`, `subscriber.product_purchase`, `subscriber.tag_add`, `subscriber.tag_remove`

### Segments

| Method | Path | Description |
|--------|------|-------------|
| GET | `/segments` | List segments |
| GET | `/segments/:id` | Get segment details |

### Purchases

| Method | Path | Description |
|--------|------|-------------|
| GET | `/purchases` | List purchases |
| GET | `/purchases/:id` | Get purchase details |
| POST | `/purchases` | Create purchase |

## Error Responses

Errors return JSON with status code and message:

```json
{
  "errors": ["The resource you were looking for could not be found"]
}
```

Common codes: `401` (bad API key), `404` (not found), `422` (validation error), `429` (rate limited).
