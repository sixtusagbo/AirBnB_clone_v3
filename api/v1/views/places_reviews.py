from api.v1.views import app_views
from models import storage
from models.review import Review
from models.place import Place
from flask import jsonify, request, abort


@app_views.route("/places/<place_id>/reviews")
def reviews_of_a_place(place_id):
    """Get all reviews of a place.

    Args:
        place_id (str): ID of the place to get the reviews from.

    Returns:
        list: Reviews of that place.

    Raises:
        404: If the specified place_id does not exist.
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    result = []

    for review in place.reviews:
        result.append(review.to_dict())

    return jsonify(result)
