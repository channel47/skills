# Production and QA

Use this reference during pilot generation, adaptation, and final QA.

## Build the generation prompt

Specify:

- campaign objective and awareness level;
- composition and visual mechanism;
- copy mode and exact on-image copy, including **none** when intentional;
- CTA treatment: on-image, platform button, caption, or none;
- visual authority and palette;
- product reference paths;
- prohibited claims and inventions;
- target ratio and placement behavior;
- required negative space or safe zones;
- what may adapt versus what must remain fixed.

Tell the model to recompose for the target ratio, not crop or stretch.

## Favor generative integration

Let the capable image model create the full scene, composition, and every brief-required element together. When the concept is type-led or lightly labeled, this includes the specified typography and any on-image CTA. When the concept is copy-free, do not invent text. The output should already read as the intended finished advertisement, not as background material awaiting a layout pass.

Treat these as generation failures:

- wrong aspect ratio or canvas;
- missing or materially incorrect brief-required copy;
- missing CTA when the brief includes one;
- generic scene-only or product-only output when the approved concept requires a more specific visual idea;
- text floating outside the visual system;
- a composition that requires major cropping or overlays to become an ad.

Regenerate failures. For an approved visual that needs another placement, use a capable generative edit or fresh generation to recompose it for the new ratio.

Use deterministic correction when:

- one word, glyph, or small copy fragment is wrong while the native typography and hierarchy are otherwise successful;
- an authentic logo must replace a generated mark;
- packaging is materially altered;
- pixel dimensions are slightly off but the aspect ratio and composition already match;
- a clean artifact repair is possible without redesigning the creative.

Do not deterministically add or redraw brief-required primary typography, cards, borders, or overall hierarchy. Do not crop a tall or square generation into a different required ratio and then reconstruct its layout. If correction becomes a manual layout pass, regenerate instead. If capable generation repeatedly fails, disclose that limitation and obtain approval before changing production methods.

## Validate the pilot itself

Before presenting a pilot, confirm:

- It is one standalone finished ad file in the requested ratio.
- Every brief-required visual and textual element is native to the composition.
- Any absence of on-image copy or CTA is intentional rather than a generation omission.
- The visual stopping idea is intentional and coherent. If the caption carries the proposition, the image still supports rather than contradicts it.
- Any on-image copy is readable at feed-preview size.
- The image is not a mockup, scene study, contact sheet, or screenshot.
- Any deterministic intervention was localized and explicitly disclosed.

## Adapt by placement

### 4:5

- Treat as the primary feed narrative.
- Keep the hook visible before secondary proof.
- Preserve meaningful product or action scale.

### 1:1

- Compress to one dominant idea.
- Remove secondary explanation before shrinking essential copy.
- Keep any on-image CTA and the core visual immediately legible.

### 9:16

- Reserve roughly the top 12–14% and bottom 10% from critical text.
- Use the extra height for narrative sequence, not empty filler.
- Keep the primary hook visible before the fold.

### 1.91:1

- Recompose horizontally.
- Use a clear text zone and a clear visual zone.
- Avoid turning the creative into a miniature vertical poster.

## Inspect every output

Review at full size and thumbnail size.

### Strategy

- The approved hypothesis is still present.
- The message matches the destination.
- The intended test variable remains isolated.

### Copy and truth

- Every visible word matches the approved brief.
- No prices, reviews, guarantees, offers, gifts, or claims were invented.
- Quantitative statements match the evidence source.
- Any visible CTA is accurate.

### Visual quality

- Anatomy and object relationships are plausible.
- No limbs, hands, tools, or products occupy impossible spaces.
- There are no duplicated, melted, or malformed objects.
- Lighting, scale, shadows, and perspective agree.
- Hierarchy works at feed size.

### Product fidelity

- Packaging geometry, colors, and recognizable marks match references.
- The logo is authentic.
- The packshot is not blended into a different product.
- Generated packaging has no unsupported microclaims.

### Adaptation

- Required safe zones are respected.
- Nothing important is cropped.
- The format feels purpose-built.
- Text remains readable.

### Delivery

- Files use sRGB.
- Metadata is stripped when practical.
- Dimensions and filenames are exact.
- Intermediates are removed.
- Contact sheets reflect final files.
- The ZIP opens and passes an archive integrity check.

Regenerate or repair failures autonomously. Escalate only if the correction changes strategy or business truth.
