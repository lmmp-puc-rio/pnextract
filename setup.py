import os
import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py

class build_py(_build_py):
    def run(self):
        subprocess.run(["make"], check=True)

        pnextract_name = "pnextract" + (".exe" if os.name == "nt" else "")
        (Path("bin") / pnextract_name).rename(Path("python/pnextract/") / pnextract_name)

        voxel_image_process_name = "voxelImageProcess" + (".exe" if os.name == "nt" else "")
        (Path("bin") / voxel_image_process_name).rename(Path("python/pnextract/") / voxel_image_process_name)

        super().run()

setup(
    cmdclass={"build_py": build_py},
    package_dir={"": "python"},
    package_data={"pnextract": ["pnextract*", "voxelImageProcess*"]},
)
