# channel47 Skills

Marketing systems for Claude Code and agentic workflows. Marketers do not need more AI tips; they need systems they can run.

## Install

All skills:

```
npx skills add channel47/skills
```

Single skill:

```
npx skills add channel47/skills --skill gaql
```

Or copy a skill folder to `~/.claude/skills/` manually.

## Skills

| Skill | What it does |
|-------|-------------|
| [creative-strategist](skills/creative-strategist) | Run the full research -> personas -> angles pipeline |
| [customer-research](skills/customer-research) | Pull voice-of-customer research from public reviews, Reddit, forums, and articles |
| [persona-builder](skills/persona-builder) | Turn research into behavior-based personas and anti-personas |
| [angle-generator](skills/angle-generator) | Generate ranked ad angles, hooks, variants, and a testing roadmap |
| [advertorial-builder](skills/advertorial-builder) | Turn a winning angle into a build-ready editorial pre-sell page |
| [media-buyer](skills/media-buyer) | Query and operate Google Ads, Bing Ads, and Meta Ads through Channel47 MCPs |
| [gaql](skills/gaql) | Write, debug, and validate Google Ads Query Language queries |
| [content-miner](skills/content-miner) | Extract shareable content from recent activity |
| [kit-newsletter](skills/kit-newsletter) | Manage Kit (ConvertKit) newsletters from the CLI |
| [twitter-algorithm-optimizer](skills/twitter-algorithm-optimizer) | Optimize tweets against X's ranking algorithm |
| [prompt-optimizer](skills/prompt-optimizer) | Transform rough prompts into best-practice format |

## System Map

The flagship Channel47 workflow is:

```
customer-research -> persona-builder -> angle-generator -> advertorial-builder
                                      \-> media-buyer + MCP connectors
```

The standalone skills are the public, agent-discoverable surface. Older Claude Code plugin packaging lives in [`channel47/plugins`](https://github.com/channel47/plugins) for history and compatibility.

## Compatible with

Claude Code, Cursor, Cline, Windsurf, Codex CLI, and any tool that reads SKILL.md files.

## By [channel47](https://channel47.dev)
