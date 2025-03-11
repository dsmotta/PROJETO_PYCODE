# Representação de Programação Orientada a Objetos

class Celular: # declaração do objeto e suas propriedades
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    # funcionalidades ou funções do objeto
    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha....')

    def despertador(self):
        print('Despertando...')

    def calular(self, v1, v2):
        return v1 + v2

# Criando uma instancia da classe acessando suas propriedades(atributos)
celular = Celular()
print(celular.marca)
print(celular.modelo)
print(celular.tem_camera)
print(celular.bateria)

# acessando as funcoes e funcionalidades
celular.despertador()
celular.fazer_ligacoes()
celular.jogar_cobrinha()
print(celular.calular(2, 4)) # imprimindo a classe instanciada chamando a função
# podemos criar uma variavel que contera a classe e a chamada da função e o retorno da funcao
calculado = celular.calular(3,7)
print(calculado) # imprimimos a variavel
