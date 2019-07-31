#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.rst").read()
doclink = """
Documentation
-------------

The full documentation is at http://ansible-lint-to-junit-xml.rtfd.org."""
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="ansible-lint-to-junit-xml",
    version="0.1.0",
    description="Convert ansible-lint outputs to a jUnit valid xml tests result file",
    long_description=readme + "\n\n" + doclink + "\n\n" + history,
    author="Andre Ferreira",
    author_email="andre.ferreira.v2@gmail.com",
    url="https://github.com/andreferreirav2/ansible-lint-to-junit-xml",
    packages=["ansiblelinttojunitxml"],
    package_dir={"ansible-lint-to-junit-xml": "ansiblelinttojunitxml"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ansible-lint-to-junit-xml = ansiblelinttojunitxml.ansiblelinttojunitxml:main"
        ]
    },
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords=["ansible", "lint", "junit", "report"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
