# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import tqdm
import gevent


def send(rq, pool=None, stream=False):
    if pool:
        return pool.spawn(rq.send, stream=stream)
    else:
        return gevent.spawn(rq.send, stream=stream)


def async_map(rq, stream=False, size=None, timeout=None):
    """Build asynchronous queries.

    Args:
    =====
        rq (grequests.get): grequests object
    """
    rqs = list(rq)
    jobs, ret = list(), list()
    pool = gevent.pool.Pool(size) if size else None
    loadings = len(rqs)
    pbar = tqdm.tqdm(total=loadings)
    for rq in rqs:
        jobs.append(send(rq, pool, stream=stream))
        pbar.update(n=1)
    pbar.close()
    gevent.joinall(jobs, timeout=timeout)
    for rq in rqs:
        ret.append(rq.response)

    return ret
