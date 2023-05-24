#!/usr/bin/python3
'''Handles all RESTful API actions for `State` objects'''
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State

@app_views.route('/states')
def states():
    '''Retrieve the list of all `State` objects'''
    result = []
    for value in storage.all(State).values():
        result.append(value.to_dict())
    return jsonify(result)

@app_views.route('/states/<state_id>')
def state(state_id):
    result = storage.get(State, state_id)
    if (result is None):
        abort(404)
    return jsonify(result.to_dict())