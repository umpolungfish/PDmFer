"""
Setup script for PDmFer - Production-Ready PDF Embedding CLI Tool
"""
from setuptools import setup, find_packages


# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Read the requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]


setup(
    name="pdmfer",
    version="1.0.0",
    author="PDmFer Development Team",
    author_email="pdmfer@example.com",
    description="Production-Ready PDF Embedding CLI Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pdmfer/pdmfer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Multimedia :: Graphics :: Viewers",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pdmfer=pdmfer.cli.interface:main_cli",
        ],
    },
    keywords="pdf, embedding, cli, enterprise, document, security",
    project_urls={
        "Bug Reports": "https://github.com/pdmfer/pdmfer/issues",
        "Source": "https://github.com/pdmfer/pdmfer",
        "Documentation": "https://github.com/pdmfer/pdmfer/blob/main/README.md",
    },
)