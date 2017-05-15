# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import string


def format_str(bad_str, hard=False):
    try:
        if hard:
            for char in string.punctuation:
                bad_str = bad_str.replace(char, '')

        return " ".join(bad_str.split()).lower()
    except TypeError as te:
        return bad_str
