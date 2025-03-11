# funcao com parametros e retorno
def somar(a, b):
    resultado = a + b
    return resultado

print(somar(2, 5)) # chama a funcão passando os parametros da soma e ja imprime na tela

# funcao sem parametro de entrada e retorno ela somente executa as instruções
def envia_email():
    email = 'pycode@gmail.com'
    senha = '12345'
    return 'Email enviado!'

pessoas = ['Marcos', 'Felipe', 'Carla']

for pessoa in pessoas:
    envia_email() # somente chama e executa a função nao exite retorno
    email_enviado = envia_email() # chamando a função e atribuindo seu retorno dentro da variavel
    print(email_enviado)