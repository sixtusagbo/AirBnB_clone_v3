from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities")
def cities_in_a_state(state_id):
    """Retrieve the list of all `City` objects of a state

    Args:
        state_id (str): State identifier
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    result = []
    for city in state.cities:
        result.append(city.to_dict())
    return jsonify(result)
