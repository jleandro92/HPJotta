from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from modelo import DominioException
from modelo.edl import Dado


# Definindo um TypeVar para tipos genéricos
E = TypeVar('E', bound='Dado')
K = TypeVar('K')

class VetorTADS(ABC, Generic[E, K]):
    TAMANHO_MINIMO_DE_ELEMENTOS = 1

    def __init__(self, cls, quantidadeDeElementos: int):
        self.verificaSeAQuantidadeInformadaEhValida(quantidadeDeElementos)
        self.elementos: List[E] = [None] * quantidadeDeElementos
        self.quantidade = 0

    def buscar_por_posicao(self, posicao: int) -> E:
        self.estruturaEstahVazia()
        self.aPosicaoEhValida(posicao)
        self.haElementoNaPosicao(posicao)
        return self.elementos[posicao]

    def buscar_por_chave(self, chave: K) -> E:
        self.estruturaEstahVazia()
        for elemento in self.elementos:
            if elemento is None:
                continue
            if elemento.get_chave() == chave:
                return elemento
        raise DominioException("Elemento não encontrado na estrutura!!!")

    def posicaoNaEstrutura(self, chave: K) -> int:
        self.estruturaEstahVazia()
        for i, elemento in enumerate(self.elementos):
            if elemento is None:
                continue
            if elemento.get_chave() == chave:
                return i
        raise DominioException("Elemento não encontrado na estrutura!!!")

    def inserir(self, elemento: E, posicao: int):
        self.estruturaEstahCheia()
        self.oElementoEhValido(elemento)
        self.naoHaElementoNaPosicao(posicao)
        self.elementos[posicao] = elemento
        self.quantidade += 1

    def remover(self, posicao: int) -> E:
        elementoASerRemovido = self.buscar_por_posicao(posicao)
        self.elementos[posicao] = None
        self.quantidade -= 1
        return elementoASerRemovido

    def array(self) -> List[E]:
        return self.elementos.copy()

    def aPosicaoEhValida(self, posicao: int):
        if posicao < 0 or posicao >= len(self.elementos):
            raise DominioException("Posição informada é inválida!!!")

    def naoHaElementoNaPosicao(self, posicao: int):
        if self.elementos[posicao] is not None:
            raise DominioException("Já existe um elemento na posição informada!!!")

    def haElementoNaPosicao(self, posicao: int):
        if self.elementos[posicao] is None:
            raise DominioException("Não existe elemento na posição informada!!!")

    def oElementoEhValido(self, elemento: E):
        if elemento is None or elemento.get_chave() is None:
            raise DominioException("Elemento inválido!!!")

    def verificaSeAQuantidadeInformadaEhValida(self, quantidadeDeElementos: int):
        if quantidadeDeElementos < self.TAMANHO_MINIMO_DE_ELEMENTOS:
            raise DominioException("Quantidade insuficiente para criar a estrutura!!!")

    def estruturaEstahCheia(self):
        if self.quantidade >= len(self.elementos):
            raise DominioException("A estrutura está cheia!!!")

    def estruturaEstahVazia(self):
        if self.quantidade == 0:
            raise DominioException("A estrutura está vazia!!!")
