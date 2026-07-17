class ContaBancaria:
    # Utilizando 'None' para evitar a armadilha do argumento padrão mutável
    def __init__(self, titular, saldo_inicial=0.0, extrato_inicial=None):
        self.titular = titular
        self.saldo = saldo_inicial
        
        # Se não vier extrato do JSON, inicia uma nova lista vazia na memória.
        # Se vier, utiliza a lista carregada do disco.
        if extrato_inicial is None:
            self.extrato = []
        else:
            self.extrato = extrato_inicial

    def consultar_saldo(self):
        print(f"\nSaldo atual: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
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

    def __str__(self):
        return f"Conta de {self.titular} — Saldo Atual: R${self.saldo:.2f}"