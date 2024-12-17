from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from modelo import DominioException

E = TypeVar('E') # Tipo de elemento
K = TypeVar('K') # Tipo de chave

class Vetor(ABC, Generic[E, K]):
  
  
  @abstractmethod
  def buscar_por_posicao(self, posicao: int) -> E:
    """Busca um elemento pelo seu índice."""
    pass
  
  @abstractmethod
  def buscar_por_chave(self, chave: K) -> E:
    """Busca um elemento pelo seu valor de chave."""
    pass
  
  @abstractmethod
  def posicao_na_estrutura(self, chave: K) -> int:
    """Retorna a posição do elemento na estrutura."""
    pass
  
  @abstractmethod
  def inserir(self, elemento: E, posicao: int):
    """Insere um elemento na estrutura."""
    pass
  
  @abstractmethod
  def remover(self, posicao: int) -> E:
    """Remove um elemento da estrutura."""
    pass
  
  @abstractmethod
  def vector(self) -> List[E]:
    """Retorna o vetor."""
    pass
  