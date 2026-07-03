---
name: creative-strategist
description: Turn real customer language into ads that convert — voice-of-customer research, buyer personas, ranked ad angles, and a build-ready advertorial, accumulating in one per-product dossier. Use when the user wants to research what customers say about a product or category (pull reviews, Reddit threads, VOC, pain points, complaints), build buyer personas or customer avatars, find ad angles, hooks, or creative concepts, write an advertorial, presell, editorial, or listicle landing page, or run the creative strategy pipeline end to end.
---

# Creative Strategist

Four stages, each feeding the next. Load only the stage file(s) needed from `references/`:

| User wants | Load | Prereq |
|---|---|---|
| Customer research, reviews, VOC | `research.md` | — |
| Personas, customer avatars | `personas.md` | research |
| Ad angles, hooks, concepts | `angles.md` | personas |
| Advertorial, presell page | `advertorial.md` | angles |

Full pipeline = all four in sequence. If a prerequisite section is missing from the dossier, offer to run that stage first — or accept equivalent context from the user and note the thinner foundation.

Research runs as a subagent: launch an Agent whose prompt is the contents of `research.md` + `sources.md`, plus the research target and the dossier path. This keeps the noisy crawl out of the main context.

## The dossier

All output accumulates in `creative/[product-slug]-dossier.md` — one file per product, each stage owning a `## Stage: ...` section.

**Traceability law** (the whole system rests on it):

- Every quote is verbatim, tagged, and gets a stable ID: `Q12 [🔥2 | solution-aware] "exact words" — source URL`
- Intensity: 🔥1 calm fact · 🔥2 clear emotion · 🔥3 visceral story (hook material — if over ~30% of quotes land here, recalibrate; real 🔥3 is rare)
- Journey stage: pre-aware · problem-aware · solution-aware · decision · post-purchase
- Every downstream claim — persona trait, angle, headline — cites the quote IDs it stands on
- IDs are append-only: re-runs add new quotes under fresh IDs; never renumber or reuse an ID
- When a stage re-runs, prepend `> Stale — upstream re-run [date]` to each downstream section until it is rebuilt
- Never fabricate quotes, testimonials, stats, or reviews. Thin evidence → label the output speculative and say what's missing.

## Working style

Check `brand/context.md` (the brief-me brand dossier) and `.claude/creative-strategist.local.md` for product context; if the target is still unclear, ask for product or category, known competitors, and open questions — or suggest running `brief-me` first. After each stage, brief the user in 3-5 lines (headline findings, biggest gap, suggested next stage) — don't dump the file.
