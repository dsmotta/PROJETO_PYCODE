# Conceito de Herança 

class Carro:
    numero_rodas = 4
    qtde_passageiros = 5

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinar...')

carro = Carro()
carro.acelerar()

class Uno(Carro): # Criando a classe Uno herdando (herança) tudo da classe Carro
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1994

uno = Uno()
uno.acelerar()
print(uno.numero_rodas)
