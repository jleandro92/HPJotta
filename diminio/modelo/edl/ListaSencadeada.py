from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from modelo import DominioException


T = TypeVar('T')

class ListaSencadeada(ABC, Generic[T]):

    @abstractmethod
    def inserir(self, elemento: T):

      pass

    @abstractmethod
    def tamanho(self) -> int:

      pass

    @abstractmethod
    def primeiroElemento(self) -> T:
 
      pass

    @abstractmethod
    def ultimoElemento(self) -> T:
     
      pass
