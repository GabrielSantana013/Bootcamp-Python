# def mensagem (nome):
#     print("executando funcao mensagem")
#     return f"oi {nome}"

# def mensagem_longa(nome):
#     print("executando funcao mensagem_longa")
#     return f"Olá tudo bem com você {nome}?"

# def executar(funcao, nome):
#     print("executando funcao executar")
#     return funcao(nome)

# print(executar(mensagem, "cleitom"))
# print(executar(mensagem_longa, "cleitom"))


# def principal():
#     print("executando a função principal")

#     def interna():
#         print("Executando a funcao interna")

#     def interna2():
#         print("Executando a funcao interna2")

#     interna2()
#     interna()

# principal()


# def calculadora(operacao):

#     def soma(a,b):
#         return a+b
    
#     def sub(a,b):
#         return a-b
    
#     def mult(a,b):
#         return a*b
    
#     def div(a,b):
#         return a/b

#     match operacao:
#         case '+':
#             return soma
#         case '-':
#             return sub
#         case '*':
#             return mult
#         case '/':
#             return div
        
# op = calculadora('*')
# print(op(4,8))

# # ou

# print(calculadora('+')(2,4))


#===================
# DECORADORES

# def meu_decorador(funcao):
#     def envelope():
#         print("Algo antes de executar")
#         funcao()
#         print("Algo depois de executar")
    
#     return envelope

# @meu_decorador
# def ola_mundo():
#     print("Olá mundo!")

# ola_mundo()

"""   
*ARGS e **KWARGS

*ARGS é tupla
**Kwargs é lista

"""

# def duplicar(func):
#     def envelope(*args, **kwargs):
#         print("Algo Antes")
#         resultado = func(*args, **kwargs)
#         print("Algo Depois")
#         return resultado

#     return envelope

# @duplicar
# def aprender(tecnologia):
#     print(f"Estou aprendendo {tecnologia}")
#     return tecnologia.upper()

# resultado = aprender("python")
# print(resultado)

#======================================

# import functools

# def duplicar(func):
#     @functools.wraps(func)
#     def envelope(*args, **kwargs):
#         func(*args, **kwargs)
    
#     return envelope

# @duplicar
# def aprender(tecnologia):
#     print(f"Estou aprendendo {tecnologia}")

# print(aprender.__name__)



#==========================================
# Decoradores e Iteradores
#==========================================

#Iteradores

# class MeuIterator:

#     def __init__(self, lista: list[int]):
#         self.numeros = lista
#         self.contador = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             numero = self.numeros[self.contador]
#             self.contador += 1
#             return numero *2
#         except IndexError:
#             raise StopIteration

# for i in MeuIterator(lista=[1, 2, 3]):
#     print(i)


#============================
# Geradores
#============================

# def meu_gerador(numeros:list[int]):
#     for numero in numeros:
#         yield numero* 2

# for i in meu_gerador(numeros = [1,2,3,4,5]):
#     print(i)
