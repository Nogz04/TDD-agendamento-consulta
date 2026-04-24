from unittest import TestCase
from models.medico import Medico
from enums.mensagens_erro import MensagensErro

class TestMedico(TestCase):

    def setUp(self):
        Medico.limpar_registros() # Limpa o registro de médicos antes de cada teste, para que os testes não interfiram uns nos outros
        

    def test_criar_medico(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        self.assertEqual(medico.nome, "Dr House")
        self.assertEqual(medico.cpf, "12345678900")
        self.assertEqual(medico.horario_inicio, "08:00")
        self.assertEqual(medico.horario_fim, "10:00")

    def test_gerar_grade_horarios(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        esperado = ["08:00", "08:30", "09:00", "09:30", "10:00"]
        self.assertEqual(medico.horarios_disponiveis, esperado)

    def test_gerar_grade_horarios_com_erro(self):

        with self.assertRaises(ValueError) as context:
            medico = Medico("Dr House", "12345678900", "08:00", "10")
        self.assertEqual(str(context.exception), MensagensErro.HORARIO_INVALIDO.value)

    def test_medico_com_dados_invalidos(self):
        with self.assertRaises(ValueError) as context:
            medico = Medico("", "12345678900", "08:00", "10:00")
        self.assertEqual(str(context.exception), MensagensErro.MEDICO_DADOS_INVALIDOS.value)
        with self.assertRaises(ValueError) as context:
            medico = Medico("Dr House", "", "08:00", "10:00")
        self.assertEqual(str(context.exception), MensagensErro.MEDICO_DADOS_INVALIDOS.value)


    def test_medico_ja_cadastrado(self):
        medico = Medico("Dr House", "12345678900", "08:00", "10:00")
        with self.assertRaises(ValueError) as context:
            medico2 = Medico("Dr House", "12345678900", "08:00", "10:00")
        self.assertEqual(str(context.exception), MensagensErro.MEDICO_JA_CADASTRADO.value)

    
        
        
