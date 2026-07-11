# channel47 Skills

Public repository of three creative-strategy skills.

## Structure

```
skills/
└── creative-strategy/
    ├── ad-recon/
    ├── brief-me/
    └── creative-strategist/
scripts/
└── sanitize-check.sh
```

Each skill directory contains `SKILL.md` as its entry point. A skill may also
include `references/`, `scripts/`, `assets/`, or `agents/` when those files are
required by the workflow.

## Commands

```bash
./scripts/sanitize-check.sh
```

## Adding a Skill

1. Add the skill under `skills/creative-strategy/<name>/`.
2. Add `SKILL.md` with valid `name` and `description` frontmatter.
3. Add supporting files only when the workflow requires them.
4. Run `./scripts/sanitize-check.sh` and fix any flags.
5. Update `README.md` and `skills.sh.json`.

## Conventions

- Skill and category directories use kebab-case.
- `SKILL.md` is the required entry point.
- `references/` contains supporting instructions; `scripts/` contains helpers.
- The repository has no build step or package dependencies.
- Public install command: `npx skills add channel47/skills`.

## Shared Files

- `brief-me` writes shared brand context to `brand/context.md`.
- `ad-recon` and `creative-strategist` write stage sections to
  `creative/[product-slug]-dossier.md`.
- Quote and ad IDs are append-only. Do not renumber them during maintenance.

## Sanitization

This is a public repository. Do not include:

- real client or employer details;
- local machine paths;
- private environment variable names or account IDs;
- references to private skills or personal files.

Run `./scripts/sanitize-check.sh` before publishing changes.
