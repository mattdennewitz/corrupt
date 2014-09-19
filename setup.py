#!/usr/bin/env python

from distutils.core import setup

setup(
    name='corrupt',
    version='0.0.1',
    description="Python port of Recyclism's image corruption tool",
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    url='https://github.com/mattdennewitz/corrupt',
    requires=['click', 'Pillow'],
    scripts=['scripts/corrupt'],
)
