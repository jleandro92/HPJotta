class LeitorDeEntrada:
    @staticmethod
    def apresente(mensagem):
        print(mensagem, end="")

    @staticmethod
    def leia_int(mensagem):
        while True:
            try:
                return int(input(mensagem))
            except ValueError:
                print("Por favor, insira um número válido.")
