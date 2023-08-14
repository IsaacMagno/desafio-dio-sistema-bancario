def menu():
    opcao = input("""

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuario
[q] Sair

=>""")
    return opcao


def depositar(saldo, valor, extrato, /):
    if valor < 0:
        print("Depósito invalido. O valor deve ser maior que 0")

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

    print("Depósito realizado com sucesso.")


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite de saques excedido.")
    elif valor > saldo: 
        print("Saldo insuficiente.")
    elif valor > limite:
        print("o limite de saque é R$ 500.00")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"

        print("Saque realizado com sucesso.")


def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = str(input("Insira o CPF (apenas números): "))

    cpf_cadastrado = any(usuario['cpf'] == cpf for usuario in usuarios)

    if not cpf_cadastrado:
        nome = str(input("Insira o seu nome: "))
        data_nascimento = str(input("Insira a data de nascimento: "))
        endereço = str(input("Insira seu endereço: "))

        usuarios.append({
            "cpf": cpf,
            "nome": nome,
            "data nascimento": data_nascimento,
            "endereço": endereço,
        })

        print("Usuario criado com sucesso!")
    else:
        print("Usuario já cadastrado!")


def criar_conta(agencia, numero_da_conta, usuarios):
    cpf_usuario = input(str("Insira o cpf do usuario (apenas números): "))

    usuario_cadastrado = next((usuario for usuario in usuarios if usuario['cpf'] == cpf_usuario), None)

    if usuario_cadastrado:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "usuario": usuario_cadastrado}
    else:
        print("Usuario não encontrado!")


def listar_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print(linha)
    else:
        print("Nenhuma conta cadastrada!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE = 500

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas= []

    while True:
        opcao = menu()

        if opcao == "d":
            print("Depósito")

            valor = float(input("Insira o valor do depósito: "))

            depositar(saldo, valor, extrato)
        elif opcao == "s":
            print("Saque")

            valor_saque = float(input("Insira o valor do saque: "))

            sacar(saldo = saldo, valor = valor_saque, extrato = extrato, limite = LIMITE, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
        elif opcao == "e":
            print("Extrato")

            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "nc":
            print ("Nova conta")

            numero_conta = len(contas) + 1

            conta  = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            print("Listar contas")

            listar_contas(contas)
        elif opcao == "nu":
            print ("Novo usuario")

            criar_usuario(usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()