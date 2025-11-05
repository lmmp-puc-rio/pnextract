import os
import subprocess
import sys

from pathlib import Path


PNEXTRACT_PATH = Path(__file__).parent / ("pnextract" + (".exe" if os.name == "nt" else ""))
VOXEL_IMAGE_PROCESS_PATH = Path(__file__).parent / ("voxelImageProcess" + (".exe" if os.name == "nt" else ""))


def pnextract() -> None:
    completed_process = subprocess.run([PNEXTRACT_PATH, *sys.argv[1:]])
    sys.exit(completed_process.returncode)


def voxel_image_process() -> None:
    completed_process = subprocess.run([VOXEL_IMAGE_PROCESS_PATH, *sys.argv[1:]])
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    pnextract()
