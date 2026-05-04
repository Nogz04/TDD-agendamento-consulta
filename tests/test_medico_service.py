from unittest import TestCase

from enums.mensagens_erro import MensagensErro
from service.medico_service import MedicoService


class TestMedicoService(TestCase):

    def test_cadastrar_medico(self):
        service = MedicoService()
        medico = service.cadastrar_medico("Dr House", "12345678900", "08:00", "10:00")

        self.assertEqual(medico.nome, "Dr House")
        self.assertEqual(len(service.listar_medicos()), 1)

    def test_cadastrar_medico_duplicado(self):
        service = MedicoService()
        service.cadastrar_medico("Dr House", "12345678900", "08:00", "10:00")

        with self.assertRaises(ValueError) as context:
            service.cadastrar_medico("Dr House", "12345678900", "08:00", "10:00")

        self.assertEqual(
            str(context.exception), MensagensErro.MEDICO_JA_CADASTRADO.value
        )
