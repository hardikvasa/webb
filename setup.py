#!/usr/bin/env python

from setuptools import setup

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Super S3 command line tool, setup.py
"""

import sys
from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
	
	
setup(
      name='webb',
      version='0.9.2.5',
      description='An all-in-one Web Crawler, Web Parser and Web Scrapping library!',
      author='Hardik Vasa',
      maintainer='Hardik Vasa',
      author_email='hnvasa@gmail.com',
      long_description=long_description,
      license="Apache License, Version 2.0",
      url='https://github.com/hardikvasa/webb',
      keywords='scraper crawler spider webb',
	  classifiers=[
	    'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'License :: OSI Approved :: Apache Software License',

        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
	  ],
	  zip_safe=False,
      packages=['webb'],
	  )
