from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

from enums.mensagens_erro import MensagensErro


@dataclass
class Medico:
    nome: str
    cpf: str
    horario_inicio: str
    horario_fim: str

    def __post_init__(self):
        if not self.nome or not self.cpf:
            raise ValueError(MensagensErro.MEDICO_DADOS_INVALIDOS.value)

    def gerar_grade_horarios(self) -> List[str]:
        horarios = []
        try:
            inicio = datetime.strptime(self.horario_inicio, "%H:%M")
            fim = datetime.strptime(self.horario_fim, "%H:%M")

            atual = inicio
            while atual <= fim:
                horarios.append(atual.strftime("%H:%M"))
                atual += timedelta(minutes=30)

        except ValueError as exc:
            raise ValueError(MensagensErro.HORARIO_INVALIDO.value) from exc

        return horarios

    def __str__(self):
        return f"Dr(a). {self.nome} (CPF: {self.cpf})"
