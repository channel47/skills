# channel47 Skills

Agentic marketing systems for Claude Code and SKILL.md-compatible agents.

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
| [creative-strategist](skills/creative-strategy/creative-strategist) | Run the research -> personas -> angles pipeline end to end |
| [customer-research](skills/creative-strategy/customer-research) | Pull voice-of-customer research from public reviews, Reddit, forums, and articles |
| [persona-builder](skills/creative-strategy/persona-builder) | Turn research into behavior-based personas and anti-personas |
| [angle-generator](skills/creative-strategy/angle-generator) | Generate ranked ad angles, hooks, variants, and a testing roadmap |
| [advertorial-builder](skills/creative-strategy/advertorial-builder) | Turn a winning angle into a build-ready editorial pre-sell page |

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

## Agent Ops

| Skill | What it does |
|-------|-------------|
| [prompt-optimizer](skills/agent-ops/prompt-optimizer) | Transform rough prompts into best-practice format |

## System Map

The flagship Channel47 workflow is:

```
customer-research -> persona-builder -> angle-generator -> advertorial-builder
                                      \-> media-buyer + MCP connectors
```

The standalone skills are the public, agent-discoverable surface. The MCP connectors live in [`channel47/mcps`](https://github.com/channel47/mcps). Older Claude Code plugin packaging lives in [`channel47/plugins`](https://github.com/channel47/plugins) for history and compatibility.

## Compatible with

Claude Code, Cursor, Cline, Windsurf, Codex CLI, and any tool that reads `SKILL.md` files. The repo is structured for the Vercel `skills` CLI and public discovery through [skills.sh](https://skills.sh).

## By [channel47](https://channel47.dev)
