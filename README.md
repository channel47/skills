# channel47 Skills

Three installable creative-strategy skills for SKILL.md-compatible agents.

## Install

```bash
# Choose skills and target agents interactively
npx skills add channel47/skills

# Install all three skills to all detected agents
npx skills add channel47/skills --all

# One skill
npx skills add channel47/skills --skill creative-strategist

# List available skills
npx skills add channel47/skills --list
```

Or copy a skill folder to your agent's skills directory manually.

## Skills

| Skill | What it does |
|-------|-------------|
| [brief-me](skills/creative-strategy/brief-me) | Interviews the user and writes shared brand context to `brand/context.md`. |
| [ad-recon](skills/creative-strategy/ad-recon) | Collects and classifies competitor ads from public ad libraries. |
| [creative-strategist](skills/creative-strategy/creative-strategist) | Runs research, persona, angle, and advertorial stages in a product dossier. |

## Requirements

- A client that supports `SKILL.md` skills.
- File access for the shared context and dossier outputs.
- Web or browser tools when a workflow needs live research or public ad-library access.

Client behavior and available tools vary. Review each `SKILL.md` before use.
