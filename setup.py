# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in it_support/__init__.py
from it_support import __version__ as version

setup(
	name='it_support',
	version=version,
	description='Sending IT and ERP support tickets',
	author='Botan Burhan Abdullah',
	author_email='botan.b.abdullah@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
