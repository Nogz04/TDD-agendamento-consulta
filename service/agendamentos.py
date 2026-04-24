from models.medico import Medico
from models.paciente import Paciente
from enums.mensagens_erro import MensagensErro

class RealizarAgendamento():  

    def __init__(self):
        self._consultas_agendadas = []

    @property
    def consultas_agendadas(self):
        return self._consultas_agendadas

    def agendar_consulta(self, medico: Medico, paciente: Paciente, data: str, hora: str) -> bool:
        if not self.validar_formato_horario(hora):
            raise ValueError(MensagensErro.HORARIO_INVALIDO.value)
        
        self.verificar_horario_disponivel(medico, hora) # Verifica se o horário está disponível
        self.remover_horario_disponivel(medico, hora) # Remove o horário da lista do médico
        self._consultas_agendadas.append(f"Consulta: {medico.nome} - {paciente.nome} em {data} às {hora}")
        
        return True


    def cancelar_consulta(self, medico: Medico, hora: str) -> bool:
        if hora not in medico.horarios_disponiveis:
            medico.horarios_disponiveis.append(hora)
            medico.horarios_disponiveis.sort() # Ordena a lista
            
            consultas_a_remover = [c for c in self._consultas_agendadas if f"{medico.nome} -" in c and f"às {hora}" in c]
            for c in consultas_a_remover:
                self._consultas_agendadas.remove(c)
                
            return True
        return False  


    # Metodos auxiliares de verificação para o método agendar_consulta

    def verificar_horario_disponivel(self, medico: Medico, hora: str) -> bool:
        if hora not in medico.horarios_disponiveis:
            # Se o horário está na grade original mas não na disponível, é porque já foi agendado
            if hora in medico.gerar_grade_horarios():
                raise ValueError(MensagensErro.CONFLITO_DE_HORARIO.value)
            # Se não está nem na grade original, é porque está fora da jornada de trabalho
            raise ValueError(MensagensErro.HORARIO_INDISPONIVEL.value)
        return True

    def remover_horario_disponivel(self, medico: Medico, hora: str) -> bool:
        if hora in medico.horarios_disponiveis:
            medico.horarios_disponiveis.remove(hora)
            return True
        return False


    # Verifica se o horário está no formato HH:MM e se os valores são válidos.
    def validar_formato_horario(self, hora: str) -> bool:
    
        try:
            if ":" not in hora or len(hora) != 5:
                return False
            
            partes = hora.split(":") # EX: 10:00 -> ["10", "00"]
            horas = int(partes[0]) # EX: "10" -> 10
            minutos = int(partes[1]) # EX: "00" -> 0

            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                return False
                
            return True
        except (ValueError, IndexError, TypeError):
            return False

    def listar_agendamentos(self, medico: Medico) -> list[str]:
        return self._consultas_agendadas

    # Metodos de funcionalidades extras
    def listar_horarios_disponiveis(self, medico: Medico) -> list[str]:
        return medico.horarios_disponiveis

    def listar_consultas_por_paciente(self, paciente: Paciente) -> list[str]:
        return [consulta for consulta in self._consultas_agendadas if paciente.cpf in consulta]

    def listar_consultas_agendadas(self) -> list[str]:
        return self._consultas_agendadas

