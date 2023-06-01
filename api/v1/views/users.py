from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User


@app_views.route("/users")
def users():
    """Get all users

    Returns:
        list: All the users
    """
    users = storage.all(User)
    result = []

    for user in users.values():
        result.append(user.to_dict())

    return jsonify(result)
