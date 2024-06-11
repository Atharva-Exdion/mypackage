# setup.py

from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Atharva Deshmukh",
    author_email="Atharva@Exdion.Dev",
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    python_requires='>=3.6',
)
