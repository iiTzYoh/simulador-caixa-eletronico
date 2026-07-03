saldo = 1000.0

while True:
    print("\n=== Caixa Eletrônico ===")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "4":
        print("Obrigado por usar o nosso banco!")
        break
        
    elif opcao == "1":
        print(f"Saldo atual: R${saldo:.2f}")
        
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        # Este IF precisa estar "dentro" do elif opcao == 2
        if valor > 0 and valor <= saldo:
            saldo -= valor  # Esta linha precisa estar dentro do IF
            print(f"Saque realizado. Novo saldo: R${saldo:.2f}")
        else:
            # Este ELSE pertence ao IF do saque
            print("Valor inválido ou saldo insuficiente.")

    elif opcao == "3":
        valor = float(input("Valor do depósito: "))
        # Este IF precisa estar "dentro" do elif opcao == 3
        if valor > 0:
            saldo += valor  # Esta linha precisa estar dentro do IF
            print(f"Depósito realizado. Novo saldo: R${saldo:.2f}")
        else:
            # Este ELSE pertence ao IF do depósito
            print("Valor inválido.")
            
    else:
        # Este ELSE final pertence à escolha das opções do menu inicial
        print("Opção inválida, tente novamente.")