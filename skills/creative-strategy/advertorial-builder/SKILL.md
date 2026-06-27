---
name: advertorial-builder
description: Build a research-backed, long-form advertorial or editorial pre-sell page from customer research, personas, and a winning angle. Use when the user asks for an advertorial, presell page, editorial sales page, listicle landing page, comparison page, "reasons why" page, problem-solution page, or wants to turn an ad angle into a build-ready page.
---

# Advertorial Builder — From Winning Angle to Build-Ready Page

Turn a validated angle into a long-form editorial pre-sell page that bridges cold traffic from ad click to product page. The output is not generic landing page copy. It is a structured advertorial with a clear reader journey, proof ledger, claims guardrails, and build notes.

## Required Inputs

Look in the workspace first:

- `[product-slug]-research.md` from `customer-research`
- `[product-slug]-personas.md` from `persona-builder`
- `[product-slug]-angles.md` from `angle-generator`

If one of these is missing, proceed only if the user provides equivalent context. Warn clearly when the advertorial is being built from thin inputs.

Also collect or infer:

- Product name, URL, price, and offer
- Target persona
- Primary angle
- Proof assets available now: testimonials, demos, reviews, stats, certifications, before/after data
- Compliance constraints: health, finance, children, supplements, regulated claims, platform policy risks
- Desired destination after the advertorial: PDP, checkout, quiz, call booking, lead form

## Core Principle

An advertorial earns the sale before the offer appears. It should move the reader through:

1. Recognition: "this is my situation"
2. Stakes: "this problem costs more than I thought"
3. Mechanism: "this solution works differently"
4. Proof: "I can believe this"
5. Objection handling: "my hesitation is answered"
6. Bridge: "the next click makes sense"

Every section should serve that path. Do not add decorative sections.

## Archetype Selection

Choose one primary archetype based on the angle and persona:

| Archetype | Use When |
|---|---|
| Problem-Solution | The audience has a clear painful problem and needs a credible path out |
| Myth-Busting | The market believes the wrong thing and the product wins by correcting it |
| Us-vs-Them | The product has a meaningful mechanism or category difference |
| Honest Review | Skeptical buyers need a balanced, specific evaluation |
| Listicle | The angle benefits from multiple reasons, symptoms, or buying criteria |
| Founder Story | The origin story creates trust and explains the mechanism |
| Comparison | The buyer is actively choosing between alternatives |
| Quiz/Diagnostic | The reader needs self-identification before the offer |

Do not force an archetype. If the evidence is thin, pick the simplest structure and say what proof is missing.

## Build Process

### 1. Validate the angle

Read the selected angle and confirm:

- It has at least one high-intensity quote or equivalent evidence
- It maps to a specific persona and journey stage
- It has a clear claim the advertorial can prove
- It does not attract the anti-persona

If no angle is specified, select the highest-ranked Tier 1 angle from the angles file and explain why.

### 2. Build the page outline

Use this default spine unless the archetype demands a different order:

```markdown
# [Advertorial Title]

## Above the Fold
- Eyebrow:
- Headline:
- Deck:
- Hero visual:
- Credibility cue:
- Primary bridge CTA:

## The Problem
## Why Common Solutions Miss
## The Mechanism
## Proof Ledger
## How It Works
## Objection Handling
## Product Bridge
## Final CTA
## Claims And Compliance Notes
```

### 3. Write the advertorial

Write the full page in build-ready Markdown:

- Use the persona's language fingerprint
- Pull exact phrases from research naturally
- Keep paragraphs short enough for mobile reading
- Put the strongest proof within the first third of the page
- Use subheads that carry the skimming story on their own
- Treat the CTA as a bridge, not a hard pitch

### 4. Create the proof ledger

Every meaningful claim needs a source status:

| Claim | Status | Source | Safe Wording |
|---|---|---|---|
| [claim] | proven / needs source / demo-only / remove | [quote, review, study, internal data, none] | [publish-safe version] |

Rules:

- Never invent testimonials, metrics, ratings, customer counts, or before/after results.
- If proof is missing, use honest placeholders like `[needs testimonial]` or rewrite the claim as a hypothesis.
- Label demo/spec artifacts as demos or concepts.
- For regulated categories, downgrade claims to observable facts and user-reported language unless substantiation is supplied.

### 5. Add build notes

Include practical handoff notes:

- Suggested sections and component types
- Image or screenshot needs
- CTA destination and tracking parameters
- Mobile reading rhythm
- Suggested ad-to-page message match
- Optional A/B test variants

## Output Format

Save as `[product-slug]-advertorial.md`:

```markdown
---
product: "[product-slug]"
stage: advertorial
generated: "[YYYY-MM-DD]"
persona: "[persona name]"
angle: "[angle name]"
archetype: "[archetype]"
destination_url: "[URL]"
proof_status: complete | partial | demo-only
---

# [Advertorial Title]

## Strategy Brief
- Persona:
- Angle:
- Archetype:
- Reader state:
- Belief to create:
- CTA:

## Page Copy
[Full advertorial]

## Proof Ledger
[Claims table]

## Build Notes
[Implementation notes]

## Risks And Revisions
[Compliance, proof, tone, or conversion risks]
```

## Quality Standards

- The page is traceable to research, persona, and angle inputs.
- The first screen makes the product/category signal obvious.
- The page answers the biggest objection before the final CTA.
- Claims are either sourced, softened, labeled, or removed.
- No fake proof, fake scarcity, fake statistics, or invented quotes.
- The final deliverable is useful to a copywriter, designer, and builder without another explanation pass.
