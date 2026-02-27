#!/bin/bash
# Checks skills/ directory for personal details that shouldn't be published.
# Run from repo root: ./scripts/sanitize-check.sh
# Returns non-zero if any matches found.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "No skills/ directory found. Run sync.sh first."
  exit 1
fi

# Patterns to flag (case-insensitive grep)
PATTERNS=(
  "Jackson Dean"
  "jackson dean"
  "Jackson's"
  "/Users/jackson"
  "KIT_API_KEY_CH47"
  "fouram"
  "4AM"
  "ctrlswing"
  "Chiara"
  "paidbriefs"
)

found=0

for pattern in "${PATTERNS[@]}"; do
  matches=$(grep -rl "$pattern" "$SKILLS_DIR" 2>/dev/null || true)
  if [ -n "$matches" ]; then
    echo "FOUND: \"$pattern\" in:"
    echo "$matches" | sed 's/^/  /'
    found=1
  fi
done

if [ "$found" -eq 1 ]; then
  echo ""
  echo "Personal details found. Sanitize before pushing."
  exit 1
else
  echo "Clean. No personal details found."
  exit 0
fi
