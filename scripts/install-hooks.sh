#!/usr/bin/env bash
# install-hooks.sh — Installs make-a-change pre-commit audit guard into .git/hooks/pre-commit
set -euo pipefail

GIT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [ -z "$GIT_ROOT" ]; then
  echo "❌ Error: Not inside a Git repository." >&2
  exit 1
fi

HOOKS_DIR="$GIT_ROOT/.git/hooks"
PRE_COMMIT_HOOK="$HOOKS_DIR/pre-commit"

mkdir -p "$HOOKS_DIR"

cat << 'EOF' > "$PRE_COMMIT_HOOK"
#!/usr/bin/env bash
# make-a-change pre-commit guard
set -euo pipefail

# Find python3
PYTHON_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PYTHON_BIN" ]; then
  echo "⚠️ Warning: python3 not found, skipping make-a-change pre-commit audit."
  exit 0
fi

# Locate audit script (in repo or skills library)
AUDIT_SCRIPT=""
if [ -f "./scripts/audit-work-items.py" ]; then
  AUDIT_SCRIPT="./scripts/audit-work-items.py"
elif [ -f "$HOME/vault/data/skills_db/make-a-change/scripts/audit-work-items.py" ]; then
  AUDIT_SCRIPT="$HOME/vault/data/skills_db/make-a-change/scripts/audit-work-items.py"
elif [ -f "$HOME/skills/make-a-change/scripts/audit-work-items.py" ]; then
  AUDIT_SCRIPT="$HOME/skills/make-a-change/scripts/audit-work-items.py"
fi

if [ -n "$AUDIT_SCRIPT" ]; then
  echo "🔍 [make-a-change] Running pre-commit work-item audit..."
  if ! "$PYTHON_BIN" "$AUDIT_SCRIPT" --strict .; then
    echo "❌ [make-a-change] Pre-commit audit failed! Fix errors or malformatted files before committing." >&2
    exit 1
  fi
fi

exit 0
EOF

chmod +x "$PRE_COMMIT_HOOK"
echo "✓ make-a-change pre-commit hook installed successfully into: $PRE_COMMIT_HOOK"
