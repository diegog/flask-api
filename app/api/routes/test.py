from flask import jsonify, request, current_app
from app.api import api

from app.api.controllers.test_controller import (
  testController
)

base_url = '/test'

@api.route(base_url)
def test():
  return testController.test()

# Available at /test/<name>, where <name> is a string
@api.route(base_url + '/<name>')
def hello_name(name):
  return testController.hello_name(name)