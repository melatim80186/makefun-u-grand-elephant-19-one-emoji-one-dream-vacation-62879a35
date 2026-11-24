"""One Emoji, One Dream Vacation — make.fun entry.

Writes a single emoji — the reviewed winner, U+1F338 CHERRY BLOSSOM —
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

EMOJI = "\U0001F338"  # 🌸 CHERRY BLOSSOM


def main() -> None:
    text = EMOJI
    assert len(text) == 1, f"entry must be exactly one code point, got {len(text)}"
    assert text == "\U0001F338", "entry must match the reviewed winner exactly"
    assert "\n" not in text, "entry must contain no newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
