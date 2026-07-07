# --- FUNÇÕES DO SISTEMA DE CAIXA ELETRÔNICO ---

def consultar_saldo(saldo):
    print(f"\nSaldo atual: R${saldo:.2f}")

def depositar(saldo, valor):
    if valor > 0:
        novo_saldo = saldo + valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        return novo_saldo
    else:
        print("Erro: O valor do depósito deve ser maior que zero.")
        return saldo # Se der erro, retorna o saldo antigo sem alterar
def sacar(saldo, valor):
    if valor <= 0:
        print("Erro: O valor do saque deve ser maior que zero.")
        return saldo
    elif valor > saldo:
        print("Erro: Saldo insuficiente para realizar a operação.")
        return saldo
    else:
        novo_saldo = saldo - valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
        return novo_saldo
    
def registrar_transacao(extrato, tipo, valor):
    # Cria um dicionário com os dados da transação e adiciona na lista
    transacao = {"tipo": tipo, "valor": valor}
    extrato.append(transacao)


def exibir_extrato(extrato):
    print("\n=== EXTRATO BANCÁRIO ===")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for transacao in extrato:
            print(f"{transacao['tipo']}: R${transacao['valor']:.2f}")
    print("========================")

# --- FLUXO PRINCIPAL DO CAIXA ELETRÔNICO ---

saldo = 1000.0
extrato = [] # Lista iniciada vazia antes do loop

while True:
    print("\n=== Caixa Eletrônico ===")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Ver extrato")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Obrigado por usar o nosso banco!")
        break
        
    elif opcao == "1":
        consultar_saldo(saldo)
        
    elif opcao == "2":
        valor_saque = float(input("Valor do saque: "))
        saldo_antigo = saldo
        saldo = sacar(saldo, valor_saque)
        
        # Se o saldo mudou, significa que o saque foi bem-sucedido
        if saldo != saldo_antigo:
            registrar_transacao(extrato, "Saque", valor_saque)

    elif opcao == "3":
        valor_deposito = float(input("Valor do depósito: "))
        saldo_antigo = saldo
        saldo = depositar(saldo, valor_deposito)
        
        # Se o saldo mudou, significa que o depósito foi bem-sucedido
        if saldo != saldo_antigo:
            registrar_transacao(extrato, "Depósito", valor_deposito)

    elif opcao == "4":
        exibir_extrato(extrato)

    else:
        print("Opção inválida, tente novamente.")
        
