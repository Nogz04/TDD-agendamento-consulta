from dataclasses import dataclass
from enums.mensagens_erro import MensagensErro

@dataclass
class Paciente:
    nome: str
    cpf: str
    data_nascimento: str
    telefone: str
    
    def __post_init__(self):
        if not self.nome or not self.cpf:
            raise ValueError(MensagensErro.PACIENTE_DADOS_INVALIDOS.value)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf}) - {self.data_nascimento} - {self.telefone}"
