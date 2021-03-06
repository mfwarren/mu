# -*- coding: utf-8 -
#
# This file is part of mu released under the MIT license.
# See the NOTICE for more information.

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from mu import __version__


CLASSIFIERS = [
    'Development Status :: 1 - Alpha',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet :: WWW/HTTP']

# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

# read dev requirements
fname = os.path.join(os.path.dirname(__file__), 'requirements_test.txt')
with open(fname) as f:
    tests_require = [l.strip() for l in f.readlines()]

if sys.version_info[:2] < (3, 3):
    tests_require.append('mock')

class PyTestCommand(TestCommand):
    user_options = [
        ("cov", None, "measure coverage")
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        if self.cov:
            self.test_args += ['--cov', 'mu']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='mu',
    version=__version__,

    description='Web API Framework for Amazon Lambda',
    long_description=long_description,
    author='Matt Warren',
    author_email='matt.warren@gmail.com',
    license='MIT',
    url='http://github.com/mfwarren/mu',

    classifiers=CLASSIFIERS,
    zip_safe=False,
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,

    tests_require=tests_require,
    cmdclass={'test': PyTestCommand},

    entry_points="""
    [console_scripts]
    mu=mu.app.consoleapp:run
    """
)
