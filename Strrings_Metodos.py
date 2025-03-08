texto = 'AULA PYCODEBR' # String um conjunto de caracteres onde o espaço vazio também é contado
print(texto)

print(texto[0]) # imprime o caracter de indice 0 na string
print(texto[0:4]) # imprime o caracter de indice 0 ate 4
print(texto[5:]) # imprime os caracteres da posição de indice 5 até o final da string
print(texto[:4]) # imprime os caracteres da posição de indice 0 até 3
print(texto[-4]) # imprime o indice -4 da lista do final para o começo 

print(len(texto)) # mosta o tamanho da string ou seja a quantidade de caracteres inclousive os espaços
print(texto.count('A')) # conta quantas incidencias da letra A existem na string
print(texto.count('P', 5, 11)) # incidencia da letra pe na string do indice 5 até o 11
print(texto.count('AULA')) # imprime a recorrencia dapalavra AULA ou seja quantas existem na string
print(texto.find('AULA')) # procura no trecho a posição em que ele começa
print(texto.find('PYCODEBR'))
print(texto.lower()) # coloca todos os caracteres da string em minusculo
print(texto.upper()) # coloca todos os caracteres da string em maiúsculo
txt = ('estudando em python')
print(txt.capitalize()) # coloca em maiusculo somente a primeira letra string
print(txt.title()) # coloca o primeiro caractere em maiuscula e todas as outros primeiros caracteres depois do espaço
print(texto.split()) # divite a string de acordo com o espaços eliminando-os em uma lista
lista = txt.split() 
print('-'.join(lista)) # quebra a string em uma lista de acordo com espaços depois e usa o join para unir porem e definido pelo joi
texto = '   AULA PYCODEBR    '
print(texto.strip()) # elimina espaços em branco antes e depois dos caracteres
print(texto.rstrip()) # elimina os espaços em branco somente na direita dos caracteres da string
print(texto.lstrip()) # elimina os espaços em branco somente na esquerda dos caracteres da string