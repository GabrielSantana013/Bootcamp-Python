#=============================================
# Variáveis de Classe e Variáveis de Instância
#=============================================

#Atributo de instância não influência nos outros atributos
#e é única por objeto


# class Estudante:
#     escola = "ETEC" #Atributo de classe

#     def __init__(self, nome, matricula):
#         self.nome = nome
#         self.matricula = matricula
    
#     def __str__(self):
#         return f"{self.nome} - {self.matricula} - {self.escola}"
    
# def mostrar_valores(*objs):
#     for obj in objs:
#         print(obj)
    

# aluno1 = Estudante("Gabriel", "0001")
# aluno2 = Estudante("Pedro","0002")
# mostrar_valores(aluno1, aluno2)
# aluno2.matricula = "0004" #variável de instância
# Estudante.escola = "Fatec" #variável de classse
# mostrar_valores(aluno1, aluno2)



#=====================================================
# Métodos de classe e Métodos estáticos
#=====================================================

# class Pessoa:
#     def __init__(self, nome = None, idade = None):
#         self.nome = nome
#         self.idade = idade

#     @classmethod
#     def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
#         idade = 2024 - ano
#         return cls(nome, idade)
    
#     @staticmethod
#     def e_maior_idade(idade):
#         return idade >=18

# # p1 = Pessoa("gabriel", 22)
# # print(p1.nome, p1.idade)

# p = Pessoa.criar_apartir_data_nascimento(2004, 11, 14, "Gabriel")
# print(p.nome, p.idade)
# print(Pessoa.e_maior_idade(18))
# print(Pessoa.e_maior_idade(10))



#=====================================================
# Classes Abstratas
#=====================================================

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv")

    def desligar(self):
        print("Desligando a tv")
    
    @property
    def marca(self):
        return "Samsung"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar")

    

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()



