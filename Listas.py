# criando listas e seus metodos

carros = list()
carros.append('fusca') # insere valor na lista sempre na ultima posição
carros.append('Marea')
carros.append(10)
carros.insert(0, 'Corcel') # insere valores na lista de acordo com a posição do indice passado
print(carros[0]) # acessa valor da lista pelo indice

# removendo valores da lista
print(carros.pop()) # remove o ultimo elemento da lista
del carros[0] # elimina valores usando o indice
carros.remove('Marea') # remove pelo valor da lista
carros.append('fusca')
print(carros.count('fusca')) # conta a quantidade de incidencias do valor que foi passado
carros.pop()
carros.append('kombi')
print(carros)
carros.reverse() # jinverte os valores da lista

print(carros)

numeros = [2,5,8,1,7,0]
print(numeros)
numeros.sort() # coloca em ordem os valores da lista
print(numeros)


