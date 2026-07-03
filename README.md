# channel47 Skills

Agentic marketing systems for Claude Code and SKILL.md-compatible agents.

**Flagship — [`creative-strategist`](skills/creative-strategy/creative-strategist):** real customer language → buyer personas → ranked ad angles → build-ready advertorial, accumulating in one per-product dossier where every claim cites the customer quote it stands on. **[See a sample dossier →](examples/hushhound-dossier.md)**

```
npx skills add channel47/skills --skill creative-strategist
```

Marketers do not need more AI tips. They need systems they can run: research pipelines, creative strategy workflows, advertorial builders, paid media operators, and distribution tools that install cleanly into the agents they already use.

## Install

All skills:

```
npx skills add channel47/skills
```

Single skill:

```
npx skills add channel47/skills --skill creative-strategist
```

List available skills:

```
npx skills add channel47/skills --list
```

Or copy a skill folder to your agent's skills directory manually.

## Creative Strategy

| Skill | What it does |
|-------|-------------|
| [brief-me](skills/creative-strategy/brief-me) | Discovery interview that grills you about brand, offer, and audience, then writes the shared brand context file other skills read |
| [creative-strategist](skills/creative-strategy/creative-strategist) | Voice-of-customer research -> personas -> ad angles -> advertorial, as one pipeline or stage by stage |

## Paid Media

| Skill | What it does |
|-------|-------------|
| [media-buyer](skills/paid-media/media-buyer) | Query and operate Google Ads, Bing Ads, and Meta Ads through Channel47 MCPs |
| [gaql](skills/paid-media/gaql) | Write, debug, and validate Google Ads Query Language queries |

## Distribution

| Skill | What it does |
|-------|-------------|
| [content-miner](skills/distribution/content-miner) | Extract shareable content from recent activity |
| [kit-newsletter](skills/distribution/kit-newsletter) | Manage Kit newsletters from the CLI |
| [twitter-algorithm-optimizer](skills/distribution/twitter-algorithm-optimizer) | Optimize tweets against X's ranking algorithm |

## System Map

The flagship Channel47 workflow is the `creative-strategist` skill:

```
research -> personas -> angles -> advertorial
                      \-> media-buyer + MCP connectors
```

Each stage runs independently or in sequence, accumulating into a single per-product dossier.

The standalone skills are the public, agent-discoverable surface. The MCP connectors live in [`channel47/mcps`](https://github.com/channel47/mcps). Older Claude Code plugin packaging lives in [`channel47/plugins`](https://github.com/channel47/plugins) for history and compatibility.

## Compatible with

Claude Code, Cursor, Cline, Windsurf, Codex CLI, and any tool that reads `SKILL.md` files. The repo is structured for the Vercel `skills` CLI and public discovery through [skills.sh](https://skills.sh).

## By [channel47](https://channel47.dev)
