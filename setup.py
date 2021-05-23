# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup


with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")


setup(
    name="115sha1link",
    version="0.1.0",
    author="Xavier-Lam",
    author_email="xavierlam7@hotmail.com",
    url="https://github.com/Xavier-Lam/115sha1link",
    py_modules=["115sha1link"],
    keywords=["115", "sha1"],
    long_description=long_description,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
    ],
    entry_points = dict(
        console_scripts=[
            "115sha1link = 115sha1link:main"
        ],              
    ),
)