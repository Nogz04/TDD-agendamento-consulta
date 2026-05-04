from typing import List

from enums.mensagens_erro import MensagensErro
from models.consulta import Consulta
from models.medico import Medico
from models.paciente import Paciente


class AgendamentoService:
    def __init__(self):
        self._consultas_agendadas: List[Consulta] = []

    @property
    def consultas_agendadas(self):
        return self._consultas_agendadas

    def agendar_consulta(
        self, medico: Medico, paciente: Paciente, data: str, hora: str
    ) -> bool:
        if not self.validar_formato_horario(hora):
            raise ValueError(MensagensErro.HORARIO_INVALIDO.value)

        # Verifica se o horário está dentro do turno do médico
        if hora not in medico.gerar_grade_horarios():
            raise ValueError(MensagensErro.HORARIO_INDISPONIVEL.value)

        # Verifica conflito de horário no mesmo dia
        for consulta in self._consultas_agendadas:
            if (
                consulta.medico == medico
                and consulta.data == data
                and consulta.hora == hora
            ):
                raise ValueError(MensagensErro.CONFLITO_DE_HORARIO.value)

        nova_consulta = Consulta(medico, paciente, data, hora)
        self._consultas_agendadas.append(nova_consulta)

        return True

    def cancelar_consulta(self, medico: Medico, data: str, hora: str) -> bool:
        for consulta in self._consultas_agendadas:
            if (
                consulta.medico == medico
                and consulta.data == data
                and consulta.hora == hora
            ):
                self._consultas_agendadas.remove(consulta)
                return True
        return False

    def validar_formato_horario(self, hora: str) -> bool:
        try:
            if ":" not in hora or len(hora) != 5:
                return False

            partes = hora.split(":")
            horas = int(partes[0])
            minutos = int(partes[1])

            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                return False

            return True
        except (ValueError, IndexError, TypeError):
            return False

    def listar_agendamentos(self, medico: Medico) -> list[str]:
        return [
            str(consulta)
            for consulta in self._consultas_agendadas
            if consulta.medico == medico
        ]

    def listar_horarios_disponiveis(self, medico: Medico, data: str) -> list[str]:
        grade = medico.gerar_grade_horarios()
        horarios_ocupados = [
            consulta.hora
            for consulta in self._consultas_agendadas
            if consulta.medico == medico and consulta.data == data
        ]
        return [horario for horario in grade if horario not in horarios_ocupados]

    def listar_consultas_por_paciente(self, paciente: Paciente) -> list[str]:
        return [
            str(consulta)
            for consulta in self._consultas_agendadas
            if consulta.paciente == paciente
        ]

    def listar_consultas_agendadas(self) -> list[str]:
        return [str(consulta) for consulta in self._consultas_agendadas]
