from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

from flask import jsonify, abort


@app_views.route("/amenities")
def amenities():
    """Retrieve list of all `Amenity` objects

    Returns:
        `flask.Response`: List of all the amenities
    """
    amenities = storage.all(Amenity)
    result = []

    for amenity in amenities.values():
        result.append(amenity.to_dict())

    return jsonify(result)


@app_views.route("/amenities/<amenity_id>")
def amenity(amenity_id):
    """Retrieve one `Amenity`

    Args:
        amenity_id (str): Amenity identifier

    Returns:
        flask.Response: An amenity in json
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    """Delete an amenity.

    Args:
        amenity_id (str): The ID of the amenity.

    Returns:
        dict: An empty JSON.

    Raises:
        404: If the specified amenity_id does not exist.
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    amenity.delete()
    storage.save()

    return jsonify({})
