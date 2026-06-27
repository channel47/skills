---
name: kit-newsletter
description: "Manage Kit (ConvertKit) newsletter operations — subscribers, broadcasts, tags, sequences, and more — directly from the CLI. Use this skill whenever the user mentions Kit, ConvertKit, newsletter, email list, broadcast, subscribers, email campaign, drip sequence, or wants to create/send/manage email content through Kit. Also trigger when they say things like 'draft a newsletter', 'check my subscriber count', 'tag subscribers', 'create a broadcast', or reference any Kit-related workflow. If the user is working on email content and you know they use Kit, proactively suggest using this skill."
---

# Kit Newsletter Manager

Manage your Kit (ConvertKit) newsletter entirely from the CLI — draft broadcasts, manage subscribers, organize with tags, and monitor performance without ever opening the Kit dashboard.

## Setup

The skill requires a `KIT_API_KEY` environment variable. The user should set this once:

```bash
export KIT_API_KEY="your-api-key-here"
```

The API key is generated in **Kit > Settings > Developer**. If the key is missing, the helper script will tell the user where to find it.

## How This Skill Works

This skill bundles a lightweight Python CLI (`scripts/kit-api.py`) that wraps the Kit V4 REST API. It uses only Python stdlib — no pip installs needed. You call it via Bash and it returns human-readable output or raw JSON.

The general pattern for every operation:

```bash
python3 /path/to/kit/scripts/kit-api.py <resource> <action> [options]
```

Replace `/path/to/kit` with the actual path to this skill's directory. When Claude invokes this skill, it should use the resolved path (e.g., the path from which SKILL.md was read).

## Core Operations

### Check Account

Verify the connection is working and see account details:

```bash
python3 scripts/kit-api.py account
```

Always start here if the user hasn't used Kit in this session — it confirms auth is working.

### Broadcasts (Newsletters)

Broadcasts are Kit's term for one-off email sends (newsletters, announcements, updates).

**List recent broadcasts:**
```bash
python3 scripts/kit-api.py broadcasts list
```

**Create a draft broadcast:**
```bash
python3 scripts/kit-api.py broadcasts create \
  --subject "Your subject line" \
  --content "<p>HTML email body here</p>" \
  --preview "Preview text shown in inbox"
```

This creates a **draft** — it will NOT send until the user explicitly schedules it or sends from the Kit dashboard. This is the safe default for automation.

**Schedule a broadcast for a specific time:**
```bash
python3 scripts/kit-api.py broadcasts create \
  --subject "Weekly Update" \
  --content "<p>Content here</p>" \
  --send-at "2026-02-15T10:00:00Z"
```

When scheduling, always confirm the date/time with the user before executing. Scheduled broadcasts WILL send automatically.

**Update a draft:**
```bash
python3 scripts/kit-api.py broadcasts update <broadcast-id> \
  --subject "Updated subject" \
  --content "<p>New content</p>"
```

**Get broadcast details or stats:**
```bash
python3 scripts/kit-api.py broadcasts get <broadcast-id>
python3 scripts/kit-api.py broadcasts stats <broadcast-id>
```

**Delete a draft:**
```bash
python3 scripts/kit-api.py broadcasts delete <broadcast-id>
```

#### Writing Broadcast Content

When the user asks you to draft a newsletter or broadcast:

1. Write the HTML content first. Kit broadcasts accept HTML in the `content` field — this is the email body that gets wrapped in whatever email template the user has set up in Kit.
2. Keep the HTML simple and email-safe: `<p>`, `<h2>`, `<h3>`, `<a>`, `<strong>`, `<em>`, `<ul>`, `<li>`, `<blockquote>`, `<img>`. Avoid complex CSS, JavaScript, or div-heavy layouts — the Kit template handles the outer styling.
3. Show the user the content for review before creating the broadcast.
4. Create as a draft unless the user explicitly asks to schedule it.

For longer content, write the HTML to a temp file first and pass it via shell substitution:
```bash
python3 scripts/kit-api.py broadcasts create \
  --subject "Weekly Digest" \
  --content "$(cat /tmp/broadcast-content.html)"
```

### Subscribers

**List subscribers:**
```bash
python3 scripts/kit-api.py subscribers list
```

**Search by email:**
```bash
python3 scripts/kit-api.py subscribers search user@example.com
```

**Add a new subscriber (with optional name and tags):**
```bash
python3 scripts/kit-api.py subscribers create user@example.com --name "Jane" --tags "newsletter,vip"
```

This uses Kit's upsert behavior — if the email already exists, it updates their name rather than creating a duplicate.

**Tag or untag a subscriber:**
```bash
python3 scripts/kit-api.py subscribers tag <subscriber-id> <tag-id>
python3 scripts/kit-api.py subscribers untag <subscriber-id> <tag-id>
```

### Tags

Tags are how you segment your audience in Kit.

**List all tags:**
```bash
python3 scripts/kit-api.py tags list
```

**Create a new tag:**
```bash
python3 scripts/kit-api.py tags create "tag-name"
```

### Sequences

Sequences are Kit's automated email series (drip campaigns).

**List sequences:**
```bash
python3 scripts/kit-api.py sequences list
```

**Add someone to a sequence:**
```bash
python3 scripts/kit-api.py sequences subscribe <sequence-id> user@example.com
```

### Forms & Templates

**List forms/landing pages:**
```bash
python3 scripts/kit-api.py forms list
```

**List email templates:**
```bash
python3 scripts/kit-api.py templates list
```

Template IDs are useful when creating broadcasts — pass `--template-id` to wrap content in a specific template.

### Custom Fields

**List custom fields:**
```bash
python3 scripts/kit-api.py custom-fields list
```

**Create a custom field:**
```bash
python3 scripts/kit-api.py custom-fields create "Field Label"
```

## Important Behaviors

### Safety First
- Broadcasts are always created as **drafts** unless `--send-at` is explicitly provided.
- Before scheduling a broadcast (setting `--send-at`), always confirm the time with the user.
- Deleting broadcasts only works on drafts — you can't delete sent broadcasts.

### Rate Limiting
The Kit API allows 120 requests per rolling 60-second window. The helper script doesn't do any batching or throttling, so if you're doing bulk operations (like tagging hundreds of subscribers), space out your calls or batch the work.

### Pagination
List commands return 50 items per page by default. If there are more, the output will show a `--page` cursor value you can pass to get the next page.

### Error Handling
The helper script prints errors to stderr and exits with code 1. If you see a `401` error, the API key is wrong or expired. A `429` means rate limiting — wait a moment and retry.

## API Reference

For detailed endpoint specs, field names, and response shapes, read:

```
references/kit-v4-api.md
```

This is useful when you need to understand exact request/response formats or want to extend the helper script with additional operations.

## Resources

### scripts/
- `kit-api.py` — Core CLI helper. Zero dependencies beyond Python stdlib. Handles auth, error formatting, and pagination.

### references/
- `kit-v4-api.md` — Complete Kit V4 API endpoint reference with field types, required/optional markers, and response examples.
