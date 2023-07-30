# index.py

from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns a JSON with the status 'OK'"""
    return jsonify({"status": "OK"})

