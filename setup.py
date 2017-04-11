#!/usr/bin/env python
from setuptools import setup

VERSION = '3.0.3'
DESCRIPTION = "Dynamic Pybloom: A Suite of Probabilistic Data Structures"
LONG_DESCRIPTION = """
``dynamic-pybloom`` is a fork of the popular https://travis-ci.org/jaybaird/python-bloomfilter repo module
that includes a Bloom Filter data structure, an implementation of the Scalable Bloom Filter[1] and
a new implementation of the Dynamic Bloom Filter[2].
"""

CLASSIFIERS = filter(None, map(str.strip,
"""
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Operating System :: OS Independent
Topic :: Utilities
Topic :: Database :: Database Engines/Servers
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
    name="dynamic_pybloom",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('data structures', 'bloom filter', 'bloom', 'filter',
              'probabilistic', 'set'),
    author="srf5132",
    author_email="srf5132@gmail.com",
    url="http://github.com/srf5132/dynamic-pybloom/",
    license="MIT License",
    platforms=['any'],
    test_suite="dynamic_pybloom.tests",
    zip_safe=True,
    install_requires=['bitarray>=0.3.4'],
    packages=['dynamic_pybloom']
)
