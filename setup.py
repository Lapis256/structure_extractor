from setuptools import setup
import sys
import re

if not sys.prefix.startswith("/data/data/com.termux/files/"):
    raise RuntimeError("can install only with termux")

version = ""
with open("extractor/__init__.py") as f:
    version = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")


setup(
    name="extractor",
    author="Lapis256",
    url="https://github.com/Lapis256/structure_extractor",
    version=version,
    packages=["extractor"],
    install_requires=["bedrock@git+https://github.com/Lapis256/bedrock.git@master"],
    python_requires=">=3.8.0",
)
