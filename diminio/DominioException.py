class DominioException(Exception):
  """Clase para excepciones de dominio"""
  def __init__(self, msg, cause = None):
    super().__init__(msg)
    self.cause = cause

def __str__(self):
  if self.cause:
    return f"{super().__str__()} (Causa: {repr(self.cause)})"
  return super().__str__()