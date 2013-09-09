#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name = 'renormimg',
    version = '0.0.1',
    author = 'Rich Wareham',
    author_email = 'rjw57@cantab.net',
    description = 'Renormalise a set of images on the command line',
    license = 'MIT',
    packages = find_packages(),
    entry_points = { 'console_scripts': [
        'renormimg = renormimg.tool:main',
    ] },
    install_requires = [ 'docopt', 'numpy', 'matplotlib', 'PIL', ],
)

# vim:sw=4:sts=4:et

