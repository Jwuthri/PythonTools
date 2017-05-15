# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import dateutil.parser
import datetime
import numpy


def time2scds(tm):

    if isinstance(tm, str):
        tm = dateutil.parser.parse(tm)
        return tm.hour * 3600 + tm.minute * 60 + tm.second

    if isinstance(tm, datetime.datetime):
        return tm.hour * 3600 + tm.minute * 60 + tm.second

    if isinstance(tm, int):
        return tm

    if isinstance(tm, numpy.int64):
        return time2scds(int(tm))

    else:
        message = "Format of time {} unknow".format(type(tm))
        raise Time2ScdsException(message)


def scds2time(scd):

    if isinstance(scd, str):
        try:
            return scds2time(int(scd))
        except TypeError as e:
            raise Scds2TimeException(e)

    if isinstance(scd, int):
        return str(datetime.timedelta(seconds=scd))

    if isinstance(scd, datetime.datetime):
        return str(scd.date())

    if isinstance(scd, numpy.int64):
        return scds2time(int(scd))

    else:
        message = "Format of seconds {} unknow".format(type(scd))
        raise Scds2TimeException(message)


class Scds2TimeException(Exception):

    def __call__(self, *args):
        return self.__class__(*args)


class Time2ScdsException(Exception):

    def __call__(self, *args):
        return self.__class__(*args)
