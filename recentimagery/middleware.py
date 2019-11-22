"""MIDDLEWARE"""
from functools import wraps
import json
import logging
from flask import request
from recentimagery.routes.api import error


def get_recent_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            lat = request.args.get('lat')
            lon = request.args.get('lon')
            start = request.args.get('start')
            end = request.args.get('end')
            sort_by = request.args.get('sort_by', None)
            bmin = request.args.get('min', None)
            bmax = request.args.get('max', None)
            opacity = request.args.get('opacity', 1.0)
            bands = request.args.get('bands', None)
            if not lat or not lon or not start or not end:
                return error(status=400, detail='[RECENT] Parameters: (lat, lon. start, end) are needed')
        kwargs["lat"] = lat
        kwargs["lon"] = lon
        kwargs["start"] = start
        kwargs["end"] = end
        kwargs["sort_by"] = sort_by
        kwargs["bmin"] = bmin
        kwargs["bmax"] = bmax
        kwargs["opacity"] = float(opacity)
        kwargs["bands"] = bands
        return func(*args, **kwargs)

    return wrapper


def get_recent_tiles(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            logging.info(f"[Middleware POST] {request.get_json()}")
            data_array = request.get_json().get('source_data', [])
            bands = request.args.get('bands', None)
            if not bands:
                bands = request.get_json().get('bands', None)
            bmin = request.args.get('min', 0)
            bmax = request.args.get('max', None)
            opacity = request.args.get('opacity', 1.0)
            if not data_array:
                return error(status=400, detail='[TILES] Some parameters are needed')
        kwargs["bands"] = bands
        kwargs["data_array"] = data_array
        kwargs["bmin"] = bmin
        kwargs["bmax"] = bmax
        kwargs["opacity"] = float(opacity)
        return func(*args, **kwargs)

    return wrapper


def get_recent_thumbs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if request.method == 'POST':
            data_array = request.get_json().get('source_data', [])
            bands = request.args.get('bands', None)
            if not bands:
                bands = request.get_json().get('bands', None)
            bmin = request.args.get('min', 0)
            bmax = request.args.get('max', None)
            opacity = request.args.get('opacity', 1.0)
            if not data_array:
                return error(status=400, detail='[THUMBS] Some parameters are needed')
        kwargs["data_array"] = data_array
        kwargs["bands"] = bands
        kwargs["bmin"] = bmin
        kwargs["bmax"] = bmax
        kwargs["opacity"] = float(opacity)
        return func(*args, **kwargs)
    return wrapper
