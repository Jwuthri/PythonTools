# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import importlib


def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['--trusted-host', 'pypi.python.org', 'install', package])
    finally:
        try:
            globals()[package] = importlib.import_module(package)
        except:
            print("package {} not installed".format(package))


def get_all_packages():
    lst_packages = list()
    with open('requirements.txt') as fp:
        for line in fp:
            lst_packages.append(line.split("=")[0].lower())

    return lst_packages


if __name__ == '__main__':
    lst_install_requires = get_all_packages()
    for module in lst_install_requires:
        install_and_import(module)
    print('END')
