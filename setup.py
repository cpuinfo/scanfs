from os import name
from setuptools import setup, find_packages

setup(
    name="scanfs",
    extra_requires=dict(tests=["pytest"]),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
