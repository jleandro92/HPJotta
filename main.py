from apresentacao.comando import Sair, CriarAlaComTamanhoFixo, AdicionarPacienteEmUmLeitoDaAla, RelatorioDeAla, RealocarPaciente
from apresentacao.menu import Menu
from dominio.hospital import Hospital
from dominio.paciente import AdicionarExame, RemoverExame

def main():
    Hospital.configurar_hospital_para_sessao("Hospital João Macchado", 5)

    menu = Menu(7) 
    menu.adicionar_comando(1, CriarAlaComTamanhoFixo())
    menu.adicionar_comando(2, AdicionarPacienteEmUmLeitoDaAla())
    menu.adicionar_comando(3, RealocarPaciente())
    menu.adicionar_comando(4, RelatorioDeAla())
    menu.adicionar_comando(5, AdicionarExame()) 
    menu.adicionar_comando(6, RemoverExame())
    menu.adicionar_comando(0, Sair())

    menu.apresentar_e_executar()

if __name__ == "__main__":
    main()