#!/usr/bin/env python

from setuptools import setup

setup(
    name='helloworld-zacthewise2',  # pip install
    version='0.0.1',
    description='Say hello!',
    py_modules=["helloworld"],  # import
    package_dir={'': 'src'},  # code is in src dir
    scripts=['helloworld'],
    entry_points={
        'console_scripts': [
            'hello-world=src:main',
        ]
    }
)
