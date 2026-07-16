=======

# 🏦 Simulador de Caixa Eletrônico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Codespaces](https://img.shields.io/badge/Codespaces-181717?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

Um simulador de caixa eletrônico interativo desenvolvido em Python. Este projeto roda diretamente no terminal e permite aos usuários realizar operações bancárias básicas, mantendo um registro detalhado das transações.

🧠 Aprendizados
Este projeto foi fundamental para praticar conceitos de fluxo de controle (while, if/elif/else), conversão de tipos de dados, manipulação de strings (f-strings) e o escopo de variáveis dentro e fora de funções em Python.

## 🚀 Funcionalidades

- **Consultar Saldo:** Visualização do saldo atual em tempo real.
- **Depósito:** Adição de valores com validação (apenas valores positivos).
- **Saque:** Subtração de valores com validação de saldo insuficiente e regras de negócio.
- **Extrato Bancário:** Histórico detalhado de todas as transações de saque e depósito válidas durante a sessão.

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python 3:** Linguagem principal do projeto.
- **Clean Code & Modularização:** O código foi refatorado para utilizar funções isoladas (`sacar`, `depositar`, `exibir_extrato`), retirando a carga do loop principal.
- **Estruturas de Dados:** Uso de Listas e Dicionários para gerenciar o histórico do extrato.
  
