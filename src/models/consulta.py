from dataclasses import dataclass

from models.medico import Medico
from models.paciente import Paciente


@dataclass
class Consulta:
    medico: Medico
    paciente: Paciente
    data: str
    hora: str

    def __str__(self):
        return f"Consulta: {self.medico.nome} - {self.paciente.nome} (CPF: {self.paciente.cpf}) em {self.data} às {self.hora}"
