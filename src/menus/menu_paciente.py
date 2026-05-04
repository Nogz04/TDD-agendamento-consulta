def realizar_agendamento_paciente(app, paciente):
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

    data = input("Data da consulta (DD/MM/AAAA): ")
    hora = input("Hora da consulta (HH:MM): ")

    try:
        if app.gerenciador.agendar_consulta(medico, paciente, data, hora):
            print("Agendamento realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao agendar: {e}")


def cancelar_consulta_paciente(app, paciente):
    agendamentos = app.gerenciador.listar_consultas_por_paciente(paciente)
    if not agendamentos:
        print("Você não tem nenhuma consulta agendada para cancelar.")
        return

    print("\nSuas consultas agendadas:")
    for i, ag in enumerate(agendamentos):
        print(f"{i+1}. {ag}")

    try:
        escolha = int(input("Cancelar consulta de qual número? ")) - 1
        if 0 <= escolha < len(agendamentos):
            consulta_escolhida = agendamentos[escolha]
        else:
            print("Seleção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    # Extrai data e hora de: "Consulta: Dr House - Matheus em 23/04/2026 às 10:00"
    parte_em_diante = consulta_escolhida.split(" em ")[-1]
    data = parte_em_diante.split(" às ")[0]
    hora = parte_em_diante.split(" às ")[1]

    # Extrai o nome do médico
    nome_e_resto = consulta_escolhida.replace("Consulta: ", "")
    nome_medico_str = nome_e_resto.split(" - ")[0]

    medico_alvo = next((m for m in app.medicos if m.nome == nome_medico_str), None)
    if not medico_alvo:
        print("Erro: Médico associado não encontrado no sistema.")
        return

    if app.gerenciador.cancelar_consulta(medico_alvo, data, hora):
        print("Consulta desmarcada com sucesso.")
    else:
        print(
            "Falha ao cancelar: o horário não constava como agendado com este médico."
        )


def executar(app):
    cpf = input("Informe seu CPF: ")
    paciente = next((p for p in app.pacientes if p.cpf == cpf), None)

    if not paciente:
        print("Paciente não cadastrado. Vamos realizar seu cadastro.")
        nome = input("Informe seu nome: ")
        data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
        tel = input("Telefone: ")
        try:
            paciente = app.paciente_service.cadastrar_paciente(
                nome, cpf, data_nasc, tel
            )
            print("Cadastro realizado com sucesso!")
        except Exception as e:
            print(f"Erro no cadastro: {e}")
            return

    while True:
        print(f"\n--- BEM-VINDO, {paciente.nome} ---")
        print("1. Realizar agendamento")
        print("2. Listar minhas consultas")
        print("3. Cancelar consulta")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            realizar_agendamento_paciente(app, paciente)
        elif opcao == "2":
            agendamentos = app.gerenciador.listar_consultas_por_paciente(paciente)
            print("Suas consultas:")
            for ag in agendamentos:
                print(ag)
            if not agendamentos:
                print("Nenhuma consulta encontrada.")
        elif opcao == "3":
            cancelar_consulta_paciente(app, paciente)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
