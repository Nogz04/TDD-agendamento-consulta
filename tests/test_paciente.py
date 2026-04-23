from unittest import TestCase
from models.paciente import Paciente

class TestPaciente(TestCase):
    
    def test_criar_paciente(self):
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")
        self.assertEqual(paciente.nome, "Matheus")
        self.assertEqual(paciente.cpf, "11122233344")
        self.assertEqual(paciente.data_nascimento, "01/01/1980")
        self.assertEqual(paciente.telefone, "11999999999")

    def test_str_paciente(self):
        paciente = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")
        self.assertEqual(str(paciente), "Matheus (CPF: 11122233344) - 01/01/1980 - 11999999999")

    def test_verifica_se_pacientes_tem_mesmo_cpf(self):
        paciente1 = Paciente("Matheus", "11122233344", "01/01/1980", "11999999999")
        paciente2 = Paciente("Lucas", "11122233344", "02/02/1990", "11999999999")
        self.assertEqual(paciente1.cpf, paciente2.cpf)
        