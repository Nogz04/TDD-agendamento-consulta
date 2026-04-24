from enum import Enum

class MensagensErro(Enum):
    # Mensagens de erro para o agendamento de consultas
    HORARIO_INDISPONIVEL = "Horário indisponível"
    HORARIO_INVALIDO = "Formato de horário inválido"
    CONFLITO_DE_HORARIO = "Conflito de horário"

    # Mensagens de erro para o cadastro de pacientes
    PACIENTE_DADOS_INVALIDOS = "Dados do paciente inválidos"
    
    # Mensagens de erro para o cadastro de médicos
    MEDICO_DADOS_INVALIDOS = "Dados do médico inválidos"
    MEDICO_JA_CADASTRADO = "Médico já cadastrado"