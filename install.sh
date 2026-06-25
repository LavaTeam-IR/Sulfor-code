#!/bin/bash
# ─────────────────────────────────────────────────────────
#  Sulfor Code — installer
#  by @lavateam_IR
#  Usage:
#    curl -sSL https://YOUR_SERVER/install.sh | bash
# ─────────────────────────────────────────────────────────

set -e

VIOLET='\033[38;2;130;80;255m'
CYAN='\033[38;2;0;220;200m'
AMBER='\033[38;2;255;180;40m'
GREEN='\033[38;2;60;220;120m'
RED='\033[38;2;255;70;70m'
GRAY='\033[38;2;90;90;110m'
RESET='\033[0m'
BOLD='\033[1m'

echo ""
echo -e "${VIOLET}  ██████  ██    ██ ██      ███████  ██████  ██████${RESET}"
echo -e "${VIOLET} ██       ██    ██ ██      ██      ██    ██ ██   ██${RESET}"
echo -e "${CYAN}  ███████  ██    ██ ██      █████   ██    ██ ██████${RESET}"
echo -e "${CYAN}       ██  ██    ██ ██      ██      ██    ██ ██   ██${RESET}"
echo -e "${VIOLET}  ██████   ██████  ███████ ██       ██████  ██   ██${RESET}"
echo ""
echo -e "${AMBER}  ▸ CODE${RESET}  ${GRAY}installer  —  by @lavateam_IR${RESET}"
echo ""
echo -e "${VIOLET}────────────────────────────────────────────────────${RESET}"
echo ""

# ── Check Python ──────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
  echo -e "  ${RED}✗  Python 3 is required but not found.${RESET}"
  echo -e "  ${GRAY}Install it from https://python.org and re-run.${RESET}"
  exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo -e "  ${GREEN}✓${RESET}  Python ${PY_VER} detected"

# ── Check pip ─────────────────────────────────────────────
if ! python3 -m pip --version &>/dev/null; then
  echo -e "  ${AMBER}⚙  Installing pip...${RESET}"
  python3 -m ensurepip --upgrade 2>/dev/null || true
fi
echo -e "  ${GREEN}✓${RESET}  pip ready"

# ── Download sulfor.py + setup.py ─────────────────────────
INSTALL_DIR="$HOME/.sulfor/pkg"
mkdir -p "$INSTALL_DIR"

BASE_URL="https://lavateam_IR.github.io/sulfor-code"   # ← replace with your server URL

echo -e "  ${CYAN}↓${RESET}  Downloading Sulfor Code..."
curl -sSL "${BASE_URL}/sulfor.py"  -o "${INSTALL_DIR}/sulfor.py"
curl -sSL "${BASE_URL}/setup.py"   -o "${INSTALL_DIR}/setup.py"
echo -e "  ${GREEN}✓${RESET}  Files downloaded"

# ── Install ───────────────────────────────────────────────
echo -e "  ${CYAN}⚙${RESET}  Installing..."
python3 -m pip install --quiet --upgrade "${INSTALL_DIR}"
echo -e "  ${GREEN}✓${RESET}  Sulfor Code installed"

# ── Shell PATH fix ────────────────────────────────────────
PIPBIN=$(python3 -m site --user-base 2>/dev/null)/bin
if [[ ":$PATH:" != *":$PIPBIN:"* ]]; then
  SHELL_RC=""
  if [[ -f "$HOME/.zshrc" ]]; then
    SHELL_RC="$HOME/.zshrc"
  elif [[ -f "$HOME/.bashrc" ]]; then
    SHELL_RC="$HOME/.bashrc"
  fi

  if [[ -n "$SHELL_RC" ]]; then
    echo "" >> "$SHELL_RC"
    echo "# Sulfor Code" >> "$SHELL_RC"
    echo "export PATH=\"\$PATH:$PIPBIN\"" >> "$SHELL_RC"
    echo -e "  ${AMBER}!${RESET}  Added ${PIPBIN} to PATH in ${SHELL_RC}"
    echo -e "  ${GRAY}   Run: source ${SHELL_RC}  (or open a new terminal)${RESET}"
  else
    echo -e "  ${AMBER}!${RESET}  Add this to your shell config manually:"
    echo -e "        ${GRAY}export PATH=\"\$PATH:${PIPBIN}\"${RESET}"
  fi
fi

echo ""
echo -e "${VIOLET}────────────────────────────────────────────────────${RESET}"
echo -e "  ${GREEN}${BOLD}Sulfor Code is ready!${RESET}"
echo ""
echo -e "  Run:  ${CYAN}sulfor run${RESET}"
echo ""
echo -e "  ${GRAY}by @lavateam_IR${RESET}"
echo ""
