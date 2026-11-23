"""THE COPPER PLATE atas nama @cicihandayani (Akun 3) — NI22 Wave 7.

Plat tembaga ini dicetak sekali dan tidak boleh berubah setelahnya.
Karena itu program ini menguji platnya lebih dulu — header PNG dan
batas sisi — sebelum menggandakannya ke keluaran dan menguji ulang
hasil gandanya sampai terbukti sama persis.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

CONCEPT = "THE COPPER PLATE"
ACCOUNT = "@cicihandayani"
ACCOUNT_LABEL = "Akun 3"
BOUNTY = "news-image-20261122"
STORIES = 36
MAX_SIDE = 1024

MAGIC = b"\x89PNG\r\n\x1a\n"


def profile(path):
    """Profil berkas: (sha256 heksadesimal, ukuran dalam byte)."""
    h = hashlib.sha256()
    n = 0
    with path.open("rb") as src:
        while True:
            buf = src.read(16384)
            if not buf:
                break
            h.update(buf)
            n += len(buf)
    return h.hexdigest(), n


def dimensions(path):
    """Tarik lebar dan tinggi dari 33 byte pertama berkas PNG."""
    with path.open("rb") as src:
        first = src.read(33)
    if len(first) != 33:
        print("33 byte pertama tidak terbaca penuh.", file=sys.stderr)
        sys.exit(1)
    if first[0:8] != MAGIC:
        print("Signature PNG tidak sah.", file=sys.stderr)
        sys.exit(1)
    if first[12:16] != b"IHDR":
        print("Chunk IHDR tidak berada di awal.", file=sys.stderr)
        sys.exit(1)
    w, h = struct.unpack(">II", first[16:24])
    return w, h


def main():
    root = Path(__file__).resolve().parent
    plate = root / "entry.png"
    if not plate.is_file():
        print("entry.png tidak ada.", file=sys.stderr)
        return 1

    w, h = dimensions(plate)
    # Gerbang dimensi bersifat mutlak: satu piksel berlebih pun ditolak.
    if w > MAX_SIDE or h > MAX_SIDE:
        print(f"Plat {w}x{h} lebih besar dari pagu {MAX_SIDE}.", file=sys.stderr)
        return 1

    sha_src, size_src = profile(plate)

    out_path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_path.mkdir(parents=True, exist_ok=True)
    copy_path = out_path / "entry.png"
    copy_path.write_bytes(plate.read_bytes())

    sha_dst, size_dst = profile(copy_path)
    if sha_dst != sha_src or size_dst != size_src:
        print("Ganda plat tidak sama dengan plat asal.", file=sys.stderr)
        return 1

    print(f"Concept: {CONCEPT}")
    print(f"Account: {ACCOUNT} ({ACCOUNT_LABEL})")
    print(f"Bounty: {BOUNTY}")
    print("File: entry.png")
    print(f"Size: {size_src}")
    print(f"Dim: {w}x{h}")
    print(f"SHA256: {sha_src}")
    print(f"Stories: {STORIES}")
    print("Copy verified byte-identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
