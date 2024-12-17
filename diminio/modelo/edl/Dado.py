from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Dado(ABC, Generic[T]):
 
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def get_chave(self) -> T:
        pass
