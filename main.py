"""news-image-20261125 entry program.

The front-page image is stored beside this file as base64, split into
entry.png.b64.0 and entry.png.b64.1 (one file was too large to push in
a single API call). This program joins the parts, decodes them, and
writes the PNG to the output directory. Standard library only.

Run locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The grader runs it with /output as the output directory and no network.
"""
import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    parts = []
    for name in ("entry.png.b64.0", "entry.png.b64.1"):
        path = HERE / name
        if not path.is_file():
            raise SystemExit(f"missing image part: {name}")
        parts.append(path.read_text().strip())
    data = base64.b64decode("".join(parts))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("decoded bytes are not a PNG")
    target = OUT / "entry.png"
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
