from enum import Enum

class MensagensErro(Enum):
    HORARIO_INDISPONIVEL = "Horário indisponível"
    HORARIO_INVALIDO = "Formato de horário inválido"
    CONFLITO_DE_HORARIO = "Conflito de horário"