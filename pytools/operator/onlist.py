# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""

def change_list_type(item, func):

    if isinstance(item, list):
        return [change_list_type(x, func) for x in item]

    else:
        message = "Type of item {} unknow".format(type(item))
        raise ListException(message)

    return func(item)


def pairwise(lst, last=True):
    """Build pair data with all list values.

    Args:
    =====
        last (bool): pair between first and last
    """
    res = [(x, y) for x, y in zip(lst, lst[1:])]
    if last:
        res = res + [
            (x, y) for x, y in zip(lst[-1:], lst[:1])
        ]

    return res


def lists_equals(l1, l2):
    return l1 == l2


def lists_intersection(l1, l2):
    return set(l1) & set(l2)


def lists_symetric_difference(l1, l2):
    return set(l1) ^ set(l2)


def lists_difference(l1, l2):
    return set(l1) - set(l2)


class ListException(Exception):

    def __call__(self, *args):
        return self.__class__(*args)
