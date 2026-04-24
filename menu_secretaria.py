from models.medico import Medico
from models.paciente import Paciente

def cadastrar_paciente_adm(app):
    nome = input("Nome do paciente: ")
    cpf = input("CPF do paciente: ")

    if any(p.cpf == cpf for p in app.pacientes):
        print("Erro: Já existe um paciente cadastrado com este CPF.")
        return

    data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
    tel = input("Telefone: ")
    try:
        novo_paciente = Paciente(nome, cpf, data_nasc, tel)
        app.pacientes.append(novo_paciente)
        print(f"Paciente {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}")

def realizar_agendamento_adm(app):
    if not app.medicos:
        print("Não há médicos disponíveis.")
        return
    print("\nMédicos disponíveis:")
    for i, m in enumerate(app.medicos):
        print(f"{i+1}. {m.nome}")
    try:
        escolha = int(input("Selecione o médico pelo número: ")) - 1
        if 0 <= escolha < len(app.medicos):
            medico = app.medicos[escolha]
        else:
            print("Seleção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    if not app.pacientes:
        print("Não há pacientes cadastrados. Cadastre um primeiro.")
        return
    print("\nPacientes cadastrados:")
    for i, p in enumerate(app.pacientes):
        print(f"{i+1}. {p.nome} (CPF: {p.cpf})")
    try:
        escolha = int(input("Selecione o paciente pelo número: ")) - 1
        if 0 <= escolha < len(app.pacientes):
            paciente = app.pacientes[escolha]
        else:
            print("Seleção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    data = input("Data da consulta (DD/MM/AAAA): ")
    hora = input("Hora da consulta (HH:MM): ")

    try:
        if app.gerenciador.agendar_consulta(medico, paciente, data, hora):
            print("Agendamento realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao agendar: {e}")

def cancelar_consulta_adm(app):
    if not app.medicos:
        print("Não há médicos cadastrados no sistema.")
        return
    print("\nMédicos disponíveis:")
    for i, m in enumerate(app.medicos):
        print(f"{i+1}. {m.nome}")
    try:
        escolha = int(input("Selecione o médico pelo número: ")) - 1
        if 0 <= escolha < len(app.medicos):
            medico = app.medicos[escolha]
        else:
            print("Seleção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    hora = input("Hora da consulta a cancelar (HH:MM): ")
    if app.gerenciador.cancelar_consulta(medico, hora):
        print("Consulta de horário liberada na agenda do médico com sucesso.")
    else:
        print("Falha ao cancelar: o horário não constava como agendado.")

def executar(app):
    while True:
        print("\n--- MENU ADMINISTRADOR / SECRETARIA ---")
        print("1. Cadastrar Médico")
        print("2. Cadastrar Paciente")
        print("3. Realizar Agendamento")
        print("4. Listar horários disponíveis de todos os médicos")
        print("5. Listar consultas agendadas de um médico")
        print("6. Listar consultas agendadas de um paciente")
        print("7. Cancelar consulta")
        print("8. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do médico: ")
            cpf = input("CPF do médico: ")

            if any(m.cpf == cpf for m in app.medicos):
                print("Erro: Já existe um médico cadastrado com este CPF.")
                continue

            inicio = input("Horário de início (HH:MM): ")
            fim = input("Horário de fim (HH:MM): ")
            try:
                novo_medico = Medico(nome, cpf, inicio, fim)
                app.medicos.append(novo_medico)
                print(f"Médico {nome} cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro ao cadastrar médico: {e}")
        elif opcao == "2":
            cadastrar_paciente_adm(app)
        elif opcao == "3":
            realizar_agendamento_adm(app)
        elif opcao == "4":
            if not app.medicos:
                print("Nenhum médico cadastrado.")
            for medico in app.medicos:
                horarios = app.gerenciador.listar_horarios_disponiveis(medico)
                print(f"{medico}: {', '.join(horarios)}")
        elif opcao == "5":
            busca = input("Nome ou CPF do médico: ")
            medico = next((m for m in app.medicos if m.cpf == busca or busca.lower() in m.nome.lower()), None)
            if medico:
                agendamentos = app.gerenciador.listar_agendamentos(medico)
                print(f"Agendamentos do {medico.nome}:\n" + "\n".join(agendamentos) if agendamentos else "Nenhum agendamento.")
            else:
                print("Médico não encontrado.")
        elif opcao == "6":
            busca = input("Nome ou CPF do paciente: ")
            paciente = next((p for p in app.pacientes if p.cpf == busca or busca.lower() in p.nome.lower()), None)
            if paciente:
                agendamentos = app.gerenciador.listar_consultas_por_paciente(paciente)
                print(f"Agendamentos do {paciente.nome}:\n" + "\n".join(agendamentos) if agendamentos else "Nenhum agendamento.")
            else:
                print("Paciente não encontrado.")
        elif opcao == "7":
            cancelar_consulta_adm(app)
        elif opcao == "8":
            break
        else:
            print("Opção inválida!")
