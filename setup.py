import re
from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent


# Read version without importing the package
with open(ROOT / "funcbox" / "__init__.py", encoding="utf-8") as f:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        f.read(),
        re.MULTILINE,
    )
    version = version_match.group(1) if version_match else "0.0.0"


def get_pypi_readme():
    try:
        with open(ROOT / "README_PYPI.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "funcBox - A highly-optimized functional utility box with various helper functions. See https://github.com/funcbox-i3/funcbox for docs."


setup(
    name="funcbox",
    version=version,
    packages=find_packages(),
    description="A functional utility box with various functions",
    long_description=get_pypi_readme(),
    long_description_content_type="text/markdown",
    author="Aditya Prasad S",
    author_email="plutoniumx502@gmail.com",
    url="https://github.com/funcbox-i3/funcbox",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
