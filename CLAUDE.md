# Channel 47 Skills

Public repo of marketing-focused Claude Code skills. Compatible with skills.sh.

## Structure

```
skills/
├── <skill-name>/
│   ├── SKILL.md          # Required — agent instructions
│   ├── references/       # Optional — supporting docs
│   └── scripts/          # Optional — helper scripts
├── scripts/
│   ├── sync.sh           # Pull from ~/.claude/skills/ into repo
│   └── sanitize-check.sh # Flag personal details before push
```

## Commands

```bash
./scripts/sync.sh            # Sync skills from ~/.claude/skills/
./scripts/sanitize-check.sh  # Check for personal details
```

## Adding a New Skill

1. Create and iterate the skill in `~/.claude/skills/<name>/`
2. Add the skill to the `SKILLS` map in `scripts/sync.sh`
3. Run `./scripts/sync.sh`
4. Run `./scripts/sanitize-check.sh` — fix any flags
5. Update `README.md` skills table
6. Commit and push

## Conventions

- Skill dirs: kebab-case names
- `SKILL.md` is the required entry point (agent skills standard)
- `references/` for supporting docs, `scripts/` for helpers
- No build step, no dependencies, no package.json
- Install: `npx skillsadd channel47/skills`

## Sanitization Rules

This is a PUBLIC repo. Before pushing, ensure NO personal details:

- No real names, employer references, or relationship details
- No local machine paths (`/Users/...`)
- No private env var names or account IDs
- No references to private skills (personal-voice, weekly-reflection, etc.)

Generic references like `KIT_API_KEY` are fine — that's a standard env var name.

Run `./scripts/sanitize-check.sh` to verify. It checks for known patterns.
