# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='study_visit_schedule',
    version='0.1',
    author=u'Salahdin',
    author_email='salahdinjemal@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/salahdin/study_visit_schedule',
    license='GPL license, see LICENSE',
    description='study subject',
    long_description=README,
    zip_safe=False,
    keywords='django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
