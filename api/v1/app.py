#!/usr/bin/python3
"""Main API module"""

from flask import Flask
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

# Create a CORS instance with allow_all_origins set to True
# This will allow requests from all origins (0.0.0.0) for now
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})



@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage session."""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)

@app.teardown_appcontext
def teardown_appcontext(error):
    """Teardown method"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Error handler for 404 - Not found"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
