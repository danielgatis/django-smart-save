#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='django-smart-save',
    version='0.0.11',
    description='Automatically validates when you call your model’s save()',
    author='Daniel Gatis Carrazzoni',
    author_email='danielgatis@gmail.com',
    url='https://github.com/danielgatis/django-smart-save',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
