---
name: twitter-algorithm-optimizer
description: Analyze and optimize tweets for maximum reach using X's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility based on how the recommendation system ranks content.
license: AGPL-3.0 (referencing X's open-source algorithm)
---

# X Algorithm Optimizer

Optimize tweets against X's actual ranking system. This skill uses the publicly available algorithm code (github.com/xai-org/x-algorithm) and observed platform behavior to maximize reach.

## When to Use

- Optimizing a tweet draft before posting
- Rewriting a tweet that underperformed
- Planning a thread for maximum distribution
- Debugging why engagement dropped
- Choosing between tweet formats (text vs image vs video vs thread)

## The Algorithm (January 2026 Grok-Based System)

X open-sourced its Grok-powered recommendation algorithm in January 2026. This replaced the legacy 2023 system. The architecture:

- **Home Mixer**: Orchestrates the feed
- **Thunder**: In-memory storage for posts from accounts you follow
- **Phoenix**: Grok-based ranking — a transformer model that reads every post and scores it by predicted engagement
- **Candidate Pipeline**: Pulls candidates from followed accounts (Thunder) and random platform-wide posts (Phoenix Retrieval)

The Grok model learns from engagement patterns, not hand-coded rules. It predicts: will THIS user like, reply, repost, bookmark, or spend time on THIS post?

### Engagement Weights (From Source Code)

These are the actual multipliers from the open-sourced algorithm:

| Action | Weight | What It Means |
|--------|--------|---------------|
| Like | 0.5–1x | Baseline signal. Weakest positive action. |
| Bookmark | ~10x | Strong intent signal — user plans to return. |
| Link Click | 11x | User found content useful enough to explore. |
| Profile Click | 12x | Curiosity about the author. High-value signal. |
| Reply | 13.5x | Conversation starter. Algorithm heavily rewards this. |
| Repost | 20x | Strongest single action — user wants their network to see it. |
| Reply with author engagement | 75x | A reply that gets a reply FROM YOU. This is the king signal. |
| Engaged reply chain | ~150x | Back-and-forth conversation. Worth ~150 likes. |

**The takeaway**: One genuine reply chain where you engage back is worth more than hundreds of likes. Conversation depth dominates everything.

### Negative Signals

These actively suppress your reach:

| Signal | Impact |
|--------|--------|
| Block | Severe. Creates lasting distribution penalty. |
| Report | Severe. Flags content to moderation AND ranking. |
| Mute | Moderate. Removes you from that user's signals. |
| "Not interested" | Moderate. Trains algorithm away from your content. |
| Quick scroll-past | Mild. Low dwell time = low relevance signal. |
| Unfollow after viewing | Strong negative. Direct rejection signal. |

### Time Decay

A post loses half its potential visibility score every 6 hours. The first 30 minutes are everything — engagement velocity in this window is the single biggest distribution factor.

### Sentiment Analysis (New in 2026)

Grok monitors tone. Positive/constructive messaging gets wider distribution. Negative/combative tone gets reduced visibility even if engagement is high. Hot takes still work, but combative flamebait gets throttled.

## The Three Distribution Multipliers

### 1. X Premium Boost

Premium accounts get meaningful algorithmic advantages:

| Tier | In-Network Boost | Out-of-Network Boost | Avg Impressions/Post |
|------|-------------------|----------------------|----------------------|
| Free | 1x (baseline) | 1x (baseline) | Low — near-zero for link posts |
| Premium | ~4x | ~2x | ~600 |
| Premium+ | ~4x+ | ~2x+ | ~1,550+ |

Premium replies are also prioritized to appear at the top of conversation threads, which compounds visibility.

**Note**: If you're on Premium, you already have a structural advantage. If you're not, link posts in particular will be nearly invisible.

### 2. Content Format Boost

The algorithm applies different boosts by format:

| Format | Boost | Notes |
|--------|-------|-------|
| Native video | Highest | X is pushing video-first. Vertical video especially. |
| Image/carousel | High | Rich media gets direct ranking boost. |
| Poll | High | Easy engagement mechanic. High impression counts. |
| Text-only | Baseline | Can still perform well with strong hooks. |
| Text + external link | Penalized | 30-50% reach reduction. Near-zero for free accounts. |

### 3. Author Credibility (Tweepcred)

Your account's historical engagement patterns affect every post you make. Consistent quality posting builds compounding distribution over time. Sporadic viral attempts don't build this.

## The Link Problem

External links are the single biggest reach killer on X. The platform wants users to stay on X.

**The numbers**: Free accounts posting links get near-zero median engagement. Even Premium accounts see 30-50% reduction.

**Workaround**: Post the tweet without a link. Add the link in a reply. The main post gets full algorithmic distribution; interested users find the link in replies.

**Note**: X tested an in-app browser in late 2025 to soften link penalties. This is evolving — but for now, treat links as reach poison in the main post body.

## Format-Specific Optimization

### Single Tweet

Best for: Strong opinions, observations, questions, quick wins.

**Structure that works**:
- Lead with a hook or bold claim (first 2 seconds decide if they scroll past)
- Support with one specific detail
- End with engagement trigger (question, invitation, open loop)

**Character sweet spots**:
- 71-100 characters: 17% higher engagement rate
- 240-259 characters: Most likes (near-max length signals substance)
- The middle ground (100-200) underperforms both extremes

### Thread (4-12 Posts)

Best for: Tutorials, breakdowns, stories, building authority.

Threads get ~3x engagement vs single tweets. 8-12 tweets is the sweet spot (47% better than shorter threads).

**Thread architecture**:
1. **Hook tweet** (tweet 1): This is everything. Bold claim, specific number, or burning question. Must stand alone as compelling. "I gained 12,847 followers in 63 days" outperforms "I grew my following quickly" by 300%.
2. **Value promise** (tweet 2): Tell them what they'll get. Respect their time.
3. **Body** (tweets 3-N): One idea per tweet. Line breaks, not walls of text. Visual breaks every 3-4 tweets (screenshots, charts, images) increase completion rates by 45%.
4. **Closer**: Summary + CTA. Repost request or question.

**Thread-specific algorithm behavior**: Each tweet in a thread is ranked independently but connected. Strong early engagement on tweet 1 pulls the whole thread into feeds.

### Image/Video Post

Best for: Tutorials, demonstrations, reactions, storytelling.

- Native video gets 10x more engagement than text-only
- Vertical video accounts for ~20% of daily user time
- Users are 7x more likely to interact with vertical video
- Always upload natively — never link to YouTube/external

### Poll

Best for: Community engagement, quick temperature checks, driving replies.

Polls generate high impressions because the interaction cost is extremely low (one tap). Pair with a strong opinion in the tweet text to drive replies alongside votes.

## The Optimization Workflow

When a user gives you a tweet to optimize, follow these steps:

### Step 1: Score the Draft

Rate the tweet 1-10 on each factor:

| Factor | Weight | What to Assess |
|--------|--------|----------------|
| Reply Potential | 5x | Will people reply? Is there a question, debate, or open loop? |
| Repost Potential | 4x | Is it useful/entertaining enough that people want their followers to see it? |
| Hook Strength | 3x | First 2 seconds — does it stop the scroll? |
| Bookmark Potential | 2x | Is it reference-worthy? Will they want to come back? |
| Community Fit | 2x | Does it resonate with a specific niche/SimCluster? |
| Author Fit | 1x | Does it align with your established topics? |
| Negative Risk | -3x | Any block/report/mute risk? Combative tone? |
| Link Penalty | -2x | Does it contain an external link in the main body? |

**Weighted Score = Sum of (rating x weight)**
- 80+: Ship it
- 60-79: Good bones, minor tweaks
- 40-59: Needs rework
- Below 40: Rethink the approach

### Step 2: Identify the Primary Goal

Every tweet should optimize for ONE primary engagement type:

- **Reply-optimized**: Question, debate, incomplete thought, hot take
- **Repost-optimized**: Useful information, representational value ("this tweet speaks for me"), breaking insight
- **Bookmark-optimized**: Tutorial, data, reference material, how-to
- **Profile-click-optimized**: Mysterious/intriguing, establishes expertise, makes them want to know more

### Step 3: Map to Algorithm Strategy

Which distribution channel will carry this tweet?

- **In-network (followers)**: Content your existing audience cares about. Leverage Real-graph — reference topics they engage with.
- **Out-of-network (For You)**: Content that resonates with a SimCluster community. Needs to be niche-specific with clear topic signals.
- **Search/trending**: Keyword-relevant content. Use specific terminology the algorithm can categorize.

### Step 4: Rewrite

Apply optimizations. Every rewrite must sound like you. No growth-hacker voice. No engagement bait. The algorithm rewards genuine engagement, and your authentic voice IS genuine engagement.

Key rewrites:
- Add a hook if missing
- Add an engagement trigger (question, debate prompt) if reply potential is low
- Remove or relocate external links
- Sharpen to one clear topic (don't confuse SimCluster classification)
- Add specifics — numbers, names, timeframes (your voice should be grounded in specifics)

### Step 5: Present the Optimization

Show:
1. **Original** tweet
2. **Score** breakdown (the factor table filled in)
3. **Optimized** version
4. **What changed and why** — map each change to a specific algorithm signal
5. **Format recommendation** — should this be a single tweet, thread, image post, or video?
6. **Posting notes** — timing considerations, self-reply strategy, engagement plan for first 30 min

## Algorithm-Aligned Content Patterns

These patterns consistently trigger high-value engagement signals:

### The Specific Number Hook
> "I spent 47 hours this month on [X]. Here's what actually moved the needle."

Why it works: Specific numbers stop the scroll. Creates curiosity gap. Invites "what was it?" replies.

### The Contrarian Take
> "Unpopular opinion: [common practice] is actually holding you back. Here's why I stopped."

Why it works: Debate trigger. High reply potential. SimCluster resonance with the niche that agrees AND disagrees.

### The Build-in-Public Update
> "Week 12 update on [project]: [specific metric] is up [X]%. But [honest problem] is killing me. Anyone solved this?"

Why it works: Ongoing narrative builds Real-graph loyalty. Vulnerability invites help. Question triggers replies. Specifics trigger bookmarks.

### The Tactical How-To
> "The exact [process/tool/setup] I use to [specific outcome]. Thread 🧵"

Why it works: Repost-worthy (others want their followers to see it). Bookmark-worthy (reference material). Thread format = 3x engagement.

### The Quote-and-Expand
> [Quote tweet of relevant creator] + "This is right, but there's a piece missing: [your addition]."

Why it works: Taps into the quoted creator's audience. Adds genuine value. Profile clicks from curious readers. Builds Tweepcred through quality engagement.

## What NOT to Do

These patterns hurt reach through negative signals or credibility damage:

- **"Like if you agree"** — Engagement bait. Damages Tweepcred over time.
- **Posting links in the main body** — 30-50% reach cut. Put links in replies.
- **Vague statements** — "I think X is important" gives the algorithm nothing to work with.
- **Topic whiplash** — Posting about AI, then cooking, then politics confuses SimCluster classification.
- **Combative tone** — Grok's sentiment analysis throttles negative/aggressive content even if it gets engagement.
- **Reply-guy behavior** — Too many low-value replies to big accounts damages your credibility score.
- **Posting during dead hours** — First 30 minutes matter most. Post when your audience is active.
- **Ignoring replies** — A reply you DON'T respond to is a missed 75-150x multiplier.

## Engagement Velocity Strategy (The First 30 Minutes)

The first 30 minutes after posting determine 80%+ of a tweet's total reach. Plan for this:

1. **Post when your audience is online** — Check analytics for peak activity windows
2. **Reply to your own post** — Self-reply with additional context builds early momentum
3. **Engage immediately with any replies** — Every author-reply is a 75x signal
4. **Don't post and disappear** — Stay on the platform for at least 30 min after posting
5. **Notify engaged mutuals** — DM or tag people who'd genuinely find it interesting (not spam-tagging)

## Output Format

When optimizing a tweet, always output in this structure:

```
## Draft Analysis

**Original**: [the tweet]
**Format**: [single tweet / thread / image post / poll]
**Primary Goal**: [reply / repost / bookmark / profile-click optimized]

## Score

| Factor | Rating (1-10) | Weighted |
|--------|---------------|----------|
| Reply Potential (5x) | X | XX |
| Repost Potential (4x) | X | XX |
| Hook Strength (3x) | X | XX |
| Bookmark Potential (2x) | X | XX |
| Community Fit (2x) | X | XX |
| Author Fit (1x) | X | XX |
| Negative Risk (-3x) | X | -XX |
| Link Penalty (-2x) | X | -XX |
| **Total** | | **XX/170** |

## Optimized Version

[The rewritten tweet]

## What Changed

- [Change 1]: [Algorithm signal it targets]
- [Change 2]: [Algorithm signal it targets]

## Posting Strategy

- **Best format**: [recommendation]
- **Link handling**: [in-body / move to reply / remove]
- **First 30 min plan**: [engagement strategy]
```
