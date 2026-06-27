---
name: prompt-optimizer
description: Transform user prompts into well-structured, best-practice prompts optimized for Claude. This skill should be used when users want to refine a prompt, improve prompt quality, convert a rough idea into an effective prompt, or learn why their prompt could work better. Based on Anthropic's real-world prompting course.
---

# Prompt Optimizer

Transform rough prompts into production-quality, best-practice prompts optimized for Claude. Based on principles from Anthropic's real-world prompting course.

## When to Activate

Trigger this skill when the user:
- Asks to "optimize this prompt" or "improve this prompt"
- Requests "make this prompt better" or "refine my prompt"
- Wants to convert an idea into an effective prompt
- Asks "how can I prompt this better?"
- Mentions "prompt engineering" or "prompt optimization"
- Provides a prompt and asks for feedback or improvements
- Uses `/prompt-optimizer` or similar invocation

## Core Principles

### The 7 Pillars of Effective Prompts

1. **Clarity** - Unambiguous instructions with no room for misinterpretation
2. **Specificity** - Precise details about format, length, tone, and constraints
3. **Structure** - Logical organization with clear sections and boundaries
4. **Context** - Sufficient background for informed responses
5. **Examples** - Concrete demonstrations of expected input/output
6. **Constraints** - Explicit boundaries on scope, format, and behavior
7. **Output Specification** - Exact format requirements for the response

## Optimization Workflow

### Step 1: Analyze the Original Prompt

Examine the user's prompt for:

**Strengths to Preserve:**
- Core intent and goal
- Domain-specific terminology
- Existing structure (if any)
- Unique requirements

**Weaknesses to Address:**
- Ambiguity in instructions
- Missing context or background
- Unclear output format expectations
- Lack of examples
- Missing edge case handling
- No constraints or guardrails

**Classification:**
Identify the prompt type to apply appropriate patterns:
- **Task execution** - Code generation, data transformation, analysis
- **Content creation** - Writing, summarization, formatting
- **Information extraction** - Parsing, classification, entity extraction
- **Conversation/dialogue** - Customer support, tutoring, Q&A
- **Multi-step workflow** - Complex processes with dependencies

### Step 2: Apply Optimization Techniques

Select and apply relevant techniques from [references/prompt-patterns.md](references/prompt-patterns.md):

**Always Apply:**
1. **XML Tags** - Structure input/output with semantic tags
2. **Clear Objective** - State the goal explicitly in the first sentence
3. **Output Format** - Specify exact format (JSON, markdown, bullets, etc.)

**Apply When Relevant:**
4. **Role Prompting** - Establish expertise and behavioral context
5. **Chain of Thought** - Request reasoning before conclusions
6. **Few-Shot Examples** - Demonstrate expected behavior
7. **Negative Instructions** - Specify what NOT to do
8. **Edge Case Handling** - Define behavior for ambiguous inputs
9. **Guardrails** - Add safety constraints and scope limits
10. **Prefilling** - Pre-populate response start for format control

### Step 3: Structure the Optimized Prompt

Use this canonical structure (adapt as needed):

```
[ROLE/CONTEXT - Optional but recommended]
You are a [role] specializing in [domain]. Your task is to [objective].

[INPUT SECTION - Required for data processing]
<input>
{user_data_placeholder}
</input>

[INSTRUCTIONS - Required]
<instructions>
1. [First step or requirement]
2. [Second step or requirement]
3. [Continue as needed]

[CONSTRAINTS - When applicable]
Important:
- [Constraint 1]
- [Constraint 2]
- Do NOT [negative instruction]
</instructions>

[OUTPUT FORMAT - Required]
<output_format>
Respond in the following format:
[Exact structure specification]
</output_format>

[EXAMPLES - Strongly recommended]
<examples>
<example>
Input: [sample input]
Output: [sample output]
</example>
</examples>

[EDGE CASES - When applicable]
<edge_cases>
If [condition], then [behavior].
If [condition], respond with: "[exact response]"
</edge_cases>
```

### Step 4: Validate Against Checklist

Run through [references/prompt-checklist.md](references/prompt-checklist.md):

**Clarity Check:**
- [ ] Single, unambiguous interpretation possible
- [ ] No vague words ("good", "appropriate", "some")
- [ ] Technical terms defined or contextually clear

**Completeness Check:**
- [ ] All necessary context provided
- [ ] Output format fully specified
- [ ] Edge cases addressed
- [ ] Examples included (for complex tasks)

**Structure Check:**
- [ ] XML tags delineate sections
- [ ] Long content placed before instructions
- [ ] Logical flow from context → instructions → format

**Constraint Check:**
- [ ] Scope explicitly bounded
- [ ] Negative instructions included where needed
- [ ] Character/length limits specified (if applicable)

### Step 5: Present the Optimized Prompt

Provide the user with:

1. **The Optimized Prompt** - Full, ready-to-use prompt in a code block

2. **Change Summary** - Brief explanation of key improvements:
   - Techniques applied
   - Weaknesses addressed
   - Why these changes improve performance

3. **Usage Notes** (when applicable):
   - How to customize placeholders
   - When chain-of-thought helps vs. hurts
   - Suggested test cases

## Output Format

When presenting optimized prompts, use this structure:

```markdown
## Optimized Prompt

\`\`\`
[The complete optimized prompt here]
\`\`\`

## Key Improvements

| Technique | Applied | Why |
|-----------|---------|-----|
| [Technique 1] | [How] | [Benefit] |
| [Technique 2] | [How] | [Benefit] |

## Usage Notes

- [Any relevant notes about customization or testing]
```

## Quick Reference: Common Transformations

| Original Issue | Transformation |
|----------------|----------------|
| "Write about X" | "Write a [length] [format] about X that [specific goal]. Include [required elements]." |
| "Summarize this" | "<document>{doc}</document> Summarize in [format] with [constraints]. Focus on [priorities]." |
| "Help me with code" | "Write a [language] function that [spec]. Include: [requirements]. Do NOT: [exclusions]." |
| "Analyze this data" | "<data>{data}</data> Analyze for [objective]. Output as [format]. Flag [conditions]." |
| No examples | Add 1-3 representative input/output pairs in `<examples>` tags |
| Vague output | Specify exact format: JSON schema, markdown headers, bullet structure |
| Missing context | Add role definition and task background in opening section |

## Complexity Levels

**Light Optimization** (simple tasks):
- Add clear objective
- Specify output format
- Add one example if helpful

**Standard Optimization** (most tasks):
- Full XML structure
- Role context
- 2-3 examples
- Constraints section
- Output format specification

**Production Optimization** (complex/critical tasks):
- Complete canonical structure
- Chain of thought with `<thinking>` tags
- Multiple diverse examples
- Comprehensive edge case handling
- Status flags for classification
- Explicit guardrails

## References

- [references/prompt-patterns.md](references/prompt-patterns.md) - Detailed technique patterns with examples
- [references/prompt-checklist.md](references/prompt-checklist.md) - Quick validation checklist
- [references/before-after-examples.md](references/before-after-examples.md) - Real-world transformation examples

## Anti-Patterns to Fix

When optimizing, eliminate these common mistakes:

1. **Vague Qualifiers** - "good", "appropriate", "relevant" → specific criteria
2. **Implicit Assumptions** - unstated requirements → explicit instructions
3. **Missing Format** - freeform output → structured specification
4. **No Examples** - abstract instructions → concrete demonstrations
5. **Unbounded Scope** - open-ended → constrained with limits
6. **Positive-Only Instructions** - what to do → also what NOT to do
7. **Buried Requirements** - scattered constraints → organized sections
8. **Missing Edge Cases** - happy path only → explicit handling
