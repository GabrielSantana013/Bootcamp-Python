"""
=========================================
Herança em POO

Se a classe B é filha de A, ela tem todos os métodos de A.
Se a classe C é filha da classe B ela tem todos os métodos de B e de A,
pois é neta de A.

ex:

class A:
    pass
class B(A):
    pass
class C(B):
    pass

=========================================

"""

#=======================================
# HERANÇA SIMPLES
#=======================================


# class Veiculo:

#     def __init__(self, cor, placa, numero_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.numero_rodas = numero_rodas

#     def ligar_motor(self):
#         print("Motor Ligado! Vrum Vrum")
    
#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

# class Motocicleta(Veiculo):
#     pass

# class Carro(Veiculo):
#     pass

# class Caminhao(Veiculo):

#     def __init__(self, cor, placa, numero_rodas, carregado):
#         super().__init__(cor, placa, numero_rodas) #inicia o construtor do pai
#         self.carregado = carregado

#     def esta_carregado(self):
#         print(f'Sim' if self.carregado else 'Não')


# Xj = Motocicleta("preta", 1234, 2)
# celta = Carro("preto", 4321, 4)
# caminhao = Caminhao("branco", 2341, 8,True)
# print(Xj)
# print(celta)
# print(caminhao)


#=====================================
#  Herança Múltipla
#=====================================

# class Animal:
#     def __init__(self, nro_patas):
#         self.nro_patas = nro_patas

#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

# class Mamifero(Animal):
#     def __init__(self, cor_pelo, **kw):
#         self.cor_pelo = cor_pelo
#         super().__init__(**kw)

# class Ave(Animal):
#     def __init__(self, cor_bico, **kw):
#         self.cor_bico = cor_bico
#         super().__init__(**kw)

# class Cachorro(Mamifero):
#     pass

# class Gato(Mamifero):
#     pass

# class Leao(Mamifero):
#     pass

# class Ornitorrinco(Mamifero, Ave):
#     def __init__(self, cor_bico, cor_pelo, nro_patas):
#         super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)
#         #print(Ornitorrinco.__mro__) Mostra a ordem da resolução

# yumi = Gato(nro_patas = 4, cor_pelo = "tricolor")
# print (yumi)

# perry = Ornitorrinco(nro_patas = 4, cor_pelo = "Verde Água", cor_bico = "laranja")
# print(perry)

