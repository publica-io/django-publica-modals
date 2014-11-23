#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import modals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = modals.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-publica-modals',
    version=version,
    description="""A pattern and views for serving up Modal windows; content managed by Django""",
    long_description=readme + '\n\n' + history,
    author='Daryl Antony',
    author_email='daryl@commoncode.io',
    url='https://github.com/DarylAntony/django-publica-modals',
    packages=[
        'modals',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-publica-modals',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
