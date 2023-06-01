from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

from flask import jsonify


@app_views.route("/amenities")
def amenities():
    """Retrieve list of all `Amenity` objects

    Returns:
        `~flask.Response`: List of all the amenities
    """
    amenities = storage.all(Amenity)
    result = []

    for amenity in amenities.values():
        result.append(amenity.to_dict())

    return jsonify(result)
