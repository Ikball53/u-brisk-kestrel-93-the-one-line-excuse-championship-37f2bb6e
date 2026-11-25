from pathlib import Path

# Deterministic single-line entry: no randomness, no network, no extra output.
LINE = "I missed the meeting because my calendar invited my previous version, and he never forwards anything."

def main():
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
