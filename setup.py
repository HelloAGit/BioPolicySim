from setuptools import setup, find_packages

setup(
    name="biopolicysim",
    version="0.1.0",
    packages=find_packages(where="."),
    package_dir={"": "."},
    install_requires=[],
    python_requires=">=3.9",
)
