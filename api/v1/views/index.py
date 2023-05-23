#!/usr/bin/python3
"""views index"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    '''Status of my API'''
    return jsonify({'status': 'ok'})
