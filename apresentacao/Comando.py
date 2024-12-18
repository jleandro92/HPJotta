from dominio.hospital import Hospital

class Comando:
    def descricao(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class Sair(Comando):
    def descricao(self):
        return "Sair do programa"

    def execute(self):
        print("Saindo do programa...")
        exit(0)


class CriarAlaComTamanhoFixo(Comando):
    def descricao(self):
        return "Criar ala com tamanho fixo"

    def execute(self):
        nome = input("Digite o nome da ala: ")
        capacidade = int(input("Digite a capacidade da ala: "))
        try:
            Hospital.criar_ala(nome, capacidade)
            print(f"Ala '{nome}' criada com capacidade de {capacidade} leitos.")
        except ValueError as e:
            print(f"Erro ao criar ala: {e}")


class AdicionarPacienteEmUmLeitoDaAla(Comando):
    def descricao(self):
        return "Adicionar paciente em um leito da ala"

    def execute(self):
        nome_paciente = input("Digite o nome do paciente: ")
        nome_ala = input("Digite o nome da ala: ")
        indice_leito = int(input("Digite o índice do leito: "))
        try:
            Hospital.alocar_paciente(nome_ala, nome_paciente, indice_leito)
            print(f"Paciente '{nome_paciente}' alocado no leito {indice_leito} da ala '{nome_ala}'.")
        except ValueError as e:
            print(f"Erro ao alocar paciente: {e}")

class RelatorioDeAla(Comando):
    def descricao(self):
        return "Exibir relatório de alas"

    def execute(self):
        if not Hospital.alas:
            print("Não há alas cadastradas no hospital.")
            return
        
        for nome_ala, leitos in Hospital.alas.items():
            print(f"\nALA: {nome_ala} | QUANTIDADE: {len(leitos)}")
            for i, paciente in enumerate(leitos, start=1):
                status = paciente if paciente is not None else "VAZIO"
                print(f"{i} - {status}")
                
                
class RealocarPaciente(Comando):
    def descricao(self):
        return "Realocar paciente entre alas ou leitos"

    def execute(self):
        if not Hospital.alas:
            print("Erro: Não há alas cadastradas no hospital.")
            return
        
        nome_paciente = input("Digite o nome do paciente a ser realocado: ")
        
        # Procurando o paciente nas alas
        paciente_encontrado = None
        origem_ala = None
        origem_leito = None
        
        for nome_ala, leitos in Hospital.alas.items():
            for i, paciente in enumerate(leitos):
                if paciente == nome_paciente:
                    paciente_encontrado = paciente
                    origem_ala = nome_ala
                    origem_leito = i
                    break
            if paciente_encontrado:
                break

        if not paciente_encontrado:
            print(f"Erro: Paciente {nome_paciente} não encontrado no hospital.")
            return
        
        print(f"Paciente {nome_paciente} encontrado na ala {origem_ala}, leito {origem_leito + 1}.")
        
        
        nova_ala = input("Digite o nome da nova ala (ou a mesma ala para realocar de leito): ")
        
        if nova_ala not in Hospital.alas:
            print(f"Erro: A ala {nova_ala} não existe.")
            return
        
        nova_ala_leitos = Hospital.alas[nova_ala]
        
        
        if nova_ala == origem_ala:
            novo_leito = int(input(f"Digite o número do novo leito (1 a {len(nova_ala_leitos)}): ")) - 1
            if novo_leito < 0 or novo_leito >= len(nova_ala_leitos):
                print("Erro: Leito inválido.")
                return
            if nova_ala_leitos[novo_leito] is not None:
                print(f"Erro: O leito {novo_leito + 1} já está ocupado.")
                return
            # Realocar para o novo leito
            nova_ala_leitos[novo_leito] = nome_paciente
            nova_ala_leitos[origem_leito] = None
            print(f"Paciente {nome_paciente} realocado para o leito {novo_leito + 1} da ala {nova_ala}.")
        else:
            
            for i, leito in enumerate(nova_ala_leitos):
                if leito is None:
                    nova_ala_leitos[i] = nome_paciente
                    Hospital.alas[origem_ala][origem_leito] = None
                    print(f"Paciente {nome_paciente} realocado da ala {origem_ala}, leito {origem_leito + 1} para a ala {nova_ala}, leito {i + 1}.")
                    return
            print(f"Erro: Não há vaga na ala {nova_ala} para o paciente {nome_paciente}.")

