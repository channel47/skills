# Prompt Engineering Patterns

Detailed patterns and templates for each optimization technique. Reference this when applying specific techniques during prompt optimization.

---

## 1. XML Tag Structuring

**Purpose:** Clearly delineate input data from instructions and output expectations.

**Pattern:**
```
<context>
[Background information]
</context>

<input>
[User-provided data to process]
</input>

<instructions>
[What to do with the input]
</instructions>

<output_format>
[How to structure the response]
</output_format>
```

**When to Use:**
- Processing external data (documents, logs, transcripts)
- Complex multi-part instructions
- When programmatic extraction is needed

**Best Practices:**
- Use semantic tag names (`<transcript>`, `<patient_record>`, `<code>`)
- Nest related sections (`<examples>` containing multiple `<example>`)
- Place long content (documents, data) BEFORE instructions
- Use consistent tag naming throughout

**Example:**
```
Analyze the customer feedback below and categorize each item.

<feedback>
{customer_feedback_data}
</feedback>

<instructions>
1. Identify the sentiment (positive/negative/neutral)
2. Extract the main topic
3. Flag any urgent issues requiring immediate response
</instructions>

<output_format>
Return a JSON array with objects containing:
- "feedback_id": string
- "sentiment": "positive" | "negative" | "neutral"
- "topic": string
- "urgent": boolean
</output_format>
```

---

## 2. Role Prompting (System Context)

**Purpose:** Establish expertise, behavioral parameters, and response style.

**Pattern:**
```
You are a [role/expertise] with [experience/specialty].
Your task is to [primary objective].
[Behavioral guidance: tone, approach, priorities]
```

**When to Use:**
- Domain-specific tasks requiring expertise
- When tone/style matters (formal, friendly, technical)
- Customer-facing applications
- Tasks requiring specific judgment frameworks

**Best Practices:**
- Be specific about expertise ("senior Python developer" not "programmer")
- Include behavioral cues ("prioritize clarity over brevity")
- Match role to task requirements
- Don't over-specify (avoid contradictory traits)

**Example:**
```
You are a senior data analyst specializing in e-commerce metrics.
Your task is to interpret campaign performance data and provide actionable insights.
Prioritize practical recommendations over theoretical analysis.
Use specific numbers from the data to support your conclusions.
```

---

## 3. Chain of Thought (Reasoning Tags)

**Purpose:** Improve accuracy by externalizing reasoning before final output.

**Pattern:**
```
Before providing your final answer, analyze the problem in <thinking> tags.
Include your reasoning process, considerations, and any ambiguities you notice.
Then provide your final response in <answer> tags.
```

**When to Use:**
- Complex reasoning or analysis tasks
- Multi-step problem solving
- Tasks where accuracy is critical
- When debugging/auditing responses is important

**When to Avoid:**
- Simple, straightforward tasks
- When latency is critical
- High-volume production with cost constraints

**Best Practices:**
- Specify what to include in thinking (reasoning, ambiguities, alternatives)
- Use separate tags for thinking vs. final output
- Enable easy extraction of just the final answer
- Consider making thinking optional for simpler inputs

**Example:**
```
<transcript>
{call_transcript}
</transcript>

<instructions>
Summarize this customer service call.

First, in <thinking> tags, analyze:
- What was the customer's main issue?
- How was it resolved (or not)?
- What follow-up is needed?
- Any ambiguities or unclear points?

Then provide your summary in <summary> tags with the following structure:
- Issue: [brief description]
- Resolution: [what happened]
- Follow-up: [required/not required, details if needed]
</instructions>
```

---

## 4. Few-Shot Examples

**Purpose:** Demonstrate expected behavior through concrete input/output pairs.

**Pattern:**
```
<examples>
<example>
<input>[Sample input 1]</input>
<output>[Expected output 1]</output>
</example>

<example>
<input>[Sample input 2 - different case]</input>
<output>[Expected output 2]</output>
</example>

<example>
<input>[Sample input 3 - edge case]</input>
<output>[Expected output 3]</output>
</example>
</examples>
```

**When to Use:**
- Format is specific or unusual
- Task has nuanced requirements hard to describe
- Classification or categorization tasks
- When consistency across inputs is critical

**Best Practices:**
- Include 2-5 diverse examples
- Cover typical cases AND edge cases
- Show at least one "negative" example (what not to output)
- Examples should be representative, not cherry-picked
- Include examples of different lengths/complexity

**Example (Classification Task):**
```
Classify the following customer messages by priority.

<examples>
<example>
<message>My order hasn't arrived and it's been 3 weeks. I need a refund NOW.</message>
<classification>HIGH - Shipping issue with refund request</classification>
</example>

<example>
<message>Just wondering if you have this in blue?</message>
<classification>LOW - Product inquiry</classification>
</example>

<example>
<message>Your website is down and I can't complete my purchase!</message>
<classification>URGENT - Site outage affecting sales</classification>
</example>
</examples>

Now classify this message:
<message>{new_message}</message>
```

---

## 5. Output Format Specification

**Purpose:** Ensure consistent, predictable, parseable output.

**Pattern (JSON):**
```
Respond with a JSON object matching this exact structure:
{
  "field_name": "type - description",
  "nested_object": {
    "inner_field": "type - description"
  },
  "array_field": ["type - what each element represents"]
}
```

**Pattern (Markdown):**
```
Structure your response as follows:

## [Section 1 Name]
[Content description]

## [Section 2 Name]
[Content description]

### Subsection (if applicable)
- Bullet point 1
- Bullet point 2
```

**When to Use:**
- Always specify format for programmatic use
- Any task requiring structured output
- Multi-part responses
- When post-processing the output

**Best Practices:**
- Show exact structure, not just description
- Include type hints for JSON fields
- Specify max lengths where relevant
- Define what each field should contain
- Use consistent naming conventions

**Example:**
```
<output_format>
Respond with JSON matching this schema:
{
  "summary": "string (max 200 chars) - executive summary",
  "findings": [
    {
      "category": "string - one of: performance|cost|quality",
      "description": "string - what was found",
      "severity": "string - low|medium|high",
      "recommendation": "string - suggested action"
    }
  ],
  "next_steps": ["string - action items, max 5"]
}
</output_format>
```

---

## 6. Negative Instructions

**Purpose:** Explicitly prevent unwanted behaviors.

**Pattern:**
```
Do NOT:
- [Unwanted behavior 1]
- [Unwanted behavior 2]
- [Unwanted behavior 3]

Avoid:
- [Thing to avoid]
- [Another thing to avoid]
```

**When to Use:**
- Common failure modes for this task type
- Security-sensitive applications
- Customer-facing outputs (no internal references)
- When model tends to over-explain or add unwanted content

**Best Practices:**
- Be specific (not "don't be bad" but "don't include profanity")
- Pair with positive alternatives when helpful
- Place after positive instructions
- Focus on high-impact failure modes

**Example:**
```
<instructions>
Answer the customer's question about our product.

Do NOT:
- Make claims not found on the product page
- Reference your training data or knowledge cutoff
- Say "According to my information" or similar meta-commentary
- Provide medical, legal, or financial advice
- Promise specific outcomes or guarantees

If you cannot answer from the provided context, respond with:
"I don't have information about that. Please contact our support team."
</instructions>
```

---

## 7. Edge Case Handling

**Purpose:** Define explicit behavior for unusual or ambiguous inputs.

**Pattern:**
```
<edge_cases>
If [condition 1], then [specific behavior/response].
If [condition 2], then [specific behavior/response].
If the input is unclear or ambiguous, [what to do].
</edge_cases>
```

**When to Use:**
- Production systems handling diverse inputs
- When graceful degradation matters
- Tasks with known edge cases
- When "I don't know" is a valid response

**Best Practices:**
- List specific conditions, not vague criteria
- Provide exact responses for critical edge cases
- Include "catch-all" for unexpected situations
- Use status flags for classification (e.g., INSUFFICIENT_DATA)

**Example:**
```
<edge_cases>
Handle these special cases:

1. Empty or blank input:
   Return: {"status": "ERROR", "message": "No input provided"}

2. Input in unsupported language:
   Return: {"status": "UNSUPPORTED", "message": "Only English is supported"}

3. Input too short to analyze (< 20 words):
   Return: {"status": "INSUFFICIENT_DATA", "message": "Input too brief for analysis"}

4. Multiple conflicting topics in input:
   Focus on the first/primary topic and note others in "additional_topics" field

5. Ambiguous or unclear input:
   Ask one clarifying question before proceeding
</edge_cases>
```

---

## 8. Guardrails and Scope Limits

**Purpose:** Constrain behavior to safe, appropriate boundaries.

**Pattern:**
```
<scope>
This assistant handles ONLY:
- [In-scope topic 1]
- [In-scope topic 2]

Out of scope (redirect or decline):
- [Out-of-scope topic 1]
- [Out-of-scope topic 2]
</scope>

<guardrails>
If the user requests [prohibited action], respond with:
"[Exact refusal message]"
</guardrails>
```

**When to Use:**
- Customer-facing bots
- Domain-specific applications
- When safety/compliance matters
- Preventing misuse or off-topic requests

**Best Practices:**
- Define scope positively (what IS included)
- Provide exact refusal language
- Keep refusals brief and consistent
- Don't explain limitations in detail (prevents probing)

**Example:**
```
<scope>
You are a technical support agent for AcmeCloud.

In scope:
- AcmeCloud product features and troubleshooting
- Account and billing questions
- Integration guidance

Out of scope (politely redirect):
- Competitor comparisons
- General coding questions unrelated to AcmeCloud
- Personal advice or off-topic chat
</scope>

<guardrails>
Respond to out-of-scope requests with:
"I'm specifically designed to help with AcmeCloud questions. For that topic, I'd recommend [appropriate resource]. Is there anything AcmeCloud-related I can help with?"

Never:
- Share internal documentation or pricing not publicly available
- Commit to features or timelines not officially announced
- Provide legal, financial, or medical advice
</guardrails>
```

---

## 9. Prefilling (Response Start)

**Purpose:** Control response format by pre-populating the beginning.

**Pattern (API usage):**
```python
messages = [
    {"role": "user", "content": "[your prompt]"},
    {"role": "assistant", "content": "[start of response]"}
]
```

**When to Use:**
- Force specific format (JSON starting with `{`)
- Prevent preamble ("Here's the analysis...")
- Ensure structured output begins correctly

**Best Practices:**
- Start JSON responses with `{` or `[`
- Start XML responses with the opening tag
- Keep prefill minimal (just format start)
- Test that prefill doesn't create awkward completions

**Example:**
```
User: Analyze this data and return JSON.
<data>{data}</data>