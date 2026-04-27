# PARA SEGUNDA-FEIRA

## Tarefas

1. Explicar o que é o diagrama de C4 e criar o do meu projeto  
2. Verificar se o código dos menus estão Ok  
3. Quando finalizado, se houver mudanças, commitar em uma branch nova, mandar para o vini e ficar testando o sistema da GestãoDS para estudo  

---

# Objetivo

O objetivo dessa implementação é desenvolver um sistema simples de agendamento de consultas médicas seguindo a metodologia de desenvolvimento TDD (Test-Driven Development - Desenvolvimento Orientado a Testes) onde as classes de testes do sistema são desenvolvidas antes da lógica das services (métodos funcionais do sistema), o sistema terá diversas regras de negócio, funcionalidades e um Menu no terminal para testar as funcionalidades do sistema.

---

# Estrutura do Projeto

```python
TDD-Agendamento-Consulta/               # Diretório raiz do projeto
|--- enums/                             # Pasta contendo enumeradores com variáveis estáticas como mensagens de erros, etc...
|    |--- mensagens_erro.py             # Centraliza as mensagens de erro padronizadas do sistema
|--- models/                            # Pasta com as classes de modelo (entidades fundamentais de negócio)
|    |--- medico.py                     # Define as características e comportamentos da entidade Médico
|    |--- paciente.py                   # Define as características e comportamentos da entidade Paciente
|--- service/                           # Pasta para regras de negócio mais complexas e orquestração
|    |--- agendamentos.py               # Contém a lógica para realizar, validar e gerenciar agendamentos
|--- tests/                             # Pasta com toda a suíte de testes automatizados (essencial para o TDD)
|    |--- test_medico.py                # Testes unitários para garantir o correto funcionamento do modelo Médico
|    |--- test_paciente.py              # Testes unitários para garantir o correto funcionamento do modelo Paciente
|    |--- tests_agendamento.py          # Testes das regras de negócio do serviço de agendamentos
|--- C4/                                # Pasta que será utilizada para documentação arquitetural (Diagramas C4 Model)
|--- .gitignore                         # Arquivo de configuração que avisa o Git quais arquivos o versionamento deve ignorar
|--- main.py                            # Arquivo principal que inicia todo o sistema (Entry Point)
|--- menu_medico.py                     # Telas e interações via terminal (CLI) específicas para o usuário Médico
|--- menu_paciente.py                   # Telas e interações via terminal (CLI) específicas para o usuário Paciente
|--- menu_secretaria.py                 # Telas e interações via terminal (CLI) para os administradores/secretaria
|--- requirements.txt                   # Lista com todas as bibliotecas e dependências Python necessárias para o projeto rodar

```
---

# Regras de Negócio do Sistema

## Tests Médico(a)

1. Testa a criação bem sucedida de um médico  
2. Testa a criação bem sucedida de uma grade de horários, informando um intervalo de horários  
3. Testa a criação errada de uma grade de horários, caso o médico informa um intervalo errado  
4. Testa a criação de um médico com dados obrigatórios faltando (como Nome e CPF)  
5. Testa de um médico já está cadastrado no mesmo CPF  

---

## Tests Paciente

1. Testa a criação bem sucedida de um paciente  
2. Testa a exibição de um paciente em string para leitura do usuário final  
3. Testa uma verificação se um paciente está tentando efetuar o cadastro com o mesmo CPF de outro paciente já cadastrado  
4. Testa a criação de um paciente com dados obrigatórios faltando (como Nome e CPF)  

---

## Tests Agendamento

1. Testa a criação de um agendamento de uma consulta com sucesso  
2. Testa o cancelamento de uma consulta com sucesso  
3. Testa o agendamento de uma consulta informando um horário inválido  
4. Testa o agendamento de uma consulta fora do horário de trabalho do(a) médico(a)  
5. Testa o agendamento de uma consulta no mesmo horário que outra pessoa já agendou  

---

# Como executar o projeto

## 1 - Clone esse repositório na branch V3

```python
git clone --single-branch --branch <nome_do_branch> <url_do_repositorio>
git clone --single-branch --branch V3 https://github.com/Nogz04/TDD-agendamento-consulta.git
```

2- Abra o terminal e crie e inicie o venv

```python
Ctrl + ' # -> Abre o terminal

python -m venv venv # Cria o ambiente virtual
.\venv\Scripts\activate # Entra no ambiente virtual
```

3- Baixe o requirements.txt no terminal (se houver algo na pasta)

```python
pip install -r requirements.txt
```

4- Inicie o menu do sistema no terminal

```python
python .\main.py # Inicia o menu no terminal para você testar o sistema

# O sistema irá executar todos os testes antes de iniciar o menu, se todos passarem, o menu irá iniciar.
```

5- Rodando testes sem precisar rodar o menu

```python
python -m unittest discover tests
```
