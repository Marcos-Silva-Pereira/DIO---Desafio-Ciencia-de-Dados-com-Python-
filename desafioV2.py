def menu():

    menu = """

    ========== MENU ==========
    [d] Depositar
    [s] Sacar 
    [e] Extrato
    [u] Criar Usuario
    [v] Ver lista de usuarios
    [c] Criar Conta
    [l] Ver Contas
    [q] Sair

    => """ 
    return input(menu)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    print("===== Saque =====")

    if numero_saques <= limite_saques:
        if valor <= saldo:
            if valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"R$ {valor:.2f} Sacados com sucesso!!!")

            else:
                print(f"Valor limite de saque atingido: {limite}")
            
        else:
            print("Voce nao tem saldo suficiente!!!")
    else:
        print(f"Quantidade de saques diarias atingida: {limite_saques}")

    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):

    print("===== Deposito =====")

    if valor > 0:
        saldo += valor
        print(f"R$ {valor:.2f} Depositados com sucesso!!!")
        extrato += f"Deposito: R$ {valor:.2f}\n"

    else: 
        print("Valor invalido, sao permitidos somente valores maiores que 0")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== Extrato =====")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("====================")

    return saldo, extrato

def criar_usuario(usuarios, lista_usuarios):

    print("===== Criar Usuario =====")

    cpf = input("Informe o CPF (somente numeros): ")
    
    if cpf in lista_usuarios:
        print("Ja existe um usuario cadastrado com esse CPF!!!")
        return
        
    else:
        lista_usuarios.append(cpf)
        nome = input("Informe o nome completo: ")
        data = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data, "cpf": cpf, "endereco": endereco})

        print("Usuario cadastrado com sucesso!!!")

def ver_usuarios(usuarios):

    print("===== Ver Usuarios =====")

    for usuario in usuarios:
        linha = f"""\
            Nome:{usuario['nome']}
            Data de Nascimento:{usuario['data_nascimento']}
            CPF:{usuario['cpf']}
            Endereco:{usuario['endereco']}
        """
        print("=" * 100)
        print(linha)

def criar_conta(nu_conta, agencia, lista_contas, lista_usuarios):

    print("===== Criar Conta =====")

    cpf = input("Informe o seu CPF (somente numeros): ")

    if cpf in lista_usuarios:
        lista_contas.append({"agencia": agencia, "numero_conta": nu_conta, "usuario": cpf})
        print("Conta criada com sucesso !!!")
        return lista_contas, lista_usuarios

    else:
        print("Usuario nao encontrado!!!")
        return

def ver_contas(lista_contas):

    print("===== Ver Usuarios =====")

    for conta in lista_contas:
        linha = f"""\
            Agencia:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']}
        """
        print("=" * 100)
        print(linha)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 3000
    limite = 500
    numero_saques = 1
    extrato = ""
    nu_conta = 1
    usuarios = []
    lista_usuarios = []
    lista_contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            
            valor = float(input("Informe o valor a ser sacado: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)

        elif opcao == "e":
            
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":

            criar_usuario(usuarios, lista_usuarios)

        elif opcao == "v":

            ver_usuarios(usuarios)
        
        elif opcao == "c":

            criar_conta(nu_conta, AGENCIA, lista_contas, lista_usuarios)
            nu_conta = len(lista_contas) + 1

        elif opcao == "l":

            ver_contas(lista_contas)

        elif opcao == "q":
            break

        else:
            print("Operacao invalida, por favor selecione novamente a operacao desejada.")

main()
