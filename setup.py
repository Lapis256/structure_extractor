from setuptools import setup
import platform
import re


if platform.machine() != "aarch64":
    raise RuntimeError("can only be installed on aarch64.")


version = ""
with open("extractor/__init__.py") as f:
    version = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")


setup(
    name="structure_extractor",
    author="Lapis256",
    url="https://github.com/Lapis256/structure_extractor",
    version=version,
    packages=["extractor"],
    install_requires=["bedrock@git+https://github.com/Lapis256/bedrock.git@master"],
    python_requires=">=3.8.0",
)
