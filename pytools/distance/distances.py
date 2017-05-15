# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import numpy


class Distance(object):

    def __init__(self, origin, destination):
        self.radius = 6372797
        self.origin = origin
        self.destination = destination

    def loc2array(self, loc):
        lat, lon = loc

        return numpy.array([lat, lon])

    def euclidean(self):
        o = self.loc2array(self.origin)
        d = self.loc2array(self.destination)

        return numpy.linalg.norm(d - o)

    def _haversine(self, o, d):
        o_rad = numpy.radians(o)
        d_rad = numpy.radians(d)

        lat_arc, lon_arc = abs(o_rad - d_rad)
        a = numpy.sin(lat_arc * 0.5)**2 + (
            numpy.cos(o_rad[0]) *
            numpy.cos(d_rad[0]) *
            numpy.sin(lon_arc * 0.5)**2
        )
        c = 2 * numpy.arcsin(numpy.sqrt(a))

        return self.radius * c

    def haversine(self):
        o = self.loc2array(self.origin)
        d = self.loc2array(self.destination)

        return self._haversine(o, d)
