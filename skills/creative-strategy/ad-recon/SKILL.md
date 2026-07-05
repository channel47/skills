---
name: ad-recon
description: Pull the ads competitors are actually running from public ad libraries (Meta Ad Library, Google Ads Transparency Center, TikTok, LinkedIn), classify every ad by angle, and map which creative territory is crowded vs. open. Use when the user wants competitor ad intelligence or a competitive ad teardown, asks "what ads are competitors running", wants to spy on a brand's ads, needs the differentiation check before the angles stage of creative-strategist, or says "ad recon".
---

# Ad Recon

Find out what the competition is actually spending money on. Targets come from the competitor map in `brand/context.md` or the dossier's research section; if neither exists, ask for 3-5 competitor names or domains. Then work every target through the library playbook in `references/sources.md`. Recon is a noisy crawl — when running inside a larger session, launch it as a subagent whose prompt is this file + `sources.md`, plus the target list and dossier path.

**Evidence law** (same law as the rest of the system): every ad captured gets a stable, append-only ID with verbatim copy — `A7 [competitor | platform | active since 2026-03 | video] "She barked at every delivery for 3 years. This fixed it in 12 days." — library URL`. Hooks are quoted exactly, never paraphrased; never invent or reconstruct an ad from memory. Longevity is the money signal: an ad active 90+ days, or running many near-identical variants, is paying for itself — tag it **proven**.

Classify each ad with the same eight angle categories the angles stage uses — pain-agitation · failed-solution · trigger-event · identity · social proof · discovery/mechanism · comparison · specificity — plus format and the awareness stage it targets. When the library links a landing page, follow it and note the ad→page bridge in one line (advertorial, listicle, straight PDP, quiz).

Synthesis is analysis, not inventory:

- **Saturation map** — angle category × competitor matrix, each cell crowded / present / open
- Per-competitor pattern read: dominant angle, format mix, landing-page approach, creative velocity (active ad count)
- **Proven ads** ranked by longevity, with what each one is evidence *for*
- Table stakes vs. white space: claims everyone makes vs. what no one is saying that the research supports
- 3-5 **openings**: open cells worth testing, each tied to research quote IDs where a dossier exists — an opening nobody runs may be an opportunity or a graveyard; say which and why
- Coverage log: platform / access method / ad count per competitor

Write `## Stage: Ad Recon` to `creative/[product-slug]-dossier.md` (create the file if none exists) — append-only IDs and staleness rules as everywhere else. Brief the user in 3-5 lines: coverage, most saturated angle, sharpest opening, and the longest-running competitor ad with its hook.
