#!/usr/bin/env python

from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Full list of classifiers can be found here:
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLS = (
  'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
  'Development Status :: 3 - Alpha',
  'Environment :: Web Environment',
  'Framework :: Jupyter',
  'Intended Audience :: Science/Research',
  'Operating System :: POSIX',
  'Programming Language :: Python',
  'Topic :: Text Processing :: Markup',
)
REQS = (
    'nbconvert >= 5.0.0',
    'nbformat >= 4.0.0',
    'click >= 7.0',
    'pyyaml >= 5.0.0',
)
REQS_TESTS = (
    'pytest >= 4.0.0',
    'coverage >= 4.0.0',
)
REQS_EXTRA = {
    'tests': REQS_TESTS,
}
CONSOLE_SCRIPTS = (
    'nbbook=nbbook.cmd:cli',
)
SRC = 'src'
TESTS = ('*.tests', 'tests.*', '*.tests.*', 'tests')

setup(
    name='nbbook',
    description='Export groups of jupyter notebooks as a full Book',
    version='0.1',
    author='Michal Grochmal',
    author_email='NmiOkeS@PgroAchmalM.org',
    license='GNU General Public License, version 3 or later',
    url='https://github.com/grochmal/nbbook',
    long_description=read('README'),
    packages=find_packages(SRC, exclude=TESTS),
    package_dir={'': SRC},
    include_package_data=True,
    classifiers=CLS,
    install_requires=REQS,
    tests_require=REQS_TESTS,
    extras_require=REQS_EXTRA,
    entry_points={'console_scripts': CONSOLE_SCRIPTS}
)

