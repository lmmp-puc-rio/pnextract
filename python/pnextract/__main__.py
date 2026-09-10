import os
import sys
from pathlib import Path

PACKAGE_DIR = Path(__file__).parent


def pnextract() -> None:
    os.execv(PACKAGE_DIR / "pnextract", sys.argv)


def voxel_image_process() -> None:
    os.execv(PACKAGE_DIR / "voxelImageProcess", sys.argv)


if __name__ == "__main__":
    pnextract()
