from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def descricao(self) -> str:
        pass

