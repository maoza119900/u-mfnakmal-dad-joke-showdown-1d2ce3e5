"""Dad Joke Showdown entry.

Writes a single dad joke to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``.
Fully deterministic: the joke is a fixed string constant. No time,
no randomness, no network, no file traversal, no reading of the
program's own source or git history.
"""

import os

JOKE = "I told my wife she should embrace her mistakes. She gave me a hug."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
