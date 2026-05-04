from unittest import TestCase

from enums.mensagens_erro import MensagensErro
from service.paciente_service import PacienteService


class TestPacienteService(TestCase):

    def test_cadastrar_paciente(self):
        service = PacienteService()
        paciente = service.cadastrar_paciente(
            "Matheus", "11122233344", "01/01/1980", "11999999999"
        )

        self.assertEqual(paciente.nome, "Matheus")
        self.assertEqual(len(service.listar_pacientes()), 1)

    def test_cadastrar_paciente_duplicado(self):
        service = PacienteService()
        service.cadastrar_paciente(
            "Matheus", "11122233344", "01/01/1980", "11999999999"
        )

        with self.assertRaises(ValueError) as context:
            service.cadastrar_paciente(
                "Outro", "11122233344", "02/02/1990", "11999999999"
            )

        self.assertEqual(
            str(context.exception), MensagensErro.PACIENTE_JA_CADASTRADO.value
        )
