# 🏥 TDD Agendamento de Consultas Médicas

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-Pytest-white?logo=pytest&logoColor=red)
![Pylint](https://img.shields.io/badge/Linter-Pylint-blue?logo=python&logoColor=white)
![Mypy](https://img.shields.io/badge/Type_Check-Mypy-blue)
![Taskipy](https://img.shields.io/badge/Task_Runner-Taskipy-red)

Um sistema de gerenciamento e agendamento de consultas médicas via terminal (CLI) desenvolvido rigorosamente com a metodologia **TDD (Test-Driven Development)** e seguindo princípios de **Clean Architecture**.

---

## 🎯 Objetivo

O objetivo central desta implementação é garantir que cada regra de negócio do mundo real nasça a partir de testes automatizados seguros. A arquitetura foi desenhada priorizando a integridade dos dados e garantindo altíssima testabilidade, separando com clareza as responsabilidades de modelos (Models), lógicas operacionais (Services) e interação visual com o usuário (Menus).

---

## 📂 Estrutura do Projeto

Abaixo apresentamos a árvore arquitetural deste sistema:

```text
TDD-Agendamento-Consulta/
├── src/                        # Código-fonte principal da aplicação
│   ├── enums/                  # Constantes e Enumeradores
│   │   └── mensagens_erro.py
│   ├── menus/                  # Telas de menu para Interação com o Usuário
│   │   ├── menu_medico.py
│   │   ├── menu_paciente.py
│   │   └── menu_secretaria.py
│   ├── models/                 # Entidades de Negócio (Camada de Domínio)
│   │   ├── consulta.py
│   │   ├── medico.py
│   │   └── paciente.py
│   ├── service/                # Regras de Negócio e Casos de Uso
│   │   ├── agendamentos.py
│   │   ├── medico_service.py
│   │   └── paciente_service.py
│   └── main.py                 # Entry Point da aplicação
├── tests/                      # Testes Unitários (TDD)
│   ├── test_agendamento.py
│   ├── test_medico.py
│   ├── test_medico_service.py
│   ├── test_paciente.py
│   └── test_paciente_service.py
├── .pre-commit-config.yaml     # Hooks de pré-commit (Lint/Format)
├── pyproject.toml              # Configurações de ferramentas (Pytest, Mypy, Pylint, Black)
├── requirements-dev.txt        # Dependências de desenvolvimento
└── requirements.txt            # Dependências de produção
```

---

## 📋 Regras de Negócio e Casos de Uso (TDD)

### 🩺 Médico(a)
- **Criação de Cadastro:** Exige CPF único e dados obrigatórios informados.
- **Grade de Horários:** Gera janelas automáticas de 30 em 30 minutos a partir do turno de trabalho.
- **Validação de Turno:** Rejeita jornada de trabalho inválida (ex: horário de fim menor que o de início).

### 🤕 Paciente
- **Criação de Cadastro:** Exige CPF único e dados vitais preenchidos.
- **Formatação de Dados:** Retorna visualização padronizada para relatórios (`Nome (CPF: X) ...`).
- **Antiduplicação:** Bloqueia dinamicamente recadastros com CPFs existentes.

### 📅 Agendamentos
- **Marcação Segura:** Exige que a consulta tente ser alocada estritamente dentro da grade horária disponível do profissional.
- **Liberação de Horário:** Devolve automaticamente a janela de tempo cancelada para a agenda do médico.
- **Validação de Formato:** Rejeita tentativas de marcação de horários diferentes de `HH:MM`.
- **Prevenção de Overbooking:** Bloqueia agendamentos simultâneos para o mesmo médico no mesmo horário.

---

## 🏗️ Arquitetura e Decisões de Projeto

O projeto adota uma estrutura inspirada em **Clean Architecture** para garantir que a lógica de negócio seja independente de frameworks e interfaces:

- **Models (Domínio):** Contém as entidades puras e regras básicas (ex: `Medico`, `Paciente`, `Consulta`).
- **Services (Aplicação):** Onde reside a orquestração e as regras complexas (ex: geração de grade, validação de conflitos).
- **Menus (Interface):** Camada de interação que consome os serviços, permitindo que a UI mude sem afetar o coração do sistema.
- **Enums:** Padronização de mensagens de erro e estados para evitar strings "mágicas" no código.

---

## 🚀 Como Executar o Programa (Como Usuário Final)

Deseja experimentar a interface sem se preocupar em codificar? Siga o passo a passo seguro para dar a partida:

**1. Clone o repositório no seu computador:**
```bash
git clone https://github.com/Nogz04/TDD-agendamento-consulta.git
cd TDD-agendamento-consulta

# ou

git clone --single-branch --branch main https://github.com/Nogz04/TDD-agendamento-consulta.git
cd TDD-agendamento-consulta
```

**2. Crie e ative a bolha de ambiente virtual para evitar conflitos na sua máquina:**
```bash
# Invoque a criação:
python -m venv venv

# Ative no Windows:
.\venv\Scripts\activate

# Se estiver no Linux/Mac substitua por:
source venv/bin/activate
```

*(Observação: Atualmente o projeto utiliza bibliotecas padrão do Python para garantir a compatibilidade e leveza, com foco total na lógica de negócio e testes.)*

**3. Inicie o Módulo Principal:**
Você pode rodar facilmente a aplicação através do nosso gerenciador de tarefas (caso tenha instalado as dependências de dev) ou diretamente pelo Python:
```bash
# Se tiver instalado as dependências de desenvolvedor:
task run

# Se não tiver instalado dependências (puro Python):
python src/main.py
```

---

## 🛠️ Guia para Desenvolvedores (Ambiente Profissional)

Deseja contribuir ou aprender com nossa infraestrutura? Construímos um laboratório blindado com avaliações estáticas agressivas e gatilhos de integração.

**1. Sincronize a Caixa de Ferramentas de Arquitetura:**
Após garantir o VENV (`passo 2` acima ativado), levante as dependências especiais:
```bash
pip install -r requirements-dev.txt
```

**2. Ative as Travas de Segurança Locais (`Pre-Commit`):**
Instale o fiscal de Git! Da próxima vez que você realizar um `git commit`, robôs invisíveis automaticamente arrumarão linhas em branco desnecessárias ou impedirão que linhas sintaticamente horrendas entrem no github do time:
```bash
pre-commit install
```

### 🧰 Principais Comandos do Cotidiano (Via Taskipy):

O nosso projeto aboliu scripts de sistema operacional e agora usa o **Taskipy** em conjunto com o `pyproject.toml` para ser 100% multiplataforma.

Basta rodar os atalhos abaixo no seu terminal:

* **Iniciação de TDD e Emissão de Cobertura Final de Código**
  ```bash
  task test        # Roda o Pytest com relatório de cobertura das pastas src/ e tests/
  ```
* **Estética de Código Cega**
  ```bash
  task format      # Aciona Black e Isort de uma só vez para arrumar o código
  ```
* **Análise Lógica Externa**
  ```bash
  task lint        # Executa o Flake8 e o rigoroso Pylint
  task typecheck   # Validação estática de tipagem de dados via Mypy
  ```

* **Automação Completa da Esteira (Sua Pipeline Local)**
  ```bash
  task check       # Executa TODOS os testes e ferramentas acima sequencialmente.
  ```
