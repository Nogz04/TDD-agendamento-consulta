# 🏥 TDD Agendamento de Consultas Médicas

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TDD](https://img.shields.io/badge/TDD-100%25_Coverage-green)
![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pylint](https://img.shields.io/badge/Pylint-10.00%2F10-brightgreen)

Um sistema robusto de gerenciamento e agendamento de consultas médicas via terminal (CLI) desenvolvido desde o princípio com a metodologia **TDD (Test-Driven Development)**, adotando as melhores práticas do ecossistema Python moderno (Clean Code, Tipagem Estática, Linters rigorosos e automação de commits).

---

## 🎯 Objetivo

O objetivo central desta implementação é garantir que cada regra de negócio do mundo real nasça a partir de testes automatizados seguros. A arquitetura foi desenhada priorizando a integridade dos dados e garantindo altíssima testabilidade, separando com clareza as responsabilidades de modelos (Models), lógicas operacionais (Services) e interação visual com o usuário (Menus).

---

## 📂 Estrutura do Projeto

Abaixo apresentamos a árvore arquitetural deste sistema:

```text
TDD-Agendamento-Consulta/
├── enums/                      # Constantes e Enumeradores
│   └── mensagens_erro.py       # Centraliza avisos do sistema (ex: Paciente já cadastrado, etc)
├── menus/                      # Telas de Interação com o Usuário (Terminal Inteligente)
│   ├── menu_medico.py
│   ├── menu_paciente.py
│   └── menu_secretaria.py
├── models/                     # Entidades de Negócio do Domínio
│   ├── medico.py               # Define as propriedades e atributos inerentes de um Médico
│   └── paciente.py             # Define as propriedades e atributos inerentes de um Paciente
├── service/                    # Orquestração e Lógica de Negócio
│   └── agendamentos.py         # Motor principal que acopla lógicas de busca e verificação
├── tests/                      # Suíte integral de Testes Unitários de TDD
│   ├── test_agendamento.py
│   ├── test_medico.py
│   └── test_paciente.py
├── C4/                         # Diagramas Contextuais da Arquitetura (C4 Model)
├── .pre-commit-config.yaml     # Regras de proteção do Git Hooks contra envios fora de padrão
├── pyproject.toml              # Central de configurações avançadas do Pytest, Mypy e Pylint
├── requirements-dev.txt        # Dependências exclusivas para desenvolvimento e arquitetura
├── requirements.txt            # Dependências exclusivas do ciclo de produção (Vazio por design)
└── main.py                     # Entry Point Primário - Bloqueado por validação de testes
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

## 🚀 Como Executar o Programa (Como Usuário Final)

Deseja experimentar a interface sem se preocupar em codificar? Siga o passo a passo seguro para dar a partida:

**1. Clone o repositório no seu computador:**
```bash
git clone --single-branch --branch V3 https://github.com/Nogz04/TDD-agendamento-consulta.git
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

*(Observação Importante: Apesar das boas práticas indicarem `pip install -r requirements.txt`, informamos que nosso projeto não depende de nenhuma lib externa em estado de Produção! Todo o core utiliza apenas bibliotecas padrões fornecidas pela base da linguagem Python).*

**3. Inicie o Módulo Principal:**
O terminal fará uma varredura rigorosa. Se nem sequer uma das regras do sistema estiver quebrada, os acessos serão liberados.
```bash
python main.py
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

### 🧰 Principais Comandos do Cotidiano:

* **Iniciação de TDD e Emissão de Cobertura Final de Código (`Pytest`)**
  ```bash
  pytest -v                                # Inspeção Detalhada
  pytest --cov=. --cov-report=term-missing # Relatório Tático e apuração de pontos cegos
  ```
* **Estética de Código Cega (`Black` e `Isort`)**
  ```bash
  isort .          # Varre seus Cabeçalhos para deixá-los alfabéticos e dividos
  black .          # Reforma Milimetricamente margens, quebras e espaçamentos no padrão PEP8
  ```
* **Análise Lógica Externa (`Pylint` e `Mypy`)**
  ```bash
  mypy .                           # Revisor de Tipo de Dados (Evita que receba Texto no lugar de Float, etc...)
  pylint models service main.py    # Avaliador de Saúde Qualitativa e Atribuidor de Notas de 0 a 10
  ```
