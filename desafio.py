menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 1
LIMITE_SAQUES = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        print("===== Deposito =====")
        deposito = float(input("Informe o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito
            print(f"R$ {deposito:.2f} Depositados com sucesso!!!")
            extrato += f"Deposito: R$ {deposito:.2f}\n"

        else: 
            print("Valor invalido, sao permitidos somente valores maiores que 0")

    elif opcao == "s":
        print("===== Saque =====")
        if numero_saques <= LIMITE_SAQUES:
            saque = float(input("Informe o valor a ser sacado: "))
            if saque <= saldo:
                if saque <= limite:
                    saldo -= saque
                    print(f"R$ {saque:.2f} Sacados com sucesso!!!")
                    numero_saques += 1
                    extrato += f"Saque: R$ {saque:.2f}\n"

                else:
                    print(f"Valor limite de saque atingido: {limite}")
            
            else:
                print("Voce nao tem saldo suficiente!!!")
        else:
            print("Quantidade de saques diarias atingida: 3")

    elif opcao == "e":
        print("\n===== Extrato =====")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================")

    elif opcao == "q":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
