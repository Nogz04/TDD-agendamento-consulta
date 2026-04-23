from dataclasses import dataclass

@dataclass
class Paciente():
    nome: str
    cpf: str
    data_nascimento: str
    telefone: str
    
    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf}) - {self.data_nascimento} - {self.telefone}"
