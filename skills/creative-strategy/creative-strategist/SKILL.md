---
name: creative-strategist
description: Turn sourced customer language into structured creative strategy — voice-of-customer research, buyer personas, ranked ad angles, and an advertorial draft, accumulating in one per-product dossier. Use when the user wants to research what customers say about a product or category (pull reviews, Reddit threads, VOC, pain points, complaints), build buyer personas or customer avatars, find ad angles, hooks, or creative concepts, write an advertorial, presell, editorial, or listicle landing page, or run the creative strategy pipeline end to end.
---

# Creative Strategist

Four stages, each feeding the next. Load only the stage file(s) needed from `references/`:

| User wants | Load | Prereq |
|---|---|---|
| Customer research, reviews, VOC | `research.md` | — |
| Personas, customer avatars | `personas.md` | research |
| Ad angles, hooks, concepts | `angles.md` | personas |
| Advertorial, presell page | `advertorial.md` | angles |

Competitor ad intelligence lives in the separate `ad-recon` skill — it writes `## Stage: Ad Recon` to the same dossier and feeds the angles differentiation gate.

Full pipeline = all four in sequence. If a prerequisite section is missing from the dossier, offer to run that stage first — or accept equivalent context from the user and note the thinner foundation.

When the client supports isolated subagents, run research in one using the
contents of `research.md` and `sources.md`, plus the target and dossier path.
Otherwise run the stage directly and write only the required evidence and
synthesis to the dossier.

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

Check `brand/context.md` for product context; if the target is still unclear, ask for product or category, known competitors, and open questions — or suggest running `brief-me` first. After each stage, brief the user in 3-5 lines (headline findings, biggest gap, suggested next stage) — don't dump the file.
