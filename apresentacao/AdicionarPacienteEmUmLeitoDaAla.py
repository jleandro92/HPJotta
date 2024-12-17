from apresentacao.util import LeitorDeEntrada
from apresentacao import Comando 
from HPJotta.diminio.modelo import Ala, DominioException, Hospital, Leito, Paciente

class AdicionarPacienteEmUmLeitoDaAla(Comando):

    def execute(self):
        problema_na_criacao = True
        
        while problema_na_criacao:
            leitor = LeitorDeEntrada()

            try:
                hospital = Hospital.get_instancia()
                
                leitor.apresente("Visualize as Alas Definidas e escolha ala o paciente deverá ser alocado!\n")
                leitor.apresente(str(hospital))

                numeracao_de_ala = leitor.leia_int("Digite a numeração da ala desejada: \n")
                ala_escolhida = hospital.buscar(numeracao_de_ala)
                
                nome_do_paciente = leitor.leia_string("Digite o nome do Paciente: \n")
                cpf = leitor.leia_string("Digite o CPF do Paciente:\n")
                paciente = Paciente(nome_do_paciente, cpf)
                
                leito_ocupado = Leito("", paciente)
                
                leitor.apresente("Visualize as localização dos leitos disponíveis !\n")
                leitor.apresente(str(ala_escolhida))

                numeracao_do_leito = leitor.leia_int("Digite a localização de um leito disponível : \n")
                ala_escolhida.inserir(leito_ocupado, numeracao_do_leito)
                
                leitor.apresente("Visualize as localização dos leitos disponíveis !\n")
                leitor.apresente(str(ala_escolhida))
            
            except DominioException as e:
                leitor.apresente("\n\nErro : " + str(e) + "\n")
                leitor.apresente("Por favor, verifique o erro e tente novamente!!\n\n")

    def descricao(self):
        return "Adicionar Paciente em um Leito da Ala"

