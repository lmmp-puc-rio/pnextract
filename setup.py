import shutil
import subprocess
import sys
from pathlib import Path

from packaging.tags import sys_tags
from setuptools import Distribution, setup
from setuptools.command.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py

BINARIES = (
    "pnextract",
    "voxelImageProcess",
)
WINDOWS_WHEEL = sys.platform == "win32"
BINARY_SUFFIX = ".exe" if WINDOWS_WHEEL else ""


class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True


class BuildPy(build_py):
    def run(self):
        binaries = [Path("bin") / f"{name}{BINARY_SUFFIX}" for name in BINARIES]

        if not all(path.is_file() for path in binaries):
            command = (
                ["cmd.exe", "/d", "/c", "msys2", "-c", "make mgw"]
                if WINDOWS_WHEEL
                else ["make"]
            )
            subprocess.run(command, check=True)

        super().run()

        package_dir = Path(self.build_lib) / "pnextract"
        package_dir.mkdir(parents=True, exist_ok=True)

        for binary in binaries:
            shutil.copy2(binary, package_dir / binary.name)


class BdistWheel(bdist_wheel):
    def get_tag(self):
        _, _, platform = super().get_tag()
        if sys.platform.startswith("linux"):
            platform = next(
                tag.platform for tag in sys_tags() if tag.platform.startswith("manylinux")
            )
        return "py3", "none", platform


setup(
    distclass=BinaryDistribution,
    cmdclass={
        "build_py": BuildPy,
        "bdist_wheel": BdistWheel,
    },
)
