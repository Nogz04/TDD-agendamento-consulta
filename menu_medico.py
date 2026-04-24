from models.paciente import Paciente

def cadastrar_paciente_medico(app):
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

def realizar_agendamento_medico(app, medico):
    if not app.pacientes:
        print("Não há pacientes cadastrados no sistema. Cadastre um primeiro.")
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

def executar(app):
    if not app.medicos:
        print("Nenhum médico cadastrado no sistema.")
        return

    cpf_busca = input("Informe seu CPF (Médico): ")
    medico = next((m for m in app.medicos if m.cpf == cpf_busca), None)

    if not medico:
        print("Médico não encontrado.")
        return

    while True:
        print(f"\n--- BEM-VINDO, DR(A). {medico.nome} ---")
        print("1. Listar meus horários disponíveis")
        print("2. Cadastrar paciente")
        print("3. Realizar agendamento")
        print("4. Listar agendamentos")
        print("5. Cancelar consulta")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            horarios = app.gerenciador.listar_horarios_disponiveis(medico)
            print(f"Horários disponíveis: {', '.join(horarios)}")
        elif opcao == "2":
            cadastrar_paciente_medico(app)
        elif opcao == "3":
            realizar_agendamento_medico(app, medico)
        elif opcao == "4":
            agendamentos = app.gerenciador.listar_agendamentos(medico)
            print(f"Agendamentos: {agendamentos}")
        elif opcao == "5":
            hora = input("Hora da consulta a cancelar (HH:MM): ")
            if app.gerenciador.cancelar_consulta(medico, hora):
                print("Consulta desmarcada na sua agenda com sucesso.")
            else:
                print("Falha ao cancelar: o horário não constava como agendado.")
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")