# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


version = re.search(
    r"__version__ = ['\"](.*)['\"]",
    open("aldryn_accordion/__init__.py").read()
).group(1)


REQUIREMENTS = [
    'aldryn-boilerplates>=0.6',
]


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]


setup(
    name='aldryn-accordion',
    version=version,
    description='Create accordion structure and put plugins of your choice in it.',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-accordion',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
