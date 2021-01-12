from flask import Flask

def create_app():
  # create and configure the app
  app = Flask(__name__)

  from .api import api as api_blueprint

  # Register necessary blueprints
  app.register_blueprint(api_blueprint)

  return app