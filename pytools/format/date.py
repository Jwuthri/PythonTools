# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import time
import datetime
import dateutil.parser


def val2date(val, nformat="%d-%m-%Y"):

    if isinstance(val, str):
        return dateutil.parser.parse(val).date().strftime(nformat)

    if isinstance(val, datetime.date):
        return val.strftime(nformat)

    if isinstance(val, datetime.datetime):
        return val.strftime(nformat)

    else:
        message = "Format of date {} unknow".format(type(val))
        raise Val2DateException(message)


def dateWscds(dt, scd):

    def cast_scd(scd):
        try:
            return int(scd)
        except TypeError as te:
            message = "Unknow type {} for scd".format(type(scd))
            raise DateWScdsException(message)

    def make_timestamp(dt, scd):
        try:
            return time.mktime(dt.timetuple()) + scd
        except TypeError as te:
            raise DateWScdsException(te)

    if isinstance(dt, str):
        dt = dateutil.parser.parse(dt).date()

    if isinstance(scd, str):
        scd = cast_scd(scd)

    return datetime.datetime.fromtimestamp(make_timestamp(dt, scd))


def range_date(start, end):
    liste_date = list()
    while(end >= start):
        liste_date.append(start)
        start = start + datetime.timedelta(days=1)

    return liste_date


class Val2DateException(Exception):

    def __call__(self, *args):
        return self.__class__(*args)


class DateWScdsException(Exception):

    def __call__(self, *args):
        return self.__class__(*args)
