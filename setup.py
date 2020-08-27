from setuptools import setup, find_packages
from os import path
from src import __version__ as version

here = path.abspath(path.dirname(__file__))


extras = {}

# Get the long description from the README file
if path.exists("README.md"):
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        extras["long_description"] = f.read()
    extras["long_description_content_type"] = "text/markdown"


setup(
    name="workflows_engine",
    version=version,
    author="UDES",
    # author_email="",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="udes",
    package_dir={"workflows_engine": "src"},
    packages=["workflows_engine"],
    python_requires=">=3.5, <4",
    install_requires=["json"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={
        "dev": [],
        "test": ["coverage", "pytest"],
        "doc": ["sphinx", "recommonmark", "pytest"],
    },
    **extras
)
