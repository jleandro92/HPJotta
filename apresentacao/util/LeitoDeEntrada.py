import sys

class LeitorDeEntrada:
    def __init__(self):
        pass

    def leia_int(self, solicitacao):
        while True:
            try:
                return int(input(solicitacao))
            except ValueError:
                print("Entrada Inválida. Por favor, entre com um inteiro: ")

    def leia_int_default(self):
        return self.leia_int("Entre com um número inteiro: ")

    def leia_double(self, solicitacao):
        while True:
            try:
                return float(input(solicitacao))
            except ValueError:
                print("Entrada inválida. Por favor, entre com valor do tipo Double (Real): ")

    def leia_double_default(self):
        return self.leia_double("Entre com valor do tipo Double (Real): ")

    def leia_string(self, solicitacao):
        return input(solicitacao)

    def leia_string_default(self):
        return self.leia_string("Entre com valor tipo String (Texto): ")

    def apresente(self, texto):
        print(texto)

