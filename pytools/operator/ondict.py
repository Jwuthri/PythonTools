# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import itertools


def dict_union(*dicts):
    return dict(itertools.chain.from_iterable(dct.items() for dct in dicts))


def dict_equals(d1, d2):
    return d1 == d2


def dict_intersection(d1, d2):
    return d1.keys() & d2.keys()


def dict_difference(d1, d2):
    return d1.keys() - d2.keys()


def dict_min_value(dct):
    return min(dct.items(), key=lambda x: x[0])[1]


def dict_max_value(dct):
    return max(dct.items(), key=lambda x: x[0])[1]


def dict_min_key(dct):
    return min(dct.items(), key=lambda x: x[0])[0]


def dict_max_key(dct):
    return max(dct.items(), key=lambda x: x[0])[0]
