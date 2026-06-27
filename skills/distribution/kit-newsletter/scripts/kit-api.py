#!/usr/bin/env python3
"""
Kit V4 API Helper — Lightweight CLI for Kit (ConvertKit) operations.

Usage:
    python3 kit-api.py <command> [options]

Environment:
    KIT_API_KEY — Required. Your Kit API key (Settings > Developer in Kit).

Commands:
    account                         Show account info
    subscribers list [--page N] [--tag TAG_ID]  List subscribers (optionally filtered by tag)
    subscribers get <id>            Get subscriber by ID
    subscribers create <email> [--name NAME] [--tags TAG1,TAG2]
    subscribers search <email>      Find subscriber by email
    subscribers tag <id> <tag_id>   Tag a subscriber
    subscribers untag <id> <tag_id> Remove tag from subscriber
    tags list                       List all tags
    tags create <name>              Create a tag
    broadcasts list [--page N]      List broadcasts
    broadcasts get <id>             Get broadcast details
    broadcasts create --subject S --content HTML [--preview TEXT] [--public] [--send-at ISO]
    broadcasts update <id> [--subject S] [--content HTML] [--preview TEXT]
    broadcasts delete <id>          Delete a draft broadcast
    broadcasts stats <id>           Get broadcast stats
    forms list                      List all forms
    sequences list                  List all sequences
    sequences subscribe <seq_id> <email>  Add subscriber to sequence
    custom-fields list              List custom fields
    custom-fields create <label>    Create a custom field
    templates list                  List email templates
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Optional

BASE_URL = "https://api.kit.com/v4"
PER_PAGE = 50


def get_api_key() -> str:
    key = os.environ.get("KIT_API_KEY", "").strip()
    if not key:
        print("Error: KIT_API_KEY environment variable is not set.", file=sys.stderr)
        print("Set it with: export KIT_API_KEY='your-api-key'", file=sys.stderr)
        print("Find your key at: Kit > Settings > Developer", file=sys.stderr)
        sys.exit(1)
    return key


def api_request(
    method: str,
    path: str,
    data: Optional[dict] = None,
    params: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Kit V4 API."""
    api_key = get_api_key()

    url = f"{BASE_URL}{path}"
    if params:
        # Filter out None values
        filtered = {k: v for k, v in params.items() if v is not None}
        if filtered:
            url += "?" + urllib.parse.urlencode(filtered)

    headers = {
        "X-Kit-Api-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    body = json.dumps(data).encode("utf-8") if data else None

    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            if not raw:
                return {}
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        try:
            error_json = json.loads(error_body)
            print(f"API Error {e.code}: {json.dumps(error_json, indent=2)}", file=sys.stderr)
        except json.JSONDecodeError:
            print(f"API Error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def pp(data: Any) -> None:
    """Pretty-print JSON output."""
    print(json.dumps(data, indent=2, default=str))


# ── Account ──────────────────────────────────────────────────────────────────

def cmd_account():
    pp(api_request("GET", "/account"))


# ── Subscribers ──────────────────────────────────────────────────────────────

def cmd_subscribers_list(page: Optional[str] = None, tag: Optional[str] = None):
    params = {"per_page": PER_PAGE}
    if page:
        params["after"] = page

    if tag:
        # Fetch subscribers via the tag endpoint: GET /tags/{id}/subscribers
        result = api_request("GET", f"/tags/{tag}/subscribers", params=params)
    else:
        result = api_request("GET", "/subscribers", params=params)
    subscribers = result.get("subscribers", [])
    pagination = result.get("pagination", {})

    for s in subscribers:
        tags = ", ".join(t.get("name", "") for t in s.get("tags", []))
        state = s.get("state", "?")
        print(f"  [{s['id']}] {s.get('email_address', '?')} — {s.get('first_name', '')} ({state}){' [' + tags + ']' if tags else ''}")

    print(f"\n  Showing {len(subscribers)} subscribers")
    if pagination.get("has_next_page"):
        cursor = pagination.get("end_cursor", "")
        print(f"  Next page: --page {cursor}")


def cmd_subscribers_get(subscriber_id: str):
    pp(api_request("GET", f"/subscribers/{subscriber_id}"))


def cmd_subscribers_create(email: str, name: Optional[str] = None, tags: Optional[str] = None):
    data: dict = {"email_address": email}
    if name:
        data["first_name"] = name

    result = api_request("POST", "/subscribers", data=data)
    sub = result.get("subscriber", result)
    print(f"  Subscriber: {sub.get('email_address')} (ID: {sub.get('id')}, state: {sub.get('state')})")

    # Tag the subscriber if tags were provided
    if tags and sub.get("id"):
        tag_names = [t.strip() for t in tags.split(",") if t.strip()]
        if tag_names:
            # Get all tags to find IDs
            all_tags = api_request("GET", "/tags", params={"per_page": 500}).get("tags", [])
            tag_map = {t["name"].lower(): t["id"] for t in all_tags}

            for tag_name in tag_names:
                tag_id = tag_map.get(tag_name.lower())
                if tag_id:
                    api_request("POST", f"/tags/{tag_id}/subscribers", data={"email_address": email})
                    print(f"  Tagged with: {tag_name}")
                else:
                    print(f"  Warning: Tag '{tag_name}' not found — skipping", file=sys.stderr)


def cmd_subscribers_search(email: str):
    # Kit V4 doesn't have a direct search-by-email — list with filtering
    # The best approach is to use the subscribers endpoint with email filter
    params = {"email_address": email, "per_page": 1}
    result = api_request("GET", "/subscribers", params=params)
    subscribers = result.get("subscribers", [])
    if subscribers:
        pp(subscribers[0])
    else:
        print(f"  No subscriber found with email: {email}")


def cmd_subscribers_tag(subscriber_id: str, tag_id: str):
    # Get subscriber email first
    sub = api_request("GET", f"/subscribers/{subscriber_id}").get("subscriber", {})
    email = sub.get("email_address")
    if not email:
        print(f"  Error: Could not find subscriber {subscriber_id}", file=sys.stderr)
        sys.exit(1)
    api_request("POST", f"/tags/{tag_id}/subscribers", data={"email_address": email})
    print(f"  Tagged subscriber {subscriber_id} with tag {tag_id}")


def cmd_subscribers_untag(subscriber_id: str, tag_id: str):
    api_request("DELETE", f"/tags/{tag_id}/subscribers/{subscriber_id}")
    print(f"  Removed tag {tag_id} from subscriber {subscriber_id}")


# ── Tags ─────────────────────────────────────────────────────────────────────

def cmd_tags_list():
    result = api_request("GET", "/tags", params={"per_page": 500})
    tags = result.get("tags", [])
    for t in tags:
        count = t.get("total_subscriptions", "?")
        print(f"  [{t['id']}] {t['name']} ({count} subscribers)")
    print(f"\n  {len(tags)} tags total")


def cmd_tags_create(name: str):
    result = api_request("POST", "/tags", data={"name": name})
    tag = result.get("tag", result)
    print(f"  Created tag: {tag.get('name')} (ID: {tag.get('id')})")


# ── Broadcasts ───────────────────────────────────────────────────────────────

def cmd_broadcasts_list(page: Optional[str] = None):
    params = {"per_page": PER_PAGE}
    if page:
        params["after"] = page
    result = api_request("GET", "/broadcasts", params=params)
    broadcasts = result.get("broadcasts", [])
    pagination = result.get("pagination", {})

    for b in broadcasts:
        status = "DRAFT" if not b.get("published_at") else "SENT"
        subject = b.get("subject", "(no subject)")
        created = b.get("created_at", "?")[:10]
        print(f"  [{b['id']}] [{status}] {subject} ({created})")

    print(f"\n  Showing {len(broadcasts)} broadcasts")
    if pagination.get("has_next_page"):
        cursor = pagination.get("end_cursor", "")
        print(f"  Next page: --page {cursor}")


def cmd_broadcasts_get(broadcast_id: str):
    pp(api_request("GET", f"/broadcasts/{broadcast_id}"))


def cmd_broadcasts_create(
    subject: str,
    content: str,
    preview: Optional[str] = None,
    public: bool = False,
    send_at: Optional[str] = None,
    template_id: Optional[str] = None,
):
    data: dict = {
        "subject": subject,
        "content": content,
        "public": public,
    }
    if preview:
        data["preview_text"] = preview
    if send_at:
        data["send_at"] = send_at
    if template_id:
        data["email_template_id"] = int(template_id)

    result = api_request("POST", "/broadcasts", data=data)
    b = result.get("broadcast", result)

    status = "SCHEDULED" if send_at else "DRAFT"
    print(f"  Created broadcast [{status}]: {b.get('subject')}")
    print(f"  ID: {b.get('id')}")
    if send_at:
        print(f"  Scheduled for: {send_at}")
    else:
        print(f"  Status: Draft — will NOT send until scheduled or sent manually in Kit")


def cmd_broadcasts_update(
    broadcast_id: str,
    subject: Optional[str] = None,
    content: Optional[str] = None,
    preview: Optional[str] = None,
):
    data: dict = {}
    if subject:
        data["subject"] = subject
    if content:
        data["content"] = content
    if preview:
        data["preview_text"] = preview

    if not data:
        print("  Nothing to update — provide at least one of --subject, --content, --preview")
        return

    result = api_request("PUT", f"/broadcasts/{broadcast_id}", data=data)
    b = result.get("broadcast", result)
    print(f"  Updated broadcast: {b.get('subject')} (ID: {b.get('id')})")


def cmd_broadcasts_delete(broadcast_id: str):
    api_request("DELETE", f"/broadcasts/{broadcast_id}")
    print(f"  Deleted broadcast {broadcast_id}")


def cmd_broadcasts_stats(broadcast_id: str):
    result = api_request("GET", f"/broadcasts/{broadcast_id}/stats")
    pp(result)


# ── Forms ────────────────────────────────────────────────────────────────────

def cmd_forms_list():
    result = api_request("GET", "/forms", params={"per_page": 500})
    forms = result.get("forms", [])
    for f in forms:
        ftype = f.get("type", "?")
        print(f"  [{f['id']}] {f.get('name', '?')} ({ftype})")
    print(f"\n  {len(forms)} forms total")


# ── Sequences ────────────────────────────────────────────────────────────────

def cmd_sequences_list():
    result = api_request("GET", "/sequences", params={"per_page": 500})
    sequences = result.get("sequences", [])
    for s in sequences:
        state = s.get("state", "?")
        print(f"  [{s['id']}] {s.get('name', '?')} ({state})")
    print(f"\n  {len(sequences)} sequences total")


def cmd_sequences_subscribe(sequence_id: str, email: str):
    result = api_request("POST", f"/sequences/{sequence_id}/subscribers", data={"email_address": email})
    print(f"  Added {email} to sequence {sequence_id}")


# ── Custom Fields ────────────────────────────────────────────────────────────

def cmd_custom_fields_list():
    result = api_request("GET", "/custom_fields", params={"per_page": 500})
    fields = result.get("custom_fields", [])
    for f in fields:
        print(f"  [{f.get('id')}] {f.get('label', '?')} (key: {f.get('key', '?')})")
    print(f"\n  {len(fields)} custom fields total")


def cmd_custom_fields_create(label: str):
    result = api_request("POST", "/custom_fields", data={"label": label})
    field = result.get("custom_field", result)
    print(f"  Created field: {field.get('label')} (key: {field.get('key')}, ID: {field.get('id')})")


# ── Email Templates ──────────────────────────────────────────────────────────

def cmd_templates_list():
    result = api_request("GET", "/email_templates", params={"per_page": 500})
    templates = result.get("email_templates", [])
    for t in templates:
        print(f"  [{t.get('id')}] {t.get('name', '?')}")
    print(f"\n  {len(templates)} templates total")


# ── CLI Argument Parser ──────────────────────────────────────────────────────

def parse_flag(args: list, flag: str, has_value: bool = True) -> Optional[str]:
    """Extract a --flag value from args list, mutating args in place."""
    for i, arg in enumerate(args):
        if arg == flag:
            if has_value:
                if i + 1 < len(args):
                    val = args.pop(i + 1)
                    args.pop(i)
                    return val
                else:
                    print(f"Error: {flag} requires a value", file=sys.stderr)
                    sys.exit(1)
            else:
                args.pop(i)
                return "true"
    return None


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__)
        sys.exit(0)

    resource = args[0]
    action = args[1] if len(args) > 1 else None

    # Account
    if resource == "account":
        cmd_account()

    # Subscribers
    elif resource == "subscribers":
        if action == "list":
            page = parse_flag(args, "--page")
            tag = parse_flag(args, "--tag")
            cmd_subscribers_list(page, tag)
        elif action == "get" and len(args) > 2:
            cmd_subscribers_get(args[2])
        elif action == "create" and len(args) > 2:
            name = parse_flag(args, "--name")
            tags = parse_flag(args, "--tags")
            cmd_subscribers_create(args[2], name, tags)
        elif action == "search" and len(args) > 2:
            cmd_subscribers_search(args[2])
        elif action == "tag" and len(args) > 3:
            cmd_subscribers_tag(args[2], args[3])
        elif action == "untag" and len(args) > 3:
            cmd_subscribers_untag(args[2], args[3])
        else:
            print("Usage: subscribers {list|get|create|search|tag|untag} ...", file=sys.stderr)
            sys.exit(1)

    # Tags
    elif resource == "tags":
        if action == "list":
            cmd_tags_list()
        elif action == "create" and len(args) > 2:
            cmd_tags_create(args[2])
        else:
            print("Usage: tags {list|create} ...", file=sys.stderr)
            sys.exit(1)

    # Broadcasts
    elif resource == "broadcasts":
        if action == "list":
            page = parse_flag(args, "--page")
            cmd_broadcasts_list(page)
        elif action == "get" and len(args) > 2:
            cmd_broadcasts_get(args[2])
        elif action == "create":
            subject = parse_flag(args, "--subject")
            content = parse_flag(args, "--content")
            preview = parse_flag(args, "--preview")
            public = parse_flag(args, "--public", has_value=False)
            send_at = parse_flag(args, "--send-at")
            template_id = parse_flag(args, "--template-id")
            if not subject or not content:
                print("Error: --subject and --content are required for broadcast create", file=sys.stderr)
                sys.exit(1)
            cmd_broadcasts_create(subject, content, preview, public == "true", send_at, template_id)
        elif action == "update" and len(args) > 2:
            bid = args[2]
            subject = parse_flag(args, "--subject")
            content = parse_flag(args, "--content")
            preview = parse_flag(args, "--preview")
            cmd_broadcasts_update(bid, subject, content, preview)
        elif action == "delete" and len(args) > 2:
            cmd_broadcasts_delete(args[2])
        elif action == "stats" and len(args) > 2:
            cmd_broadcasts_stats(args[2])
        else:
            print("Usage: broadcasts {list|get|create|update|delete|stats} ...", file=sys.stderr)
            sys.exit(1)

    # Forms
    elif resource == "forms":
        if action == "list":
            cmd_forms_list()
        else:
            print("Usage: forms list", file=sys.stderr)
            sys.exit(1)

    # Sequences
    elif resource == "sequences":
        if action == "list":
            cmd_sequences_list()
        elif action == "subscribe" and len(args) > 3:
            cmd_sequences_subscribe(args[2], args[3])
        else:
            print("Usage: sequences {list|subscribe} ...", file=sys.stderr)
            sys.exit(1)

    # Custom Fields
    elif resource == "custom-fields":
        if action == "list":
            cmd_custom_fields_list()
        elif action == "create" and len(args) > 2:
            cmd_custom_fields_create(args[2])
        else:
            print("Usage: custom-fields {list|create} ...", file=sys.stderr)
            sys.exit(1)

    # Email Templates
    elif resource == "templates":
        if action == "list":
            cmd_templates_list()
        else:
            print("Usage: templates list", file=sys.stderr)
            sys.exit(1)

    else:
        print(f"Unknown command: {resource}", file=sys.stderr)
        print("Run with --help to see available commands", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
