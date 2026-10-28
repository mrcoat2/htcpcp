class TeapotException(Exception):
  pass

def brew():
    raise TeapotException("418 I'm a teapot")
