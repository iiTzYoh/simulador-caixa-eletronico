# 🏦 Simulador de Caixa Eletrônico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Codespaces](https://img.shields.io/badge/Codespaces-181717?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

Um simulador de caixa eletrônico interativo em Python, focado em boas práticas de Programação Orientada a Objetos (POO), resiliência e persistência de dados.

## 🚀 Funcionalidades e Arquitetura

- **Orientação a Objetos:** Lógica de negócio encapsulada de forma modular na classe `ContaBancaria`.
- **Persistência de Dados (JSON):** O saldo e o histórico de transações são salvos localmente. Ao reiniciar a aplicação, o estado da conta é restaurado automaticamente, garantindo a continuidade das operações.
- **Tratamento de Exceções:** Sistema robusto com `try/except/finally` para evitar crashes por entradas inválidas do usuário (ex: validação de _floats_ contra _strings_).
- **Operações Básicas:** Consultar saldo, depósitos, saques (com regras de negócio e validação de saldo insuficiente) e exibição de extrato formatado.

## 🛠️ Como executar o projeto

1. Clone este repositório:
  git clone https://github.com/iiTzYoh/simulador-caixa-eletronico.git
