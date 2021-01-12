from app.api.services.test_service import TestService

class testController:
  def test():
    return 'OK'

  def hello_name(name):
    try:
      return TestService.hello_name(name)
    except:
      return 'Error'