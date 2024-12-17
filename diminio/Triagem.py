from modelo.edl import ListaSencadeada
from modelo import Paciente

class Triagem(ListaSencadeada):
    
    def __init__(self):
        self.lista = []

    def inserir(self, elemento: 'Paciente'):
        self.lista.append(elemento)

    def tamanho(self) -> int:
        return len(self.lista)

    def primeiro_elemento(self) -> 'Paciente':
        if len(self.lista) == 0:
            raise Exception("Estrutura vazia")
        return self.lista[0]

    def ultimo_elemento(self) -> 'Paciente':
        if len(self.lista) == 0:
            raise Exception("Estrutura vazia")
        return self.lista[-1]