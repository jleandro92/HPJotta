import sys
from apresentacao import Comando

class Sair(Comando):
  def execute(self):
    sys.exit(0)
    
  def descricao(self):
    return "Sair do programa"