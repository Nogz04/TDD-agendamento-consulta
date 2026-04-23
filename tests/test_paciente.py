from unittest import TestCase
from models.paciente import Paciente

class TestPaciente(TestCase):
    
    def test_criar_paciente(self):
        paciente = Paciente("Matheus", "01/01/1980", "11999999999")
        self.assertEqual(paciente.nome, "Matheus")
        self.assertEqual(paciente.data_nascimento, "01/01/1980")
        self.assertEqual(paciente.telefone, "11999999999")

    def test_str_paciente(self):
        paciente = Paciente("Matheus", "01/01/1980", "11999999999")
        self.assertEqual(str(paciente), "Matheus - 01/01/1980 - 11999999999")