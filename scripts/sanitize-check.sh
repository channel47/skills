#!/bin/bash
# Checks the public repository for personal details that shouldn't be published.
# Run from repo root: ./scripts/sanitize-check.sh
# Returns non-zero if any matches found.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ ! -d "$REPO_ROOT/skills" ]; then
  echo "No skills/ directory found."
  exit 1
fi

# Patterns to flag (case-insensitive fixed-string search)
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

if ! command -v rg >/dev/null 2>&1; then
  echo "sanitize-check requires ripgrep (rg)."
  exit 1
fi

for pattern in "${PATTERNS[@]}"; do
  matches=$(rg -l -i -F --hidden -g '!.git/**' -g '!scripts/sanitize-check.sh' -- "$pattern" "$REPO_ROOT" 2>/dev/null || true)
  if [ -n "$matches" ]; then
    echo "FOUND: \"$pattern\" in:"
    while IFS= read -r match; do
      printf "  %s\n" "$match"
    done <<< "$matches"
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
