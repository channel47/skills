# Content Mining

Turn your recent work into distributable content. Pulls from your work artifacts (git history, PRs), notes, chat history, and completed tasks to find the highest-signal material, then packages it for X, LinkedIn, Newsletter, and GitHub.

Not a content calendar. A mining operation.

## Install

```bash
npx skills add channel47/skills --skill content-miner
```

## What it does

1. **Gathers** the last 7–14 days from every available source (git history, notes, chats, tasks)
2. **Extracts** the highest-signal nuggets using five filters (provenance, specificity, replaceability, tension, "so what")
3. **Classifies** each nugget by type (build log, tool report, contrarian take, process note, shipping update, receipts)
4. **Packages** channel-specific drafts matched to where the content works best
5. **Presents** a ranked brief with top picks, secondary ideas, and a parking lot

## Trigger phrases

- "content mine"
- "what should I post"
- "mine my week"
- "anything worth posting"
- "find me content"
- "what's shareable"
- "show the work"

## Channels

| Channel | What works there |
|---------|-----------------|
| **X (post)** | Sharp single observations, receipts, contrarian takes |
| **X (thread)** | Compressed build logs, step-by-step process notes |
| **LinkedIn** | Same voice + more context. Observations, proof-point narratives |
| **Newsletter** | Full depth. One topic. Build logs, process notes, tool reports |
| **GitHub** | Shipping updates, skill releases, code artifacts |

## Pairs well with

- A brand voice skill or style guide (loaded first, applied to all drafts)
- [`creative-strategist`](../../creative-strategy/creative-strategist) (a finished dossier is high-signal mining material)
- [`twitter-algorithm-optimizer`](../twitter-algorithm-optimizer) (optimize the X drafts before posting)

## Fast mode

Say "just post something" and it skips the full workflow. Pulls 3 days, finds the single most concrete thing, drafts one X post and one LinkedIn post. Done.

## License

MIT
