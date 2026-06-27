---
name: content-miner
description: "Extract high-signal content from recent activity and package it for distribution. Use this skill whenever the user says anything like 'content mine', 'what should I post', 'find me content', 'what's shareable', 'content ideas', 'mine my week', 'what did I learn this week', 'anything worth posting', 'content from my notes', 'extract content', or any indication they want to turn recent work, thinking, or builds into distributable content across X, LinkedIn, Newsletter, and GitHub. Also trigger when they reference wanting to 'show the work', 'build in public', or 'post about' something recent."
---

# Content Mining

Turn recent activity into distributable content. Not a content calendar. A mining operation. Dig through what actually happened, find the veins worth extracting, and shape them for the right channel.

The premise: the best content already exists. It's buried in notes, conversations, builds, decisions, and half-formed thoughts from the past week. This skill surfaces it, tests it, and formats it.

---

## Before You Start

**Load the brand voice first.** If a brand-voice skill exists, read it before writing a single word of output. Every piece of content this skill produces must pass through that voice. No exceptions. If no brand-voice skill exists, ask the user to describe their voice and tone before drafting anything.

**Get the current date.** Run `date` or equivalent. You need this to anchor timestamps from notes and chats. Get it wrong and you're mining last month's material.

**Check available tools.** This skill pulls from multiple sources. Use what's available:

- **Apple Notes** (daily logs, longer reflections, voice-note transcripts)
- **Personal context** (`~/.claude/personal-context.md` — life context, relationships, career arc)
- **Past chats** (recent_chats / conversation_search)
- **Reminders / tasks** (completed items reveal what actually got done)
- **Web search** (for context on topics, trending angles, what's already been said)

If some sources are missing, work with what you have. Partial context is better than no context. Flag what's missing so the user knows the gaps.

---

## Phase 1: Gather

Pull the last 7–14 days from every available source. Cast wide. You're not filtering yet.

### Notes and Logs

Read daily logs and longer notes/reflections. Look for:

- **Things that broke and got fixed.** Build log material. The more specific the failure, the better the content.
- **Decisions made.** Process note material. What changed, why, what was the old way.
- **Tools tested or abandoned.** Tool report material. Real usage, not feature lists.
- **Observations or rants.** Contrarian take material. The thing they noticed that nobody's saying.
- **Numbers, results, timelines.** Proof points. "Spent 3 hours" or "saved 40%" or "deleted staging twice" are gold.

Use confirmed current date to anchor all timestamps. Chronology within each day matters. Morning confusion can resolve into evening clarity. Read entries in order and treat the last entry of a day as the landed position.

### Personal Context & Project State

Read `~/.claude/personal-context.md` and relevant project CLAUDE.md files. Look for:

- **Direction shifts.** Anything that changed course in the last two weeks. Changes in strategy are process notes waiting to happen.
- **New projects or milestones.** Anything shipped, launched, or hit a meaningful threshold.
- **Resolved questions.** If something was open and now has an answer, that's a content arc.
- **Relationships between projects.** Unexpected connections between separate threads often make the most interesting content.

### Past Chats

Use `recent_chats` (last 7–14 days) and `conversation_search` for specific threads. Look for:

- **Problems worked through.** The messy middle of a build, debugged live. Build log gold.
- **Explanations given.** When someone explained something clearly to an AI, that explanation is often 80% of a post already.
- **Questions that kept recurring.** If the same question showed up three times, it's a topic the audience is also wondering about.
- **"Aha" moments.** When the conversation shifted from confusion to clarity. That inflection point IS the content.
- **Techniques or workflows refined.** Anything that got better through iteration is a process note.

### Completed Tasks / Reminders

Check completed reminders and tasks. These reveal:

- What actually shipped vs. what was planned
- The gap between intention and execution (content in itself)
- Small wins that didn't feel noteworthy but might be

### Web Context (Optional, Strategic)

If a mined topic is timely, do a quick search to understand:

- What's already been said about it (so the user can say something different)
- Whether there's a trending angle that gives the topic a tailwind
- What the conventional wisdom is (so they can push against it if warranted)

Don't over-research. The goal isn't to write about what's trending. It's to find where lived experience intersects with what people care about right now.

---

## Phase 2: Extract

Now filter. Not everything interesting is shareable. Not everything shareable is worth the effort.

Run each potential content nugget through these five signal tests. See `references/signal-tests.md` for the detailed rubric.

**1. Provenance** — Did this come from doing something or reading about something? First-hand only.

**2. Specificity** — Does this contain at least one concrete detail the audience can use? A specific tool, number, failure mode, or decision.

**3. Replaceability** — Could any other newsletter in this space have said this? If yes, sharpen the angle or kill it.

**4. Tension** — Is there a gap between what people assume and what was experienced? Between the demo and the reality? Tension drives engagement.

**5. "So What"** — Why does this matter to someone who isn't the user? The answer needs to be specific, not general.

### Nugget Classification

Tag each surviving nugget by content type. See `references/content-types.md` for the full taxonomy with channel mapping and beat patterns.

| Type | What It Is | Primary Channel |
|------|-----------|-----------------|
| **Build Log** | What got built, broke, was learned | Newsletter / X thread |
| **Tool Report** | Tested, not reviewed. Real usage | X post / Newsletter |
| **Contrarian Take** | Thing the space isn't saying, or is saying wrong | X post / LinkedIn |
| **Process Note** | How a decision got made | Newsletter / LinkedIn |
| **Shipping Update** | Something released or made public | GitHub / X post |
| **Receipts** | Numbers, screenshots, before/after, proof | X post / LinkedIn |

---

## Phase 3: Package

For each high-signal nugget, produce channel-specific drafts. Not every nugget goes to every channel. Match the material to where it works best.

**If a brand-voice skill is loaded, follow its channel variations, beat patterns, opening moves, closing moves, and grammar rules for ALL drafts.**

### Channel Specs

**X (Short Post)**
- One idea, well-aimed
- The whole post IS the kicker
- Character-efficient. Every word load-bearing
- Observations, not announcements

**X (Thread)**
- Build an idea step by step
- Each post stands alone
- Setup (1–2 tweets), depth (3–6 tweets), kicker (final tweet)
- End with something that sticks, not a recap
- Only use for material with enough depth to warrant it

**LinkedIn**
- Same voice, slightly more context
- Needs more setup because the feed is noisier
- 1–3 paragraphs. Not an essay. Not a one-liner
- Never corporate. Never performative

**Newsletter**
- Fullest expression. Single topic, full depth
- Cold open (no preamble, no "welcome to...")
- One topic per newsletter. No roundups
- Leave one thread hanging at the end

**GitHub**
- README updates, new releases, code snippets
- Minimal narrative. Let the artifact speak
- Clear install/usage instructions if applicable
- Link to deeper content for context

---

## Phase 4: Present

Deliver the output as a structured brief. Not a wall of drafts. A menu the user can act on, with the best items at the top.

### Output Structure

```
# Content Mine: [Date Range]

## Top Picks
[2-3 highest-signal items, ranked. Each with:]
- The nugget (one sentence: what happened, why it matters)
- Recommended channel(s)
- Draft(s)

## Secondary Ideas
[3-5 additional items, less developed. Each with:]
- The nugget
- Why it passed the signal tests
- Suggested channel and angle (no full draft unless requested)

## Parking Lot
[Ideas that are interesting but not ready. Missing specificity,
need more development, or waiting on a result before they're postable.]

## Source Map
[Quick reference: which sources each nugget came from,
so the user can go deeper if needed]
```

### Presentation Rules

- Lead with the strongest piece. Don't bury it
- Don't oversell. If a nugget is good, the draft proves it
- Show the draft, not a description of the draft
- If a nugget works for multiple channels, draft the primary version and note how it adapts
- Keep the brief scannable. Should be actionable in under 5 minutes

---

## Fast Mode

When the user says "just post something" or signals urgency:

1. Pull the last 3 days of notes and chats (quick gather)
2. Find the single most concrete, specific thing that happened
3. Draft one X post and one LinkedIn post
4. Present both. No brief, no parking lot. Just the drafts

Speed over thoroughness. A good-enough post today beats a perfect post never.

---

## The Mining Instinct

These patterns tend to produce the highest-signal content. Calibrate toward them:

**The gap between the demo and the build.** When something that looked easy took 10x longer in practice.

**The workflow that replaced the old workflow.** Before/after with specifics.

**The thing that broke in a useful way.** Failures that taught something.

**The opinion that costs something.** Not a free take. One that risks social capital and builds trust.

**The number that tells a story.** Specific numbers anchor credibility without bragging.

---

## Anti-Patterns

| Don't | Why | Instead |
|-------|-----|---------|
| Mine for engagement bait | Violates the replaceability test | Mine for experience-backed insights |
| Force content from a slow week | Low signal is worse than no signal | Park the ideas and wait |
| Draft all channels for every nugget | Wastes effort on bad channel fits | Match the nugget to its natural home |
| Summarize without a take | That's a status update, not content | Add the "so what" or kill it |
| Polish before user reviews | They might hate the angle | Show nugget and angle first, polish second |
| Ignore the parking lot | Half-baked ideas ripen later | Capture them. Revisit next session |
