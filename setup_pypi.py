#!/usr/bin/env python3
# encoding: utf-8

import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCPU_RETRO70Z_ID0000",
    version="0.1.0",
    author="Scott McCallum (https github.com scott91e1 CV)",
    author_email="262464@195387.com",
    description="Virtual CPUs Support For Python",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/PyCPU/PyCPU_RETRO70Z_ID0000",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
