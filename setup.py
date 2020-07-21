# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in renovation_service_provider_manager/__init__.py
from renovation_service_provider_manager import __version__ as version

setup(
	name='renovation_service_provider_manager',
	version=version,
	description='The Manager App to be installed in the main site in Agents Bench',
	author='Leam Technology Systems',
	author_email='info@leam.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
