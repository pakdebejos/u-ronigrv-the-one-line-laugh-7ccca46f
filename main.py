"""Stressed About Relaxing: one-line laugh entry.

The program writes one funny line - a single sentence of at most 200
characters (115 characters) - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR
locally, /output in the grader). The text is a fixed constant with no
trailing newline, so both of the grader's runs write byte-identical output.
"""
import os

LINE = "I asked my AI assistant to remind me to relax, so now it pings me every hour to say I seem stressed about relaxing."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
