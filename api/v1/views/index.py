#!/usr/bin/python3

# index.py

from api.v1.views import app_views
from flask import jsonify, Response

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns a JSON with the status 'OK'"""
    response_data = {"status": "OK"}
    return jsonify(response_data), 200, {"Content-Type": "application/json"}

