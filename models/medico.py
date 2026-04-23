from enums.mensagens_erro import MensagensErro
from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta 

@dataclass
class Medico:
    nome: str
    horario_inicio: str
    horario_fim: str
    horarios_disponiveis: List[str] = field(init=False)

    def __post_init__(self): 
        self.horarios_disponiveis = self.gerar_grade_horarios()

    def gerar_grade_horarios(self) -> List[str]:
        horarios = []
        try:
            inicio = datetime.strptime(self.horario_inicio, "%H:%M")
            fim = datetime.strptime(self.horario_fim, "%H:%M")
            
            atual = inicio
            while atual <= fim:
                horarios.append(atual.strftime("%H:%M"))
                atual += timedelta(minutes=30)
                
        except ValueError:
            raise ValueError(MensagensErro.HORARIO_INVALIDO.value)
            
        return horarios

    def __str__(self):
        return f"Dr(a). {self.nome}"
