from service.agendamentos import RealizarAgendamento
import menu_secretaria
import menu_medico
import menu_paciente

class Main():
    def __init__(self):
        self.gerenciador = RealizarAgendamento()
        self.medicos = []
        self.pacientes = []

    def menu_principal(self):
        while True:
            print("\n=== SISTEMA DE AGENDAMENTO MÉDICO ===")
            print("1. Menu Secretaria (ADM)")
            print("2. Menu Médico")
            print("3. Menu Paciente")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                menu_secretaria.executar(self)
            elif opcao == "2":
                menu_medico.executar(self)
            elif opcao == "3":
                menu_paciente.executar(self)
            elif opcao == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    import unittest
    import sys

    print("Rodando testes de integridade...")
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ Todos os testes passaram! Sistema pronto para uso...\n")
        main = Main()
        main.menu_principal()
    else:
        print("\n❌ Bloqueio ativado: Falhas críticas encontradas! Por favor resolva os testes antes de subir em Produção.")
        sys.exit(1)
