#=============================================
# Variáveis de Classe e Variáveis de Instância
#=============================================

#Atributo de instância não influência nos outros atributos
#e é única por objeto


class Estudante:
    escola = "ETEC" #Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

aluno1 = Estudante("Gabriel", "0001")
aluno2 = Estudante("Pedro","0002")
mostrar_valores(aluno1, aluno2)
aluno2.matricula = "0004" #variável de instância
Estudante.escola = "Fatec" #variável de classse
mostrar_valores(aluno1, aluno2)
