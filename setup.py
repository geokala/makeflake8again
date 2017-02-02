# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='makeflake8again',
    version='.6.6.6',
    description='Making flake into a really 8 thing again!',
    long_description='makeflake8again',
    packages=[
        'flake8_again',
    ],
    install_requires=[
        'flake8',
    ],
    entry_points={
        'flake8.extension': ['FLK8AGN0 = flake8_again:Flake8Again', ],
    },
)
