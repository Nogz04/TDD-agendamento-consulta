from dataclasses import dataclass

@dataclass
class Paciente():
    nome: str
    data_nascimento: str
    telefone: str
    
    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.telefone}"
