from modelo.edl import VetorTADS, Leito
from modelo.edl import Dado

class AlaCheiaException(Exception):
    def __init__(self, message):
        super().__init__(message)

class LeitoOcupadoException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Ala(VetorTADS, Dado[str]):
    def __init__(self, descricao: str, quantidade_de_elementos: int):
        super().__init__(Leito, quantidade_de_elementos)
        self.descricao = descricao

    def get_chave(self) -> str:
        return self.descricao

    def get_descricao(self) -> str:
        return self.descricao

    def __str__(self):
        leitos = self.array()
        sb = ["Disponibilidade de Leitos na Ala: \n"]
        
        for i, leito in enumerate(leitos):
            texto = leito.get_descricao() if leito is not None else "Sem Ocupação"
            sb.append(f"[ {i} ] - {texto}\n")
        
        sb.append("\n")
        return ''.join(sb)