# app.py

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

# Create a Flask instance
app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views, url_prefix='/api/v1')


# Method to handle teardown_appcontext, calls storage.close()
@app.teardown_appcontext
def teardown_app_context(exception):
    """Closes the storage"""
    storage.close()


if __name__ == "__main__":
    # Define host and port using environment variables or default values
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    # Run the Flask server
    app.run(host=host, port=port, threaded=True)

