""" Polimorfismo - classes diferentes que herdam da mesma classe possam term 
metodos propriedades funcoes com mesmo nome mas executam coisas diferentes
"""
class Animal: # Criando a classe generica

    def emitir_som(self): # criando uma funcionalidade qualquer
        (print('Qualqer som ....'))

class Cachorro(Animal): # crianco uma clesse especifica com herança da classe Animal

    def emitir_som(self): # POLIMORFISMO - onde esta funçã e herdada de Animal porém ela executa algo diferente
        print('Au Au!')

class Gato(Animal):

    def emitir_som(self):# POLIMORFISMO - onde esta funçã e herdada de Animal porém ela executa algo diferente
        print('Miau!')

cachorro = Cachorro() # instanciando classe dentro de uma variavel
cachorro.emitir_som() # pela variavel chamando os a função

gato = Gato() # instanciando classe dentro de uma variavel
gato.emitir_som() # pela variavel chamando os a função
