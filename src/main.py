from menus import menu_medico, menu_paciente, menu_secretaria
from service.agendamentos import AgendamentoService
from service.medico_service import MedicoService
from service.paciente_service import PacienteService


class Main:
    def __init__(self):
        self.agendamento_service = AgendamentoService()
        self.medico_service = MedicoService()
        self.paciente_service = PacienteService()

    @property
    def gerenciador(self):
        return self.agendamento_service

    @property
    def medicos(self):
        return self.medico_service.listar_medicos()

    @property
    def pacientes(self):
        return self.paciente_service.listar_pacientes()

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
    import sys
    import unittest

    print("Rodando testes de integridade...")

    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ Todos os testes passaram! Sistema pronto para uso...\n")
        main = Main()
        main.menu_principal()
    else:
        print(
            "\n❌ Bloqueio ativado: Falhas críticas encontradas! Por favor resolva os testes antes de subir em Produção."
        )
        sys.exit(1)
