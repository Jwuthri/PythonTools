# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import flask


def not_found(error, metainfo=None):
    body = {
        "success": False,
        "error": error
    }
    if metainfo:
        body.update(metainfo)

    return flask.make_response(flask.jsonify(body), 404)


def bad_request(error, metainfo=None):
    body = {
        "success": False,
        "error": error
    }
    if metainfo:
        body.update(metainfo)

    return flask.make_response(flask.jsonify(body), 400)


def created_resource(data):
    body = {
        "success": True,
        "result": data
    }

    return flask.make_response(flask.jsonify(body), 201)



def processing(data):
    body = {
        "success": True,
        "result": data
    }

    return flask.make_response(flask.jsonify(body), 102)


def busy(data):
    body = {
        "success": False,
        "result": data
    }

    return flask.make_response(flask.jsonify(body), 503)


def get_resource(data):
    body = {
        "success": True,
        "result": data
    }

    return flask.make_response(flask.jsonify(body), 200)
