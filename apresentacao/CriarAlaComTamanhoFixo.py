from apresentacao.util import LeitorDeEntrada
from HPJotta.diminio.modelo import Ala, DominioException, Hospital
from apresentacao import Comando

class CriarAlaComTamanhoFixo(Comando):

    def execute(self):
        problema_na_criacao = True
        
        while problema_na_criacao:
            leitor = LeitorDeEntrada()
            
            try:
                hospital = Hospital.get_instancia()
                
                leitor.apresente("Veja a estrutura do Hospital até o momento: \n")
                leitor.apresente(str(hospital))

                ambiente_escolhido = leitor.leia_int("\n\nInforme o ambiente no qual queres instanciar uma Ala: ")
                quantidade_de_leitos = leitor.leia_int("Informe a quantidade de Leitos da Ala: ")
                nome_da_ala = leitor.leia_string("Informe o nome da Ala que deseja criar: ")
                ala = Ala(nome_da_ala, quantidade_de_leitos)
                
                hospital.inserir(ala, ambiente_escolhido)
                
                leitor.apresente(str(hospital))
                
                problema_na_criacao = False
            except DominioException as e:
                leitor.apresente("\n\nErro: " + str(e) + "\n")
                leitor.apresente("Por favor, verifique o erro e tente novamente!!\n\n")

    def descricao(self):
        return "Criar Ala Com Tamanho Fixo"

