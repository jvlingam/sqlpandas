#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for sqlpandas.

    This file was generated with PyScaffold 2.5.6, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup


def setup_package():
    setup(name='sqlpandas',
			version='0.1',
			author = 'Vijay Lingam',
			author_email = 'jvlingam@gmail.com',
			url = 'https://github.com/jvlingam/SQLpandas',
			description = "Native SQL Wrapper for Pandas",
			license="VijayLingam",
			platforms='All',
			long_description = """\
			-	This module accepts only select statement in SQL and accepts only one condition in this version.
			-	Multiple columns select, single column select and all columns select options are available.
			-	Also note, LIKE parameters, GroupBy option doesn't work in this version.
			""",
			include_package_data=True,
			packages = ['sqlpandas'],
			setup_requires=['pandas'])


if __name__ == "__main__":
    setup_package()
