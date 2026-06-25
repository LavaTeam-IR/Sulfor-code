#!/usr/bin/env python3
"""
Sulfor Code - AI Terminal Assistant
by @lavateam_IR
"""

import os
import sys
import time
import urllib.request
import textwrap
import threading

# ── Windows: enable ANSI colors ───────────────────────────────────────────────
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ── ANSI Colors ────────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
VIOLET  = "\033[38;2;130;80;255m"
CYAN    = "\033[38;2;0;220;200m"
AMBER   = "\033[38;2;255;180;40m"
WHITE   = "\033[38;2;220;220;230m"
GRAY    = "\033[38;2;90;90;110m"
RED     = "\033[38;2;255;70;70m"
GREEN   = "\033[38;2;60;220;120m"
MAGENTA = "\033[38;2;200;80;255m"

# ── Logo ───────────────────────────────────────────────────────────────────────
LOGO = f"""
{VIOLET}  ██████  ██    ██ ██      ███████  ██████  ██████  {RESET}
{VIOLET} ██       ██    ██ ██      ██      ██    ██ ██   ██ {RESET}
{CYAN}  ███████  ██    ██ ██      █████   ██    ██ ██████  {RESET}
{CYAN}       ██  ██    ██ ██      ██      ██    ██ ██   ██ {RESET}
{MAGENTA}  ██████   ██████  ███████ ██       ██████  ██   ██ {RESET}

{AMBER}  > CODE{RESET}  {GRAY}intelligent terminal assistant{RESET}
"""

BANNER = f"{VIOLET}{'─' * 52}{RESET}"

# ── Spinner ────────────────────────────────────────────────────────────────────
class Spinner:
    FRAMES = ["|", "/", "-", "\\"]

    def __init__(self, msg="Thinking"):
        self.msg = msg
        self._stop = threading.Event()
        self._t = threading.Thread(target=self._spin, daemon=True)

    def _spin(self):
        i = 0
        while not self._stop.is_set():
            f = self.FRAMES[i % len(self.FRAMES)]
            sys.stdout.write(f"\r  {CYAN}{f}{RESET}  {GRAY}{self.msg}...{RESET}   ")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def start(self): self._t.start()

    def stop(self):
        self._stop.set()
        self._t.join()
        sys.stdout.write("\r" + " " * 45 + "\r")
        sys.stdout.flush()

# ── UI Helpers ─────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_logo():
    print(LOGO)
    print(BANNER)
    print(f"{GRAY}  Build  {RESET}{WHITE}v1.0.0{RESET}   {GRAY}  by{RESET}  {AMBER}@lavateam_IR{RESET}")
    print(f"{BANNER}\n")

def print_response(text):
    width = 66
    print(f"\n{CYAN}+{'─'*52}+{RESET}")
    print(f"{CYAN}|{RESET}  {VIOLET}Sulfor{RESET}")
    print(f"{CYAN}+{'─'*52}+{RESET}")
    for line in text.split("\n"):
        chunks = textwrap.wrap(line, width) if len(line) > width else [line]
        if not chunks:
            print(f"{CYAN}|{RESET}")
            continue
        for chunk in chunks:
            print(f"{CYAN}|{RESET}  {WHITE}{chunk}{RESET}")
    print(f"{CYAN}+{'─'*52}+{RESET}\n")

def print_info(msg):  print(f"  {GRAY}i  {msg}{RESET}")
def print_error(msg): print(f"  {RED}X  {msg}{RESET}")
def print_ok(msg):    print(f"  {GREEN}OK {msg}{RESET}")

def farewell():
    print(f"\n{VIOLET}  Goodbye.{RESET}  {GRAY}-- Sulfor Code  by @lavateam_IR{RESET}\n")

# ── Local Model Config ─────────────────────────────────────────────────────────
LOCAL_DIR   = os.path.join(os.path.expanduser("~"), ".sulfor")
MODEL_FILE  = os.path.join(LOCAL_DIR, "tinyllama-q4.gguf")
MARKER_FILE = os.path.join(LOCAL_DIR, ".ready")

MODEL_URL = (
    "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
    "/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
)

# ── Ensure llama-cpp-python ────────────────────────────────────────────────────
def ensure_backend():
    try:
        import llama_cpp  # noqa
        return True
    except ImportError:
        pass
    print_info("Installing llama-cpp-python (first time only, please wait)...")
    ret = os.system(
        f'"{sys.executable}" -m pip install llama-cpp-python --quiet '
        "--extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu"
    )
    return ret == 0

# ── Download model ─────────────────────────────────────────────────────────────
def download_model():
    os.makedirs(LOCAL_DIR, exist_ok=True)
    if os.path.exists(MARKER_FILE) and os.path.exists(MODEL_FILE):
        return True

    print(f"\n  {AMBER}First-time setup:{RESET} downloading TinyLlama {GRAY}(~670 MB){RESET}")
    print(f"  {GRAY}This only happens once. After this, Sulfor works fully offline.{RESET}\n")

    try:
        def _progress(block, bsize, total):
            done = block * bsize
            if total > 0:
                pct  = min(100, int(done * 100 / total))
                fill = int(pct / 2)
                bar  = f"{CYAN}{'#' * fill}{GRAY}{'.' * (50 - fill)}{RESET}"
                mb   = done / 1_048_576
                tot  = total / 1_048_576
                sys.stdout.write(f"\r  [{bar}] {AMBER}{pct:3d}%{RESET}  {mb:.0f}/{tot:.0f} MB  ")
                sys.stdout.flush()

        urllib.request.urlretrieve(MODEL_URL, MODEL_FILE, reporthook=_progress)
        print()
        open(MARKER_FILE, "w").close()
        print_ok("Model downloaded successfully.")
        return True
    except Exception as e:
        print_error(f"Download failed: {e}")
        return False

# ── Inference ──────────────────────────────────────────────────────────────────
_llm = None

def get_llm():
    global _llm
    if _llm is None:
        from llama_cpp import Llama
        _llm = Llama(
            model_path=MODEL_FILE,
            n_ctx=2048,
            n_threads=max(1, (os.cpu_count() or 2) // 2),
            verbose=False,
        )
    return _llm

def infer(prompt):
    llm = get_llm()
    full = (
        "<|system|>\nYou are Sulfor Code, a helpful AI coding assistant "
        "in a terminal. Be concise and technical. English only. No markdown.\n"
        f"<|user|>\n{prompt}\n<|assistant|>\n"
    )
    out = llm(full, max_tokens=512, stop=["<|user|>", "<|system|>"])
    return out["choices"][0]["text"].strip()

# ── Chat Loop ──────────────────────────────────────────────────────────────────
def run_chat():
    clear()
    print_logo()
    print(f"  {MAGENTA}* LOCAL MODE{RESET}  {GRAY}-- fully offline, 100% free, no API key\n{RESET}")

    if not ensure_backend():
        print_error("Could not install llama-cpp-python.")
        print_info("Try: pip install llama-cpp-python")
        sys.exit(1)

    if not download_model():
        print_error("Model download failed. Check your internet connection.")
        sys.exit(1)

    print(f"\n  {GRAY}Loading model into memory...{RESET}")
    spin = Spinner("Loading")
    spin.start()
    try:
        get_llm()
        spin.stop()
    except Exception as e:
        spin.stop()
        print_error(f"Failed to load model: {e}")
        sys.exit(1)

    print_ok("Model loaded. Sulfor is ready.\n")
    print(f"  {GRAY}Type your message.  Type  {WHITE}bye/{GRAY}  to exit.{RESET}")
    print(f"  {BANNER}\n")

    while True:
        try:
            user_input = input(f"{VIOLET}sulfor{RESET}{GRAY}>{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            user_input = "bye/"

        if not user_input:
            continue

        if user_input.lower() in ("bye/", "exit", "quit"):
            farewell()
            sys.exit(0)

        print(f"  {AMBER}you:{RESET} {WHITE}{user_input}{RESET}")

        spin = Spinner("Thinking")
        spin.start()
        try:
            reply = infer(user_input)
            spin.stop()
            print_response(reply)
        except Exception as e:
            spin.stop()
            print_error(f"Error: {e}")

# ── Entry Point ────────────────────────────────────────────────────────────────
def main():
    args = sys.argv[1:]
    if args and args[0] == "run":
        args = args[1:]
    try:
        run_chat()
    except KeyboardInterrupt:
        farewell()
        sys.exit(0)

if __name__ == "__main__":
    main()
