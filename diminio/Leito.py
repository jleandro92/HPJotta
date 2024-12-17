from modelo.edl import Dado
from modelo import Paciente

class Leito(Dado):
    def __init__(self, descricao: str, paciente: Paciente):
        self.descricao = descricao
        self.paciente = paciente

    def get_paciente(self) -> Paciente:
        return self.paciente

    def get_chave(self) -> str:
        if self.paciente:
            return self.paciente.get_cpf()
        raise ValueError("Paciente não encontrado!")

    def get_descricao(self) -> str:
        return self.descricao
