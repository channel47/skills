---
name: make-static-ads
description: Develop, generate, adapt, QA, and package production-ready static advertising creatives. Use for brand-agnostic paid-social concept generation, approved-concept production, existing-creative refinement, multi-aspect-ratio adaptation, product-faithful image generation, creative testing portfolios, or final media-buyer asset delivery. Supports concept-only work and full raster production, but not video generation.
---

# Make Static Ads

Create strategically distinct static ad concepts, produce ambitious image-led pilots, obtain human direction approval, then finish adaptive platform assets and a clean campaign package.

## Choose the entry point

Start at the earliest stage the request requires:

1. **Ideation** — no concepts are approved.
2. **Production** — concepts or briefs are approved.
3. **Adaptation** — an existing creative needs refinement, resizing, or variants.

Do not repeat completed stages. A request for concepts does not authorize image generation unless production is also clearly requested.

## Establish the production contract

Inspect supplied files, URLs, workspace context, brand materials, product references, landing pages, claims sources, and prior creative before asking questions.

Infer safe defaults. Ask one question at a time only when an answer would materially alter strategy or production. Summarize the contract before expensive generation when ambiguity remains:

- campaign objective and desired action;
- audience and awareness level;
- offer or destination;
- approved evidence and prohibited claims;
- visual authority and product references;
- test variable;
- requested concepts and placements;
- output location.

Default output location:

1. `<current-workspace>/output/static-ads/<campaign-name>/`
2. `~/Downloads/<campaign-name>/` when no writable workspace exists.

For a URL-only request, browse the destination and autonomously extract the offer, product, audience hypothesis, approved-looking evidence, visual language, and desired action. Treat unsupported audience assumptions as hypotheses and never promote page copy into an approved quantitative claim without checking its authority. Continue through concepting and one or two pilots, then pause at the normal approval gate.

## Protect truth and test integrity

Treat supplied prices, discounts, reviews, guarantees, durations, gifts, claims, product details, and fulfillment behavior as fixed evidence. Never invent or improve them. If no approved claims source exists, use qualitative benefit language and flag quantitative copy before production.

Identify the experiment:

- Offer or landing-page test: keep creative identical and change only destination assignment.
- Creative test: keep offer, audience, placement, and destination consistent.
- Format adaptation: preserve the concept and message while recomposing responsively.
- Exploration: allow broader variation and record differences in the manifest.

## Concept strategically

When ideation is required, read [references/concepting.md](references/concepting.md). Generate strategically orthogonal concepts rather than headline swaps. Stop when the portfolio has sufficient diversity and testability, usually 6–10 strong concepts. Expand only the best 3–5 into production briefs.

Each production brief must define:

- strategic angle and hook;
- concrete composition;
- copy mode and exact on-image copy, or explicitly **none**;
- CTA treatment: on-image, platform button, caption, or none;
- expected reason to earn attention or clicks;
- fidelity, claims, or production risks.

## Choose the image engine

Prefer native Imagegen and follow its installed skill completely.

If native Imagegen is unavailable:

1. Discover supported image-generation tools.
2. Use only a model in the capability class of GPT Image 2, Nano Banana 2, or better.
3. Preserve the same inspection and approval workflow.
4. Stop and explain the limitation if no sufficiently capable model is available. Do not quietly downgrade quality.

Favor ambitious generative composition. Do not default to a collage or manually composited layout. Use deterministic editing only for precision corrections such as:

- pixel-dimension normalization when the generated aspect ratio and composition already match;
- a localized typo or malformed glyph without replacing the headline, CTA, or typographic system;
- authentic logo replacement;
- product-faithful packshot correction;
- artifact removal;
- a small safe-zone adjustment that does not rebuild the hierarchy.

The image model must generate the complete creative: scene, composition, and every visual or textual element required by the approved brief. A complete creative may be copy-free, lightly labeled, or type-led. Do not force a headline or on-image CTA into a concept that works better through imagery, a platform CTA button, or caption copy.

When the brief requires on-image typography, generate it as part of the native composition. Do not use the image model merely to generate background scenes that are later turned into ads through overlays.

Never:

- accept the wrong aspect ratio and crop it into compliance;
- redraw or overlay the complete required headline, subhead, CTA, cards, frame, or primary hierarchy;
- describe a composited output as native generation;
- deliver an undirected scene study, moodboard, or reference crop as a finished pilot.

If the canvas, composition, or any brief-required element materially fails, regenerate or use a capable generative image-edit operation. If repeated capable-model attempts still cannot produce the approved creative, disclose the limitation and request permission before using substantial deterministic typography or compositing.

## Preserve product fidelity

Product presence is optional in prospecting creative. Do not add packaging merely to satisfy a template.

When a product appears:

- locate or request trustworthy reference images first;
- hold logo, geometry, color, packaging, and recognizable details fixed;
- allow generated story and action imagery around those fixed commerce elements;
- reject or regenerate material product alteration;
- avoid unsupported microcopy or claims on generated packaging.

## Generate pilots, then pause

Generate one representative pilot when the direction is straightforward. Generate two materially different pilots when visual or strategic uncertainty remains.

A valid pilot is one complete, near-production ad in its requested ratio—not raw scene material. It must include every element the approved brief calls for, integrated into the native composition at feed-readable scale. Copy-free and platform-CTA-led ads are valid when intentional. It must also pass product-fidelity, claims, artifact, and hierarchy review.

When presenting two pilots, deliver two separate complete ad files. Do not combine them into a single comparison image unless a separate review sheet is also helpful.

Inspect and repair obvious failures before presenting them. State whether each pilot was generated natively and disclose any deterministic correction. Then pause for explicit human approval. Do not batch-produce remaining concepts or ratios until the user says **generate all** or gives equivalent clear approval.

## Produce adaptive formats

Unless placements override them, use:

- 4:5 — 1080×1350
- 1:1 — 1080×1080
- 9:16 — 1080×1920
- 1.91:1 — 1200×628

Recompose each format for its placement. Do not merely crop, stack, stretch, or widen the master. Preserve the concept, hook, exact message, visual authority, and product fidelity while allowing hierarchy and secondary detail to adapt.

For detailed generation, typography, safe-zone, and QA guidance, read [references/production.md](references/production.md).

## Self-correct before escalation

Automatically inspect and regenerate or repair:

- wrong canvas or aspect ratio;
- missing brief-required elements;
- anatomy or spatial artifacts;
- altered product or logo;
- incorrect or illegible text;
- unsupported claims;
- weak hierarchy;
- unsafe crops;
- stretched adaptations;
- results materially below the approved pilot.

Return to the user only when correction would require changing the concept, copy, product treatment, evidence, or strategy.

## Package the campaign

Use deterministic filenames:

`<concept-id>__<ratio>__<width>x<height>.<ext>`

Example:

`c01-cleaning-cabinet__4x5__1080x1350.png`

Package:

```text
campaign-name/
├── assets/
│   ├── c01-concept-name/
│   │   └── finished ratio files
│   └── ...
├── review/
│   ├── all-concepts__<ratio>.jpg
│   └── all-formats.jpg
├── campaign.json
└── manifest.csv
```

Keep `campaign.json` only when it records useful campaign metadata for the manifest. Do not retain rejected generations, intermediate sources, prompts, or duplicate upload folders unless requested.

Run:

```bash
python3 scripts/package_campaign.py <campaign-directory>
```

The packager verifies names and exact dimensions, builds review sheets when ImageMagick is available, creates `manifest.csv`, and writes a verified ZIP beside the campaign directory.

Deliver:

- a direct clickable ZIP file link, never only a directory link;
- one contact-sheet preview;
- a short summary of concept count, formats, assumptions, and caveats.

## Exclude video

Static raster creative is the production boundary. You may identify motion potential or draft a storyboard when requested, but do not generate video under this skill.
