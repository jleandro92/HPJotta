from apresentacao.util import LeitorDeEntrada

class Menu:
    
    def __init__(self, quantidade_de_comandos):
        self.leitor_de_entrada = LeitorDeEntrada()
        self.comandos = [None] * quantidade_de_comandos

    def adicionar_comando(self, posicao, comando):
        self.comandos[posicao] = comando

    def obter_comando(self, posicao):
        return self.comandos[posicao]

    def apresentar_e_executar(self):
        self.leitor_de_entrada.apresente("Escolha a opção : \n\n")
        
        for i in range(len(self.comandos)):
            self.leitor_de_entrada.apresente(f"{i} - {self.comandos[i].descricao()}\n")
        
        escolha = self.leitor_de_entrada.leia_int("\nDigite a opção desejada : ")
        
        if 0 <= escolha < len(self.comandos):
            self.comandos[escolha].execute()
        
        self.apresentar_e_executar()

