from typing import List

from enums.mensagens_erro import MensagensErro
from models.medico import Medico


class MedicoService:
    def __init__(self):
        self._medicos: List[Medico] = []
        self._cpfs_cadastrados = set()

    def cadastrar_medico(
        self, nome: str, cpf: str, horario_inicio: str, horario_fim: str
    ) -> Medico:
        if cpf in self._cpfs_cadastrados:
            raise ValueError(MensagensErro.MEDICO_JA_CADASTRADO.value)

        medico = Medico(nome, cpf, horario_inicio, horario_fim)
        self._medicos.append(medico)
        self._cpfs_cadastrados.add(cpf)
        return medico

    def listar_medicos(self) -> List[Medico]:
        return self._medicos
