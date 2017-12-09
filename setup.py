#!/usr/bin/env python
"""Setup script for act
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='act',
    version='0.1.0',
    description='Attakei Command-line Tools',
    long_description=long_description,
    url='https://github.com/attakei/act',
    author='Kazuya Takei',
    author_email='attakei@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': [],
    },
    package_data={
    },
    data_files=[],
    entry_points={
    },
)
