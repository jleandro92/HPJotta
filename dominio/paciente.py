from apresentacao.comando import Comando
from dominio.hospital import Hospital

class Paciente:
    def __init__(self, nome):
        self.nome = nome
        self.exames = []  

    def adicionar_exame(self, tipo, data):
        self.exames.append({"tipo": tipo, "data": data})
        print(f"Exame {tipo} adicionado para o paciente {self.nome} na data {data}.")

    def visualizar_exame_recente(self):
        if not self.exames:
            raise Exception("SEM_EXAMES")
        exame_recente = self.exames[-1]
        print(f"Exame mais recente do paciente {self.nome}: Tipo: {exame_recente['tipo']}, Data: {exame_recente['data']}")

    def remover_exame(self):
        if not self.exames:
            raise Exception("SEM_EXAMES")
        exame_removido = self.exames.pop()
        print(f"Exame {exame_removido['tipo']} removido do paciente {self.nome}.")

class AdicionarExame(Comando):
    def descricao(self):
        return "Adicionar exame para um paciente"

    def execute(self):
        paciente_nome = input("Digite o nome do paciente: ")
        tipo_exame = input("Digite o tipo de exame: ")
        data_exame = input("Digite a data do exame (ex: 2024-12-05): ")

        paciente = Hospital.buscar_paciente(paciente_nome)  # Método para buscar paciente
        if paciente:
            paciente.adicionar_exame(tipo_exame, data_exame)
        else:
            print(f"Erro: Paciente {paciente_nome} não encontrado.")

class VisualizarExameRecente(Comando):
    def descricao(self):
        return "Visualizar exame mais recente de um paciente"

    def execute(self):
        paciente_nome = input("Digite o nome do paciente: ")
        paciente = Hospital.buscar_paciente(paciente_nome) 
        if paciente:
            try:
                paciente.visualizar_exame_recente()
            except Exception as e:
                print(f"Erro: {str(e)}")
        else:
            print(f"Erro: Paciente {paciente_nome} não encontrado.")

class RemoverExame(Comando):
    def descricao(self):
        return "Remover exame de um paciente"

    def execute(self):
        paciente_nome = input("Digite o nome do paciente: ")
        paciente = Hospital.buscar_paciente(paciente_nome)  
        if paciente:
            try:
                paciente.remover_exame()
            except Exception as e:
                print(f"Erro: {str(e)}")
        else:
            print(f"Erro: Paciente {paciente_nome} não encontrado.")
