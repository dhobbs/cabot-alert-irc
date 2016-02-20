#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cabot-alert-irc',
      version='1.0.0',
      description='An IRC alert plugin for Cabot by Arachnys',
      author='Arachnys',
      author_email='info@arachnys.org',
      url='http://cabotapp.com',
      packages=find_packages(),
      download_url= 'https://github.com/dhobbs/cabot-alert-irc/tarball/1.0.0',
      install_requires=[
            'irc>=14.0'
      ]
     )
