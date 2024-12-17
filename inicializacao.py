class Comando:
    def executar(self):
        raise NotImplementedError("O método 'executar' precisa ser implementado.")


class Sair(Comando):
    def executar(self):
        print("Saindo do programa...")
        exit()


class CriarAlaComTamanhoFixo(Comando):
    alas = []  # Lista para armazenar as alas criadas

    def executar(self):
        descricao = input("Informe a descrição da ala: ")
        quantidade_de_leitos = int(input("Informe a quantidade de leitos: "))
        # Criando uma lista de leitos, inicialmente todos vazios
        leitos = ["VAZIO"] * quantidade_de_leitos
        ala = {"descricao": descricao, "quantidade_de_leitos": quantidade_de_leitos, "leitos": leitos}
        self.alas.append(ala)
        print(f"Ala '{descricao}' com {quantidade_de_leitos} leitos criada com sucesso.")


class AdicionarPacienteEmUmLeitoDaAla(Comando):
    pacientes = []  # Lista para armazenar pacientes cadastrados
    alas = CriarAlaComTamanhoFixo.alas  # Acesso à lista de alas criadas

    def executar(self):
        nome = input("Informe o nome do paciente: ")
        cpf = input("Informe o CPF do paciente: ")
        ala_descricao = input("Informe a descrição da ala: ")
        
        # Buscar a ala pela descrição
        ala_encontrada = None
        for ala in self.alas:
            if ala['descricao'] == ala_descricao:
                ala_encontrada = ala
                break
        
        if ala_encontrada:
            leito_numero = int(input(f"Informe o número do leito (1 a {ala_encontrada['quantidade_de_leitos']}): "))
            if 1 <= leito_numero <= ala_encontrada['quantidade_de_leitos'] and ala_encontrada['leitos'][leito_numero - 1] == "VAZIO":
                ala_encontrada['leitos'][leito_numero - 1] = nome
                paciente = {"nome": nome, "cpf": cpf, "ala": ala_descricao, "leito": leito_numero}
                self.pacientes.append(paciente)
                print(f"Paciente {nome} adicionado ao leito {leito_numero} da ala '{ala_descricao}'.")
            else:
                print("Leito inválido ou já ocupado.")
        else:
            print(f"Ala '{ala_descricao}' não encontrada.")


class ListarPacientes(Comando):
    alas = CriarAlaComTamanhoFixo.alas  # Acesso às alas criadas

    def executar(self):
        if not self.alas:
            print("Nenhuma ala cadastrada.")
        else:
            for ala in self.alas:
                print(f"\nALA: {ala['descricao']} | QUANTIDADE: {ala['quantidade_de_leitos']}")
                for i, leito in enumerate(ala['leitos'], start=1):
                    print(f"{i} - {leito}")


class Menu:
    def __init__(self, numero_de_comandos):
        self.comandos = [None] * numero_de_comandos

    def adicionar_comando(self, indice, comando):
        if 0 <= indice < len(self.comandos):
            self.comandos[indice] = comando

    def apresentar_e_executar(self):
        while True:
            print("\nMenu:")
            for i, comando in enumerate(self.comandos):
                print(f"{i} - {comando.__class__.__name__ if comando else 'Vazio'}")

            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao < len(self.comandos) and self.comandos[opcao]:
                    self.comandos[opcao].executar()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, insira um número válido.")


# Exemplo de uso do Menu
menu = Menu(4)
menu.adicionar_comando(0, Sair())
menu.adicionar_comando(1, CriarAlaComTamanhoFixo())
menu.adicionar_comando(2, AdicionarPacienteEmUmLeitoDaAla())
menu.adicionar_comando(3, ListarPacientes())

menu.apresentar_e_executar()
