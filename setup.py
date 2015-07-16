#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "edtp",
  version = "1.0",
  packages = [],
  scripts = ["scripts/edtp"],
  install_requires = ["numpy", "requests", "docopt"],
  author = "Felix \"KoffeinFlummi\" Wiegand",
  author_email = "koffeinflummi@gmail.com",
  description = "Command line Elite: Dangerous trade route finder.",
  long_description = read("README.md"),
  license = "MIT",
  keywords = "elite dangerous games game",
  url = "https://github.com/KoffeinFlummi/edtb",
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Utilities"
  ]
)
