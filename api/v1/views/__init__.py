#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import (PEP8 will complain, but it's expected and okay)
from api.v1.views.index import *

# Import your other view files here
from api.v1.views.index import *
from api.v1.views.states import  # Add this line to import the states view
from api.v1.views.cities import  # Add this line to import the cities view
from api.v1.views.amenities import  # Add this line to import the amenities view
