---
name: ad-recon
description: Collect competitor ads from public ad libraries (Meta Ad Library, Google Ads Transparency Center, TikTok, LinkedIn), classify captured ads by angle, and map what appears frequently or was not observed in sampled coverage. Use when the user wants competitor ad intelligence or a competitive ad teardown, asks "what ads are competitors running", needs the differentiation check before the angles stage of creative-strategist, or says "ad recon".
---

# Ad Recon

Collect what competitors are publishing in supported public ad libraries. Targets come from the competitor map in `brand/context.md` or the dossier's research section; if neither exists, ask for 3-5 competitor names or domains. Then work every target through the library playbook in `references/sources.md`. When the client supports isolated subagents, run the crawl in one using this file and `sources.md`, plus the target list and dossier path. Otherwise run the workflow directly and keep only the captured evidence and synthesis in the dossier.

**Evidence law** (same law as the rest of the system): every ad captured gets a stable, append-only ID with verbatim copy — `A7 [competitor | platform | active since YYYY-MM | format] "[verbatim hook]" — library URL`. Hooks are quoted exactly, never paraphrased; never invent or reconstruct an ad from memory. Treat longevity and repeated variants as persistence signals, not proof of spend, profitability, or performance.

Classify each ad with the same eight angle categories the angles stage uses — pain-agitation · failed-solution · trigger-event · identity · social proof · discovery/mechanism · comparison · specificity — plus format and the awareness stage it targets. When the library links a landing page, follow it and note the ad→page bridge in one line (advertorial, listicle, straight PDP, quiz).

Synthesis is analysis, not inventory:

- **Coverage map** — angle category × competitor matrix, each cell frequent /
  present / not observed in sampled coverage
- Per-competitor pattern read: dominant angle, format mix, landing-page
  approach, and observed active inventory
- **Long-running ads** ranked by observed longevity, with the limits of what
  that observation can establish
- Observed patterns vs. candidate gaps: claims frequent in the sampled coverage
  vs. evidence-supported claims not observed in that sample
- 3-5 **candidate openings**: angles not observed in the sampled coverage, each
  tied to research quote IDs where a dossier exists and labeled with the
  coverage limits
- Coverage log: platform / access method / ad count per competitor

Write `## Stage: Ad Recon` to `creative/[product-slug]-dossier.md` (create the file if none exists). On a rerun, preserve existing ad IDs, append newly captured ads under fresh IDs, and replace the synthesis and coverage blocks. Prepend `> Stale — Ad Recon re-run [date]` to an existing Angles or Advertorial section until it is rebuilt. Brief the user in 3-5 lines: coverage, most saturated observed angle, strongest candidate opening, and the longest-running captured ad with its hook.
