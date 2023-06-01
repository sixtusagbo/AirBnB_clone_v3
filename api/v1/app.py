#!/usr/bin/python3
""" the api module """
from os import getenv

from flask import Flask, jsonify

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

host = getenv("HBNB_API_HOST", "0.0.0.0")
port = getenv("HBNB_API_PORT", "5000")


@app.teardown_appcontext
def teardown(exception):
    """Cleanup operations"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    app.run(host, port, threaded=True, debug=True)
