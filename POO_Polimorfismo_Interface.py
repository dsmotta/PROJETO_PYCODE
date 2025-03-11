class Forma():
    def area(self):
        pass # significa uma funcao vazia

class Quadrado(Forma):

    def __init__(self, lado): # metodo construtor que recebe o parametro quando eu instanciar a função
        self.lado = lado

    def area(self): # funcao que vai usar o parametro passado no construtor
        return self.lado ** 2 # retorno da funcao com os calculos setando o parametro do construtor
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    
quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

quadrado2 = Quadrado(7)
area_quadrado2 = quadrado2.area()
print(area_quadrado2)


circulo = Circulo(5)
area_circulo = circulo.area()
print(area_circulo)