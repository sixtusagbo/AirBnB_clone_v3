from flask import jsonify, abort

from api.v1.views import app_views
from models.place import Place
from models import storage
from models import storage_t as storage_type


@app_views.route("/places/<place_id>/amenities")
def amenities_of_a_place(place_id):
    """Retrieve all amenities of a place.

    Args:
        place_id (str): ID of the place to retrieve its amenities.

    Returns:
        list: All amenities of the place in JSON.

    Raises:
        404: If the specified place_id does not exist.
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    result = []

    if storage_type == "db":
        for amenity in place.amenities:
            result.append(amenity.to_dict())
    else:
        result = place.amenities

    return jsonify(result)
