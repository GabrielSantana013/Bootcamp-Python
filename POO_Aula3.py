#====================================
#Encapsulamento
#====================================


# class Conta:
#     def __init__(self, saldo, nro_agencia):
#         self._saldo = saldo #se tem o _ na frente é privada (conveção)
#         self.nro_agencia = nro_agencia

#     def sacar(self, valor):
#         self._saldo -= valor

#     def depositar(self, valor):
#         self._saldo += valor

#     #método criado para msotrar o saldo corretamente
#     def mostrar_saldo(self):
#         return self._saldo

# conta = Conta(1000, "0001")
# conta.depositar(100)
# print(conta.mostrar_saldo())
# conta.sacar(500)
# print(conta.mostrar_saldo())
# print(conta.nro_agencia)
# print(conta.mostrar_saldo())

#==================================================
#Property
#==================================================

# class Foo:

#     def __init__(self, x = None):
#         self._x = x

#     @property
#     def x(self):
#         return self._x or 0
#     @x.setter
#     def x(self, valor):
#         self._x += valor
    
#     @x.deleter
#     def x(self):
#         self._x = 0   

# foo = Foo(10)
# print(foo.x)
# foo.x = 10
# print(foo.x)
# del foo.x
# print(foo.x)


# class Pessoa:
#     def __init__(self, nome, ano_nascimento,):
#         self._nome = nome
#         self._ano_nascimento = ano_nascimento
       
#     @property
#     def idade(self):
#         _ano_atual = 2024
#         return _ano_atual - self._ano_nascimento
       
# gabriel = Pessoa("Gabriel", 2004)
# print(f"Nome : {gabriel._nome} \t Idade: {gabriel.idade}")