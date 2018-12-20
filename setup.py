#!/usr/bin/python
import os
from setuptools import setup

this_dir = os.path.realpath(os.path.dirname(__file__))
long_description = open(os.path.join(this_dir, 'README.md'), 'r').read()

requirements = [
    'httplib2',
    'oauth2==1.9.0.post1',
    'simplejson',
    'requests',
    'requests_oauthlib',
]

test_requirements = [
    'pytest',
]

setup(
    name='pyetsy',
    version='0.5.0',
    author='Dan McKinley & Fulfil.IO Inc.',
    author_email='dan@etsy.com,support@fulfil.io',
    description='Python access to the Etsy API',
    license='GPL v3',
    keywords='etsy api handmade',
    packages=['etsy'],
    python_requires=">=3.5",
    long_description=long_description,
    test_suite='test',
    install_requires=requirements,
    package_data={'etsy': ['README.md']},
)
