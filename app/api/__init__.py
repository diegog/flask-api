"""Routes Initialization"""

from flask import Blueprint
api = Blueprint('api', __name__)

# Import routes
import app.api.routes