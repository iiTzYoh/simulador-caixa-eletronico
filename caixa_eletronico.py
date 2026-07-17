import json
from conta_bancaria import ContaBancaria

NOME_ARQUIVO = 'dados_conta.json'
NOME_TITULAR = 'Yoshiharu Ishii'

print("Iniciando sistema...")
try:
    with open(NOME_ARQUIVO, 'r') as arquivo:
        dados = json.load(arquivo)
        conta = ContaBancaria(NOME_TITULAR, dados['saldo'], dados['extrato'])
        print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Nenhum dado anterior encontrado. Criando nova conta.")
    conta = ContaBancaria(NOME_TITULAR, 1000.0)


# --- LOOP PRINCIPAL ---
while True:
    print("\n=== Caixa Eletrônico (Modular & Robusto) ===")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Ver extrato")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        # Antes de quebrar o loop, salva o estado atual no disco
        dados_para_salvar = {
            "saldo": conta.saldo,
            "extrato": conta.extrato
        }
        with open(NOME_ARQUIVO, 'w') as arquivo:
            # indent=4 deixa o arquivo JSON formatado bonito e legível
            json.dump(dados_para_salvar, arquivo, indent=4)
            
        print("Dados salvos com segurança. Obrigado por usar nosso banco!")
        break

    elif opcao == "1":
        print(f"\n{conta}")

    elif opcao == "2":
        try:
            valor_saque = float(input("Valor do saque: "))
            conta.sacar(valor_saque)
        except ValueError:
            print("Erro de digitação: Por favor, insira apenas números válidos (ex: 50.50).")
        finally:
            print("-" * 30)

    elif opcao == "3":
        try:
            valor_deposito = float(input("Valor do depósito: "))
            conta.depositar(valor_deposito)
        except ValueError:
            print("Erro de digitação: Por favor, insira apenas números válidos (ex: 50.50).")
        finally:
            print("-" * 30)

    elif opcao == "4":
        conta.exibir_extrato()

    else:
        print("Opção inválida, tente novamente.")