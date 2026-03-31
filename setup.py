import re

from setuptools import find_packages, setup

# Read version without importing the package
with open("funcbox/__init__.py") as f:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        f.read(),
        re.MULTILINE,
    )
    version = version_match.group(1) if version_match else "0.0.0"

def get_pypi_readme():
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    # Remove sections marked for GitHub only
    readme = re.sub(r"\[//\]: # \(PYPI_FILTER_START\)[\s\S]*?\[//\]: # \(PYPI_FILTER_END\)\n*", "", readme)
    # Uncomment sections marked for PyPI only
    return re.sub(r"<!-- PYPI_UNCOMMENT_START\n([\s\S]*?)\nPYPI_UNCOMMENT_END -->", r"\1", readme)

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
    python_requires=">=3.6",
)
