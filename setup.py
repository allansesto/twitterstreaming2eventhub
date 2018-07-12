#!/usr/bin/env python
import re
import os
import ast

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

long_description = 'Stream feed from Twitter to Azure Event Hub'
if os.path.exists('README.md'):
    long_description = open('README.md', encoding='utf-8').read()

with open('TS2MAEV.py', 'r') as fd:
    version = re.search(
        r'^_TS2MAEV_VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

setup(name='TS2MAEV',
    version=version,
    description='Stream feed from Twitter to Azure Event Hub',
    long_description=long_description,
    author='Allan Sesto',
    author_email='allansesto@me.com',
    platforms='any',
    py_modules=['TS2MAEV'],
    entry_points={
        'console_scripts': 'TS2MAEV=TS2MAEV:main',
    },
    install_requires=[
        'argparse',
        'azure-servicebus',
        'tweepy==3.3.0'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    keywords='stream feed twitter azure eventhub',
)
