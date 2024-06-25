from abc import ABC, abstractclassmethod, abstractmethod
from datetime import datetime, timezone, timedelta

class Conta:

    def __init__(self, numero:int, cliente:str):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self.historico = Historico()
    
    @property
    def get_saldo(self):
        return self._saldo
    
    def sacar(self, valor:float) -> bool:
        saldo = self._saldo
        status = saldo>valor

        if status:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("O valor informado é maior do que o valor em conta.")
            return False

    def depositar(self, valor:float) -> bool:
        if valor>0:
            self._saldo += valor
            return True
        else:
            print("Valor inválido digitado.")
            return False
        
    @classmethod 
    def nova_conta(cls, cliente, numero: int):
        return cls(numero, cliente)
    
class Transacao(ABC):

    @abstractmethod   
    def registrar(self, conta):
        pass

class Cliente:

    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        if conta.historico.transacoes_do_dia() >=11:
            print("Você já excedeu o limite de Transações diárias.")
            return
        transacao.registrar(conta)
            

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        
        status = conta.depositar(self._valor)

        if status:
            conta.historico.adicionar_transacao(self)
    
class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        status = conta.sacar(self._valor)

        if status:
            conta.historico.adicionar_transacao(self)

class Historico():

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao._valor,
                "data": datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
            }
        )
    
    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes_diarias = 0
        mascara_En = "%d/%m/%Y - %H:%M:%S"

        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao['data'], mascara_En).date()

            if data_transacao == data_atual:
                transacoes_diarias +=1

        return transacoes_diarias


class PessoaFisica(Cliente):

    def __init__(self, endereco, cpf: str, nome : str, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class ContaCorrente(Conta):

    def __init__(self, numero: int, cliente: str, limite: float, LIMITE_SAQUES: int):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = LIMITE_SAQUES
        self.saques_realizados = 0

    @property
    def get_limite(self):
        return self._limite
    
    @property
    def get_limite_saque(self):
        return self._limite_saques
    
    @property
    def get_saques_realizados(self):
        return self.saques_realizados
    
    def pode_sacar(self):
        if self.saques_realizados >= self._limite_saques:
            return False
        return True
    
    def registrar_saque(self):
        self.saques_realizados +=1

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

#=============================================================

def cadastrar_usuario(clientes):
    cpf = input("Digite seu cpf: ")
    status = filtrar_usuarios(cpf, clientes)

    if status:
        print("O cpf já está cadastrado!")
        return #retorna nada

    nome = input("Digite seu nome completo: ")
    data_de_nascimento = input("Digite sua data de nascimento: (dd/mm/aaaa): ")
    endereco = input("Digite o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(endereco, cpf, nome, data_de_nascimento)
    clientes.append(cliente)
    
    print("Cliente cadastrado com Sucesso!!")

def cadastrar_conta(numero_conta, clientes, contas):
    cpf = input("Digite seu cpf: ")
    cliente = filtrar_usuarios(cpf, clientes)

    if  not cliente:
        print("Cpf não encontrado, por favor realize o cadastro de usuário.")
        return False
    
    limite = float(input("Qual o limite de valor máximo de saque para a sua conta? (em R$)"))
    LIMITE_SAQUE = 10

    conta = ContaCorrente.nova_conta(numero= numero_conta, cliente = cliente, limite = limite, limite_saques = LIMITE_SAQUE)
    contas.append(conta)
    cliente._contas.append(conta)

    print("Conta criada com sucesso!")


def depositar(clientes):

    cpf = input("Digite o seu cpf: ")
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print("Cpf não encontrado, realize o cadastro primeiro.")
        return False

    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        transacao = Deposito(valor)
        conta = procura_conta(cliente)
        if not conta:
            print("O cliente ainda não possui conta. Crie uma primeiro!")
            return False
        else:
            cliente.realizar_transacao(conta, transacao)
            print("Depósito realizado com sucesso! ")
            return True
    else:
        print("Valor inválido, tente novamente.")
        

def sacar(clientes):
    cpf = input("Digite seu cpf: ")
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print("Cpf não encontrado, realize o cadastro primeiro.")
        return

    conta = procura_conta(cliente)

    if not conta:
        print("O cliente não possui conta, cadastre primeiro.")
        return

    if not conta.pode_sacar:
        print("Limite diário de saques já foi excedido.")
        return

    limite_conta = int(conta.get_limite_saque)
    saques_realizados = int(conta.get_saques_realizados)


    valor = float(input(f"Digite o valor que deseja sacar (Valor em conta: R${conta.get_saldo}): "))
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)
    conta.registrar_saque()
    

def exibir_extrato(clientes):
    #TODO: Alterar para exibir: data-operacao-valor
    cpf = input("Digite seu cpf: ")
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print("Cpf não encontrado, realize cadastro primeiro.")
        return
    
    conta = procura_conta(cliente)

    if not conta:
        print("Conta não encontrada, crie uma conta primeiro.")
        return

    transacoes = conta.historico.transacoes
    extrato = ""
    titulo = " EXTRATO "
    print(titulo.center(50, '='))

    if not transacoes:
        extrato = "Nenhuma movimentação encontrada"
    else:
        for transacao in transacoes:
            operacao = transacao['tipo'].ljust(8)
            extrato += f"\n{transacao['data']}\t{operacao} \tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo: \t\t\t\tR${conta._saldo:.2f}")
    print("=" *50)
        
    


#Funções Auxiliares:

def filtrar_usuarios(cpf, clientes):
    for cliente in clientes:
        if cpf == cliente._cpf:
            return cliente
    return False

def procura_conta(cliente):
    if not cliente._contas:
        print("O cliente não possui conta.")
        return 
    return cliente._contas[0]

# def listar_usuarios(usuarios):
#     for usuario in usuarios:
#         print(f"Nome: {usuario['nome']}")
#         print(f"CPF: {usuario['cpf']}")
#         print(f"Data de Nascimento: {usuario['data_de_nascimento']}")
#         print(f"Endereço: {usuario['endereco']}")
#         print("="*50)

# def listar_contas(contas):
#     for conta in contas:
#         print(f"Agência: {conta['agencia']}")
#         print(f"Número da conta: {conta['numero_conta']}")
#         print(f"CPF:{conta['CPF']}")
#         print("=" * 50)


def main():

    menu = """
    [1] - Cadastrar Usuário
    [2] - Cadastrar Conta Bancária
    [3] - Depositar
    [4] - Sacar
    [5] - Consultar Extrato
    [0] - Sair
    """

    clientes = []
    contas = []

    while True:

        entrada = input(menu)

        if entrada == "1":
           cadastrar_usuario(clientes) 
        elif entrada == "2":
           numero_conta = len(contas)+1
           cadastrar_conta(numero_conta, clientes, contas)
        elif entrada == "3":
            depositar(clientes)
        elif entrada == "4":
            sacar(clientes)
        elif entrada == "5":
            exibir_extrato(clientes)
        #elif entrada == "6":
        #     listar_usuarios(usuarios)
        # elif entrada == "7":
        #     listar_contas(contas)

        elif entrada == "0":
            print("Saíndo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()

