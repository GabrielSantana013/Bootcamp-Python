"""
========================================================
Introdução à Orientação a Objeto.
========================================================

joao tem uma bicicletaria e quer registrar as bicicleta
crie um programa onde joão informe:cor, modelo, ano e valor da bicicleta vendida.
uma bicicleta pode buzinar, parar e correr.
"""

# class Bicicleta:

#     def __init__(self, cor, modelo,ano,valor):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor

#     def buzinar(self):
#         print("trim trim")
    
#     def correr(self):
#         print("Bicicleta andando! Vrum vrum")

#     def parar(self):
#         print("Bicicleta parada.")

#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"
    

        

# caloi = Bicicleta("vermelha", "caloi", 2022, 800)
# caloi.buzinar()
# caloi.correr()
# caloi.parar()

# print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

# Bicicleta.buzinar(caloi) é igual a caloi.buzinar()

# print(caloi)


"""
====================================================
Construtores e Destrutores

Por hora:

construtor = __init__
destrutor = __del__

====================================================

"""

class Papagaio:

    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def cantar(self):
        print("*imitando a rhianna*")
    
    def dormir(self):
        if self.acordado:
            print("zzzzzzzz")
            self.acordado = False
        else:
            print("O papagaio já está dormindo!")
        
    def __del__(self):
        print("Removendo a instância da classe")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

paraguaio = Papagaio("paraguaio", "verde")
print(paraguaio)
paraguaio.cantar()
paraguaio.dormir()
paraguaio.dormir()

#del paraguaio Remove a instância doobjeto






