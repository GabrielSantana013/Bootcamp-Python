"""
Criar um sistema bancário com depósito, saque e extrato.

O usuário não poderá sacar mais de 500 reais por operação de saque
O usuário não poderá realizar mais de 3 saques por dia
"""

menu = """
[1] - Depositar
[2] - Sacar
[3] - Consultar Extrato
[0] - Sair
"""

saldo = 0
extrato = ""
VALOR_MAXIMO_SAQUE = 500
LIMITE_SAQUE = 3
total_de_Saques = 0

while True:

    entrada = input(menu)

    if entrada == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo +=valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Valor inválido, tente novamente.")

    elif entrada == "2":
        if total_de_Saques >= 3:
            print("Você já atingiu o limite de operações diárias, tente novamente mais tarde.")
        else:
            valor = float(input("Digite o valor do saque: "))
            if valor <= saldo and valor > 0 and valor < VALOR_MAXIMO_SAQUE:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                total_de_Saques +=1
            else:
                print("Valor inválido, tente novamente.")

    elif entrada == "3":
        titulo = " EXTRATO "
        final_extrato = "="
        print(titulo.center(50, '='))
        print(extrato)
        print(f"Saldo Total: R${saldo:.2f}")
        print('='*50)
    elif entrada == "0":
        print("Saíndo...")
        break
    else:
        print("Opção inválida, tente novamente.")