#!/bin/bash
# Syncs specified skills from ~/.claude/skills/ into this repo.
# Copies files (not symlinks) so the repo is self-contained for git.
# Run from repo root: ./scripts/sync.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_DIR="$HOME/.claude/skills"
TARGET_DIR="$REPO_ROOT/skills"

# Skills to sync: source_name:repo_relative_target
# Add new skills to this list as you publish them.
SKILLS="
gaql:paid-media/gaql
content-miner:distribution/content-miner
kit:distribution/kit-newsletter
twitter-algorithm-optimizer:distribution/twitter-algorithm-optimizer
prompt-optimizer:agent-ops/prompt-optimizer
"

# Files/dirs to exclude from copy
EXCLUDE="__pycache__ *.pyc *.pyo .DS_Store"

mkdir -p "$TARGET_DIR"

for entry in $SKILLS; do
  source_name="${entry%%:*}"
  repo_target="${entry##*:}"
  source="$SOURCE_DIR/$source_name"
  target="$TARGET_DIR/$repo_target"

  if [ ! -d "$source" ]; then
    echo "SKIP: $source_name not found in ~/.claude/skills/"
    continue
  fi

  # Clean target and copy fresh
  rm -rf "$target"
  mkdir -p "$target"

  # Build rsync exclude args
  exclude_args=""
  for pattern in $EXCLUDE; do
    exclude_args="$exclude_args --exclude=$pattern"
  done

  rsync -a $exclude_args "$source/" "$target/"

  # Preserve public install slugs when local skill names differ from repo names.
  case "$repo_target" in
    distribution/content-miner)
      perl -0pi -e 's/^name: content-mining$/name: content-miner/m' "$target/SKILL.md"
      ;;
    distribution/kit-newsletter)
      perl -0pi -e 's/^name: kit$/name: kit-newsletter/m' "$target/SKILL.md"
      ;;
  esac

  echo "Synced: $source_name -> $repo_target"
done

echo ""
echo "Done. Next steps:"
echo "  1. Run ./scripts/sanitize-check.sh"
echo "  2. Review changes: git diff"
echo "  3. Commit and push"
