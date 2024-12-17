class Paciente:
    def __init__(self, nome: str, cpf: str, numeracao_de_leito: int = None):
        self.nome = nome
        self.cpf = cpf
        self.numeracao_de_leito = numeracao_de_leito if numeracao_de_leito is not None else -1  # Valor padrão para indicar não atribuído

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_numeracao_de_leito(self) -> int:
        return self.numeracao_de_leito

    def set_numeracao_de_leito(self, numeracao_de_leito: int):
        self.numeracao_de_leito = numeracao_de_leito
