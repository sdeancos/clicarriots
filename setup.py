#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clicarriots',
    version='0.2.0',
    description='The unofficial simple client for carriots platform (in progress) (python 2.x/3.x)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='carriots,iot,internet of things',
    author='Samuel de Ancos',
    author_email='sdeancos@gmail.com',
    url='https://github.com/sdeancos/clicarriots',
    download_url='https://github.com/sdeancos/clicarriots/tarball/0.2.0',
    packages=['clicarriots'],
)
