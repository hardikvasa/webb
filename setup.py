#!/usr/bin/env python

#
# Copyright 2012 BloomReach, Inc.
#
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

from setuptools import setup, find_packages

__author__ = "Hardik Vasa"
__copyright__ = "Copyright 2015 @Z Series Innovations"
__license__ = "http://www.apache.org/licenses/LICENSE-2.0"
__version__ = "0.9"
__maintainer__ = __author__
__status__ = "Development"

setup(name='webb',
      version=__version__,
      description='An all-in-one Web Crawler, Web Parser and Web Scrapping library!',
      author=__author__,
      license=__license__,
      url='https://github.com/hardikvasa/webb',
      py_modules=['webb'],
      scripts=['webb', 'webb.py'], # Added webb.py as script for backward compatibility
    )
