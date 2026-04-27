from unittest import TestCase

from enums.mensagens_erro import MensagensErro
from models.medico import Medico
from models.paciente import Paciente
from service.agendamentos import RealizarAgendamento


class TestGerenciadorAgenda(TestCase):

    def setUp(self):
        Medico.limpar_registros()  # Limpa o registro de médicos antes de cada teste, para que os testes não interfiram uns nos outros

    def test_agenda_consulta_com_sucesso(self):
        gerenciador = RealizarAgendamento()

        # Criando médico e paciente
        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        # Agendando consulta
        resultado = gerenciador.agendar_consulta(
            medico, paciente, "2026-04-23", "10:00"
        )

        # Verificando se o horário foi agendado
        # print(f"\nHorários disponíveis do {medico.nome}: {medico.horarios_disponiveis}")

        self.assertTrue(resultado)

    def test_cancelar_consulta(self):
        gerenciador = RealizarAgendamento()

        # Criando médico e paciente
        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "55984039186")

        # Agendando e verificando se a consulta foi agendada com sucesso
        resultado = gerenciador.agendar_consulta(
            medico, paciente, "2026-04-23", "10:00"
        )
        self.assertTrue(resultado)

        # Cancelando e verificando se a consulta foi cancelada com sucesso
        resultado = gerenciador.cancelar_consulta(medico, "10:00")
        self.assertTrue(resultado)

    def test_horario_invalido(self):
        gerenciador = RealizarAgendamento()

        # Testando casos de horário inválido que devem retornar FALSO
        self.assertFalse(gerenciador.validar_formato_horario("25:00"))  # Hora inválida
        self.assertFalse(
            gerenciador.validar_formato_horario("10:65")
        )  # Minuto inválido
        self.assertFalse(gerenciador.validar_formato_horario("9:00"))  # Formato curto
        self.assertFalse(gerenciador.validar_formato_horario("1000"))  # Sem dois pontos
        self.assertFalse(gerenciador.validar_formato_horario("-10:00"))  # Negativo

        # Testando caso verdadeiro que deve retornar TRUE
        self.assertTrue(gerenciador.validar_formato_horario("08:30"))

    def test_agendamento_fora_do_horario(self):
        gerenciador = RealizarAgendamento()
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        with self.assertRaises(ValueError) as context:
            gerenciador.agendar_consulta(medico, paciente, "2026-04-23", "11:00")
        self.assertEqual(
            str(context.exception), MensagensErro.HORARIO_INDISPONIVEL.value
        )

    def test_prevencao_sobreposicao_conflito_agendamento(self):
        # Prevenção de Sobreposição (agendar no mesmo horário já agendado)
        gerenciador = RealizarAgendamento()
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        paciente1 = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")
        paciente2 = Paciente("Douglas", "55566677788", "02/02/1990", "11888888888")

        # Primeiro agendamento ok
        gerenciador.agendar_consulta(medico, paciente1, "2026-04-23", "09:00")

        # Segundo agendamento no mesmo horário deve falhar
        with self.assertRaises(ValueError) as context:
            gerenciador.agendar_consulta(medico, paciente2, "2026-04-23", "09:00")
        self.assertEqual(
            str(context.exception), MensagensErro.CONFLITO_DE_HORARIO.value
        )
