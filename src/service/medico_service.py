from typing import List

from enums.mensagens_erro import MensagensErro
from models.paciente import Paciente


class PacienteService:
    def __init__(self):
        self._pacientes: List[Paciente] = []

    def cadastrar_paciente(
        self, nome: str, cpf: str, data_nascimento: str, telefone: str
    ) -> Paciente:
        if any(p.cpf == cpf for p in self._pacientes):
            raise ValueError(MensagensErro.PACIENTE_JA_CADASTRADO.value)

        paciente = Paciente(nome, cpf, data_nascimento, telefone)
        self._pacientes.append(paciente)
        return paciente

    def listar_pacientes(self) -> List[Paciente]:
        return self._pacientes
