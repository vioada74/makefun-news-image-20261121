"""Copy the entry image to the output directory.

The entry is a pre-rendered PNG (entry.png, next to this file) that sums
up the world news of Saturday 21 November 2026. This program only copies
it to $MAKEFUN_OUTPUT_DIR/entry.png, so both runs write identical bytes.
Standard library only; no network.
"""

import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # Fail loudly on a partial copy instead of shipping a broken file.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
