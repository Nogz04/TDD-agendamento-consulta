from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List

from enums.mensagens_erro import MensagensErro


@dataclass
class Medico:
    nome: str
    cpf: str
    horario_inicio: str
    horario_fim: str
    horarios_disponiveis: List[str] = field(init=False)

    _registros: set[str] = (
        set()
    )  # Cria um conjunto para armazenar os dados dos medicos instanciados, tipo um mini banco de dados

    def __post_init__(self):
        if not self.nome or not self.cpf:
            raise ValueError(MensagensErro.MEDICO_DADOS_INVALIDOS.value)

        if self.cpf in Medico._registros:
            raise ValueError(MensagensErro.MEDICO_JA_CADASTRADO.value)

        Medico._registros.add(self.cpf)
        self.horarios_disponiveis = self.gerar_grade_horarios()

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

    @classmethod  # Permite que o método seja chamado sem criar uma instância da classe
    def limpar_registros(cls):
        cls._registros.clear()

    def __str__(self):
        return f"Dr(a). {self.nome} (CPF: {self.cpf})"
