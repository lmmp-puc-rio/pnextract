import shutil
import subprocess
from pathlib import Path

from setuptools import Distribution, setup
from setuptools.command.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py

BINARIES = (
    "pnextract",
    "voxelImageProcess",
)


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


class BuildPy(build_py):
    def run(self):
        binaries = [Path("bin") / name for name in BINARIES]

        if not all(path.is_file() for path in binaries):
            subprocess.run(["make"], check=True)

        super().run()

        package_dir = Path(self.build_lib) / "pnextract"
        package_dir.mkdir(parents=True, exist_ok=True)

        for binary in binaries:
            shutil.copy2(binary, package_dir / binary.name)


class BdistWheel(bdist_wheel):
    def get_tag(self):
        _, _, platform = super().get_tag()
        return "py3", "none", platform


setup(
    distclass=BinaryDistribution,
    cmdclass={
        "build_py": BuildPy,
        "bdist_wheel": BdistWheel,
    },
)
