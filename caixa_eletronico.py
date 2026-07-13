# --- CLASSE DO SISTEMA (Molde) ---

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        # Atributos: O estado da conta fica guardado aqui dentro 
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def consultar_saldo(self):
        print(f"\nSaldo atual: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            # O proprio método gerencia o extrato internamente
            self.extrato.append({"tipo": "Depósito", "valor": valor})
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")
            return False

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
            return False
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente para realizar a operação.")
            return False
        else:
            self.saldo -= valor
            self.extrato.append({"tipo": "Saque", "valor": valor})
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            return True

    def exibir_extrato(self):
        print(f"\n=== EXTRATO BANCÁRIO — {self.titular.upper()} ===")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for transacao in self.extrato:
                print(f"{transacao['tipo']}: R${transacao['valor']:.2f}")
        print("========================")

    # 🌟 BÔNUS: Método especial (Dunder Method) para representação em texto
    def __str__(self):
        return f"Conta de {self.titular} — Saldo Atual: R${self.saldo:.2f}"

# --- FLUXO PRINCIPAL (LOOP) ---

# Criando o objeto 'conta' a partir do molde 'ContaBancaria'
conta = ContaBancaria("Adams Yoshiharu Ishii", 1000.0)

while True:
    print("\n=== Caixa Eletrônico (POO) ===")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Ver extrato")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Obrigado por usar nosso banco!")
        break

    elif opcao == "1":
        # Graças ao método bônus __str__, podemos usar o print direto no objeto!
        print(f"\n{conta}")
        
    elif opcao == "2":
        valor_saque = float(input("Valor do saque: "))
        # Não precisamos mais checar se mudou o saldo por fora, o método resolve tudo
        conta.sacar(valor_saque)

    elif opcao == "3":
        valor_deposito = float(input("Valor do depósito: "))
        conta.depositar(valor_deposito)

    elif opcao == "4":
        conta.exibir_extrato()

    else:
        print("Opção inválida, tente novamente.")