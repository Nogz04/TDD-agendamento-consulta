from unittest import TestCase

from enums.mensagens_erro import MensagensErro
from models.medico import Medico


class TestMedico(TestCase):

    def test_criar_medico(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        self.assertEqual(medico.nome, "Dr House")
        self.assertEqual(medico.cpf, "12345678900")
        self.assertEqual(medico.horario_inicio, "08:00")
        self.assertEqual(medico.horario_fim, "10:00")

    def test_gerar_grade_horarios(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        esperado = ["08:00", "08:30", "09:00", "09:30", "10:00"]
        # In the refactored code, `medico.horarios_disponiveis` is gone.
        # We need to test `gerar_grade_horarios()` directly
        self.assertEqual(medico.gerar_grade_horarios(), esperado)

    def test_gerar_grade_horarios_com_erro(self):
        with self.assertRaises(ValueError) as context:
            Medico("Dr House", "12345678900", "08:00", "10")
            # Wait! Generating schedule in __post_init__ was removed.
            # So creating the Medico won't raise ValueError anymore until `gerar_grade_horarios()` is called.
            # Let's call it.
            medico = Medico("Dr House", "12345678900", "08:00", "10")
            medico.gerar_grade_horarios()

        self.assertEqual(str(context.exception), MensagensErro.HORARIO_INVALIDO.value)

    def test_medico_com_dados_invalidos(self):
        with self.assertRaises(ValueError) as context:
            Medico("", "12345678900", "08:00", "10:00")
        self.assertEqual(
            str(context.exception), MensagensErro.MEDICO_DADOS_INVALIDOS.value
        )
        with self.assertRaises(ValueError) as context:
            Medico("Dr House", "", "08:00", "10:00")
        self.assertEqual(
            str(context.exception), MensagensErro.MEDICO_DADOS_INVALIDOS.value
        )

    def test_str_medico(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        self.assertEqual(str(medico), "Dr(a). Dr House (CPF: 12345678900)")
