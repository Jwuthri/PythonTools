# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import time
import logging
import functools
import multiprocessing as mp

import pandas as pd

import pytools


def logged(func=None, level=logging.DEBUG, name=None, msg=None):

    if func is None:
        return functools.partial(logged, level=level, name=name, msg=msg)

    logger = name if name else pytools.logfile.logger.LogFile(
        func.__name__ + ".log", logging.INFO)
    logmsg = msg if msg else func.__name__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        msg = ":".join([str(func.__name__), str(end - start)])
        logger.log(level, logmsg)
        logger.log(level, msg)

        return result

    return wrapper


def unique(func, cols=None):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, pd.DataFrame):
            if cols:
                return result.drop_duplicates(
                    subset=cols
                ).reset_index(drop=True)
            else:
                return result.drop_duplicates().reset_index(drop=True)
        else:
            return result

    return wrapper


def mp_func(func):

    def temp(_):
        def apply(args, ignore_result=False):
            res = []
            if args:
                if not mp.current_process().daemon:
                    pol = mp.pool.Pool(mp.cpu_count())
                    lst_res = pol.map(func, args)
                    pol.terminate()
                    pol.join()
                else:
                    lst_res = map(func, args)
                if ignore_result:
                    return None
                for a_res in lst_res:
                    res.extend(a_res)

            return res
        return apply

    return temp
