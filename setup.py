# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
from setuptools import setup

REQUIREMENTS = ["numpy", "pandas", "tqdm", "grequests", "flask"]

setup(
    name='pytools',
    packages=['pytools'],
    version='0.1.0',
    url="https://github.com/Jwuthri/PythonTools.git",
    download_url ="https://github.com/Jwuthri/PythonTools/archive/0.1.tar.gz",
    description="Some snippets for python",
    author="Julien WUTHRICH",
    install_requires=REQUIREMENTS,
    license='MIT license',
    keywords=["date", "time", "log", "pandas", "list", "requests"],
    classifiers=[]
)
