"""
Criar uma função de cadastro de usuários e conta.

realizar as ações do menu através de funções

"""

def cadastrar_usuario(usuarios):
    cpf = input("Digite seu cpf: ")
    status = filtrar_usuarios(cpf, usuarios)

    if status:
        print("O cpf já está cadastrado!")
        return #retorna nada

    nome = input("Digite seu nome completo: ")
    data_de_nascimento = input("Digite sua data de nascimento: (dd/mm/aaaa): ")
    endereco = input("Digite o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

        

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    status = filtrar_usuarios(cpf, usuarios)

    if status:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta+1, "CPF": cpf}, (numero_conta+1)
    
    print("Cpf não encontrado, por favor realize o cadastro de usuário.")
    return False, None

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("Valor inválido, tente novamente.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, total_de_saques, VALOR_MAXIMO_SAQUE, LIMITE_SAQUE):

    if total_de_saques >= LIMITE_SAQUE:
        print("Você já atingiu o limite de operações diárias, tente novamente mais tarde.")
    else:
        valor = float(input("Digite o valor do saque: "))
        if valor <= saldo and valor > 0 and valor < VALOR_MAXIMO_SAQUE:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            total_de_saques +=1
        else:
            print("Valor inválido, tente novamente.")

    return saldo,extrato, total_de_saques

def exibir_extrato(saldo, /, *, extrato):
    titulo = " EXTRATO "
    final_extrato = "="
    print(titulo.center(50, '='))
    print(extrato)
    print(f"Saldo Total: R${saldo:.2f}")
    print('='*50)
    


#Funções Auxiliares:

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            return True
    return False

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Data de Nascimento: {usuario['data_de_nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print("="*50)

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}")
        print(f"CPF:{conta['CPF']}")
        print("=" * 50)




def main():

    menu = """
    [1] - Cadastrar Usuário
    [2] - Cadastrar Conta Bancária
    [3] - Depositar
    [4] - Sacar
    [5] - Consultar Extrato
    [0] - Sair
    """

    VALOR_MAXIMO_SAQUE = 500
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    total_de_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:

        entrada = input(menu)

        if entrada == "1":
            cadastrar_usuario(usuarios)
        elif entrada == "2":
           conta, numero_conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
           if conta:
               contas.append(conta)
        elif entrada == "3":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif entrada == "4":
            saldo, extrato, total_de_saques = sacar(saldo = saldo,
                valor = valor,
                extrato = extrato,
                total_de_saques=total_de_saques,
                VALOR_MAXIMO_SAQUE=VALOR_MAXIMO_SAQUE,
                LIMITE_SAQUE=LIMITE_SAQUE)
            

        elif entrada == "5":
            exibir_extrato(saldo, extrato = extrato)
        elif entrada == "6":
            listar_usuarios(usuarios)
        elif entrada == "7":
            listar_contas(contas)

        elif entrada == "0":
            print("Saíndo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()