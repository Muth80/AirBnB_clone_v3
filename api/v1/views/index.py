#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Get the number of each object by type."""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(stats)

