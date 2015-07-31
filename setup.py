#!/usr/bin/env python

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


setup(
      name='webb',
      version=0.9,
      description='An all-in-one Web Crawler, Web Parser and Web Scrapping library!',
      author='Hardik Vasa',
      maintainer='Hardik Vasa',
      author_email='hnvasa@gmail.com',
      description='An all-in-one Web Crawler, Web Parser and Web Scrapping library!',
      long_description = read('README.md'),
      license= "Apache License, Version 2.0",
      url='https://github.com/hardikvasa/webb',
      status='Development',
      py_modules=['webb'],
      scripts=['webb/webb.py'],
      )
