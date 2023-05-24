#!/usr/bin/python3
'''Handles all RESTful API actions for `State` objects'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State

@app_views.route('/states')
def states():
    '''Retrieve the list of all `State` objects'''
    result = []
    for value in storage.all(State).values():
        result.append(value.to_dict())
    return jsonify(result)