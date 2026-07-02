# channel47 Skills

Public repo of marketing-focused Claude Code skills. Compatible with skills.sh.

## Structure

```
skills/
├── creative-strategy/
│   └── creative-strategist/
├── paid-media/
│   ├── media-buyer/
│   └── gaql/
├── distribution/
│   ├── content-miner/
│   ├── kit-newsletter/
│   └── twitter-algorithm-optimizer/
└── agent-ops/
    └── prompt-optimizer/
├── scripts/
│   ├── sync.sh           # Pull from ~/.claude/skills/ into repo
│   └── sanitize-check.sh # Flag personal details before push
```

Each skill directory contains `SKILL.md` as the required entry point. Skills may also include `references/`, `scripts/`, `assets/`, or `agents/` when the extra context is part of the public reusable workflow.

## Commands

```bash
./scripts/sync.sh            # Sync skills from ~/.claude/skills/
./scripts/sanitize-check.sh  # Check for personal details
```

`scripts/sync.sh` only syncs older local standalone skills from `~/.claude/skills`.
The flagship Channel47 marketing skills in this repo are maintained directly here.

## Adding a New Skill

1. Create and iterate the skill in `~/.claude/skills/<name>/`
2. Add the skill to the `SKILLS` map in `scripts/sync.sh`
3. Run `./scripts/sync.sh`
4. Run `./scripts/sanitize-check.sh` — fix any flags
5. Update `README.md` skills table
6. Commit and push

## Conventions

- Skill dirs: kebab-case names
- Category dirs: short kebab-case product areas
- `SKILL.md` is the required entry point (agent skills standard)
- `references/` for supporting docs, `scripts/` for helpers
- `agents/` may be bundled inside a skill when the skill needs a reusable subagent prompt
- No build step, no dependencies, no package.json
- Install: `npx skills add channel47/skills`
- Public repo page grouping: update `skills.sh.json` whenever skills are added, renamed, or moved

## Flagship System

Keep the public workflow easy for agents and humans to discover:

```
creative-strategist: research -> personas -> angles -> advertorial
                               \-> media-buyer + Channel47 MCPs
```

`creative-strategist` is the single flagship skill — four stages that run independently
or in sequence, accumulating into one per-product dossier.
Do not bury the flagship skill under plugin-specific language.

## Sanitization Rules

This is a PUBLIC repo. Before pushing, ensure NO personal details:

- No real names, employer references, or relationship details
- No local machine paths (`/Users/...`)
- No private env var names or account IDs
- No references to private skills (personal-voice, weekly-reflection, etc.)

Generic references like `KIT_API_KEY` are fine — that's a standard env var name.

Run `./scripts/sanitize-check.sh` to verify. It checks for known patterns.
