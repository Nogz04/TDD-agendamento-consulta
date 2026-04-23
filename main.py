from service.agendamentos import RealizarAgendamento
from models.medico import Medico
from models.paciente import Paciente

class Main():
    def __init__(self):
        self.gerenciador = RealizarAgendamento()
        self.medicos = []
        self.pacientes = []

    def menu_principal(self):
        while True:
            print("\n=== SISTEMA DE AGENDAMENTO MÉDICO ===")
            print("1. Menu ADM")
            print("2. Menu Médico")
            print("3. Menu Paciente")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_adm()
            elif opcao == "2":
                self.menu_medico()
            elif opcao == "3":
                self.menu_paciente()
            elif opcao == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def menu_adm(self):
        while True:
            print("\n--- MENU ADMINISTRADOR ---")
            print("1. Cadastrar Médico")
            print("2. Listar horários disponíveis de todos os médicos")
            print("3. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome do médico: ")
                cpf = input("CPF do médico: ")

                if any(m.cpf == cpf for m in self.medicos):
                    print("Erro: Já existe um médico cadastrado com este CPF.")
                    continue

                inicio = input("Horário de início (HH:MM): ")
                fim = input("Horário de fim (HH:MM): ")
                try:
                    novo_medico = Medico(nome, cpf, inicio, fim)
                    self.medicos.append(novo_medico)
                    print(f"Médico {nome} cadastrado com sucesso!")
                except Exception as e:
                    print(f"Erro ao cadastrar médico: {e}")
            elif opcao == "2":
                if not self.medicos:
                    print("Nenhum médico cadastrado.")
                for medico in self.medicos:
                    horarios = self.gerenciador.listar_horarios_disponiveis(medico)
                    print(f"{medico}: {', '.join(horarios)}")
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")

    def menu_medico(self):
        if not self.medicos:
            print("Nenhum médico cadastrado no sistema.")
            return

        cpf_busca = input("Informe seu CPF (Médico): ")
        medico = next((m for m in self.medicos if m.cpf == cpf_busca), None)

        if not medico:
            print("Médico não encontrado.")
            return

        while True:
            print(f"\n--- BEM-VINDO, DR(A). {medico.nome} ---")
            print("1. Listar meus horários disponíveis")
            print("2. Cadastrar paciente")
            print("3. Realizar agendamento")
            print("4. Listar agendamentos")
            print("5. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                horarios = self.gerenciador.listar_horarios_disponiveis(medico)
                print(f"Horários disponíveis: {', '.join(horarios)}")
            elif opcao == "2":
                self.cadastrar_paciente()
            elif opcao == "3":
                self.realizar_agendamento(medico_logado=medico)
            elif opcao == "4":
                agendamentos = self.gerenciador.listar_agendamentos(medico)
                print(f"Agendamentos: {agendamentos}")
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

    def menu_paciente(self):
        cpf = input("Informe seu CPF: ")
        paciente = next((p for p in self.pacientes if p.cpf == cpf), None)

        if not paciente:
            print("Paciente não cadastrado. Vamos realizar seu cadastro.")
            nome = input("Informe seu nome: ")
            data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
            tel = input("Telefone: ")
            paciente = Paciente(nome, cpf, data_nasc, tel)
            self.pacientes.append(paciente)
            print("Cadastro realizado com sucesso!")

        while True:
            print(f"\n--- BEM-VINDO, {paciente.nome} ---")
            print("1. Realizar agendamento")
            print("2. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.realizar_agendamento(paciente_logado=paciente)
            elif opcao == "2":
                break
            else:
                print("Opção inválida!")

    def cadastrar_paciente(self):
        nome = input("Nome do paciente: ")
        cpf = input("CPF do paciente: ")

        if any(p.cpf == cpf for p in self.pacientes):
            print("Erro: Já existe um paciente cadastrado com este CPF.")
            return

        data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
        tel = input("Telefone: ")
        novo_paciente = Paciente(nome, cpf, data_nasc, tel)
        self.pacientes.append(novo_paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")

    def realizar_agendamento(self, medico_logado=None, paciente_logado=None):
        # Selecionar Médico se não estiver logado
        medico = medico_logado
        if not medico:
            if not self.medicos:
                print("Não há médicos disponíveis.")
                return
            print("\nMédicos disponíveis:")
            for i, m in enumerate(self.medicos):
                print(f"{i+1}. {m.nome}")
            try:
                escolha = int(input("Selecione o médico pelo número: ")) - 1
                if 0 <= escolha < len(self.medicos):
                    medico = self.medicos[escolha]
                else:
                    print("Seleção inválida.")
                    return
            except ValueError:
                print("Entrada inválida.")
                return

        # Selecionar Paciente se não estiver logado
        paciente = paciente_logado
        if not paciente:
            if not self.pacientes:
                print("Não há pacientes cadastrados. Cadastre um primeiro.")
                return
            print("\nPacientes cadastrados:")
            for i, p in enumerate(self.pacientes):
                print(f"{i+1}. {p.nome} (CPF: {p.cpf})")
            try:
                escolha = int(input("Selecione o paciente pelo número: ")) - 1
                if 0 <= escolha < len(self.pacientes):
                    paciente = self.pacientes[escolha]
                else:
                    print("Seleção inválida.")
                    return
            except ValueError:
                print("Entrada inválida.")
                return

        # Agendamento
        data = input("Data da consulta (DD/MM/AAAA): ")
        hora = input("Hora da consulta (HH:MM): ")

        try:
            if self.gerenciador.agendar_consulta(medico, paciente, data, hora):
                print("Agendamento realizado com sucesso!")
        except Exception as e:
            print(f"Erro ao agendar: {e}")

if __name__ == "__main__":
    main = Main()
    main.menu_principal()