# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import logging


class LogFile(object):

    def __init__(self, logfile, level, show=False, fmt="%(message)s"):
        self.logfile = logfile
        self.level = level
        self.fmt = fmt
        self.logger = logging.getLogger(logfile)
        self.logger.setLevel(level)
        self.hfile()
        if show:
            self.hstream()

    def hfile(self):
        hdlr = logging.FileHandler(self.logfile, encoding="utf-8")
        hdlr.setLevel(self.level)
        hdlr.setFormatter(logging.Formatter(self.fmt))
        self.logger.addHandler(hdlr)

    def hstream(self):
        hdlr = logging.StreamHandler()
        hdlr.setLevel(self.level)
        hdlr.setFormatter(logging.Formatter(self.fmt))
        self.logger.addHandler(hdlr)

    def log(self, level, msg):
        self.logger.log(level, msg)

    def kill(self):
        for hdlr in self.logger.handlers:
            self.logger.removeHandler(hdlr)
