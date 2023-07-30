# __init__.py

from flask import Blueprint

# Create a Blueprint instance (url prefix must be /api/v1)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import of everything in the package api.v1.views.index
# PEP8 will complain about it, but it's normal and won't be checked in this file.
# This is done to add the routes from index.py to the app_views Blueprint.
from api.v1.views.index import *
