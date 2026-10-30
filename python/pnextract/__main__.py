import os
import sys
from pathlib import Path

PACKAGE_DIR = Path(__file__).parent
BINARY_SUFFIX = ".exe" if os.name == "nt" else ""


def pnextract() -> None:
    os.execv(PACKAGE_DIR / f"pnextract{BINARY_SUFFIX}", sys.argv)


def voxel_image_process() -> None:
    os.execv(PACKAGE_DIR / f"voxelImageProcess{BINARY_SUFFIX}", sys.argv)


if __name__ == "__main__":
    pnextract()
