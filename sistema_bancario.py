menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite =500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito = float(input("Insira o valor do depósito: "))

        if valor_deposito < 0:
            print("Depósito invalido. O valor deve ser maior que 0")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

            print("Depósito realizado com sucesso.")

    elif opcao == "s":
        print("Saque")

        valor_saque = float(input("Insira o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques excedido.")
        elif valor_saque > saldo: 
            print("Saldo insuficiente.")
        elif valor_saque > 500:
            print("o limite de saque é R$ 500.00")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"

            print("Saque realizado com sucesso.")
 
    elif opcao == "e":
        print("Extrato")

        if not extrato:
            print("Não foram realizadas movimentações.")
        
        else:
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")