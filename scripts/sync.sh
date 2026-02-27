#!/bin/bash
# Syncs specified skills from ~/.claude/skills/ into this repo.
# Copies files (not symlinks) so the repo is self-contained for git.
# Run from repo root: ./scripts/sync.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_DIR="$HOME/.claude/skills"
TARGET_DIR="$REPO_ROOT/skills"

# Skills to sync: source_name → repo_name
# Add new skills to this list as you publish them.
declare -A SKILLS=(
  ["gaql"]="gaql"
  ["content-miner"]="content-miner"
  ["kit"]="kit-newsletter"
  ["twitter-algorithm-optimizer"]="twitter-algorithm-optimizer"
  ["prompt-optimizer"]="prompt-optimizer"
)

# Files/dirs to exclude from copy
EXCLUDE=(
  "__pycache__"
  "*.pyc"
  "*.pyo"
  ".DS_Store"
)

mkdir -p "$TARGET_DIR"

for source_name in "${!SKILLS[@]}"; do
  repo_name="${SKILLS[$source_name]}"
  source="$SOURCE_DIR/$source_name"
  target="$TARGET_DIR/$repo_name"

  if [ ! -d "$source" ]; then
    echo "SKIP: $source_name not found in ~/.claude/skills/"
    continue
  fi

  # Clean target and copy fresh
  rm -rf "$target"
  mkdir -p "$target"

  # Build rsync exclude args
  exclude_args=""
  for pattern in "${EXCLUDE[@]}"; do
    exclude_args="$exclude_args --exclude=$pattern"
  done

  rsync -a $exclude_args "$source/" "$target/"

  echo "Synced: $source_name → $repo_name"
done

echo ""
echo "Done. Next steps:"
echo "  1. Run ./scripts/sanitize-check.sh"
echo "  2. Review changes: git diff"
echo "  3. Commit and push"
