from unittest import TestCase

from enums.mensagens_erro import MensagensErro
from models.medico import Medico
from models.paciente import Paciente
from service.agendamentos import AgendamentoService


class TestAgendamentoService(TestCase):

    def test_agenda_consulta_com_sucesso(self):
        gerenciador = AgendamentoService()

        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        resultado = gerenciador.agendar_consulta(
            medico, paciente, "2026-04-23", "10:00"
        )

        self.assertTrue(resultado)
        self.assertEqual(len(gerenciador.consultas_agendadas), 1)
        consulta = gerenciador.consultas_agendadas[0]
        self.assertEqual(consulta.medico, medico)
        self.assertEqual(consulta.data, "2026-04-23")
        self.assertEqual(consulta.hora, "10:00")

    def test_cancelar_consulta(self):
        gerenciador = AgendamentoService()

        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "55984039186")

        resultado = gerenciador.agendar_consulta(
            medico, paciente, "2026-04-23", "10:00"
        )
        self.assertTrue(resultado)

        resultado = gerenciador.cancelar_consulta(medico, "2026-04-23", "10:00")
        self.assertTrue(resultado)
        self.assertEqual(len(gerenciador.consultas_agendadas), 0)

    def test_horario_invalido(self):
        gerenciador = AgendamentoService()

        self.assertFalse(gerenciador.validar_formato_horario("25:00"))
        self.assertFalse(gerenciador.validar_formato_horario("10:65"))
        self.assertFalse(gerenciador.validar_formato_horario("9:00"))
        self.assertFalse(gerenciador.validar_formato_horario("1000"))
        self.assertFalse(gerenciador.validar_formato_horario("-10:00"))

        self.assertTrue(gerenciador.validar_formato_horario("08:30"))

    def test_agendamento_fora_do_horario(self):
        gerenciador = AgendamentoService()
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        with self.assertRaises(ValueError) as context:
            gerenciador.agendar_consulta(medico, paciente, "2026-04-23", "11:00")
        self.assertEqual(
            str(context.exception), MensagensErro.HORARIO_INDISPONIVEL.value
        )

    def test_prevencao_sobreposicao_conflito_agendamento(self):
        gerenciador = AgendamentoService()
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        paciente1 = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")
        paciente2 = Paciente("Douglas", "55566677788", "02/02/1990", "11888888888")

        gerenciador.agendar_consulta(medico, paciente1, "2026-04-23", "09:00")

        # Conflito no mesmo dia
        with self.assertRaises(ValueError) as context:
            gerenciador.agendar_consulta(medico, paciente2, "2026-04-23", "09:00")
        self.assertEqual(
            str(context.exception), MensagensErro.CONFLITO_DE_HORARIO.value
        )

        # Sem conflito em dias diferentes
        resultado = gerenciador.agendar_consulta(
            medico, paciente2, "2026-04-24", "09:00"
        )
        self.assertTrue(resultado)

    def test_cancelamento_consulta_inexistente(self):
        gerenciador = AgendamentoService()
        medico = Medico("Dr House", "12345678900", "08:00", "12:00")

        resultado = gerenciador.cancelar_consulta(medico, "2026-04-23", "11:00")
        self.assertFalse(resultado)

    def test_agendamento_com_formato_horario_invalido(self):
        gerenciador = AgendamentoService()
        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        with self.assertRaises(ValueError) as context:
            gerenciador.agendar_consulta(medico, paciente, "2026-04-23", "25:00")

        self.assertEqual(str(context.exception), MensagensErro.HORARIO_INVALIDO.value)

    def test_validar_formato_que_aciona_excecoes(self):
        gerenciador = AgendamentoService()
        self.assertFalse(gerenciador.validar_formato_horario("aa:bb"))
        self.assertFalse(gerenciador.validar_formato_horario(None))

    def test_listagens_de_consultas_e_horarios(self):
        gerenciador = AgendamentoService()
        medico = Medico("Dr House", "12345678900", "08:00", "12:00")
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")

        gerenciador.agendar_consulta(medico, paciente, "2026-04-23", "10:00")

        self.assertEqual(len(gerenciador.listar_consultas_agendadas()), 1)
        self.assertEqual(len(gerenciador.listar_agendamentos(medico)), 1)
        self.assertEqual(len(gerenciador.listar_consultas_por_paciente(paciente)), 1)

        # Dos 9 horários possíveis (08:00 a 12:00 = 9 turnos de 30m), 1 foi ocupado na data.
        self.assertEqual(
            len(gerenciador.listar_horarios_disponiveis(medico, "2026-04-23")), 8
        )
        # Em outro dia, todos devem estar livres
        self.assertEqual(
            len(gerenciador.listar_horarios_disponiveis(medico, "2026-04-24")), 9
        )
