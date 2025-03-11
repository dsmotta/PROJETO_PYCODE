# Exemplo não usando Compreensão de Listas

numeros = [1,2,3,4,5]
numeros_dobrados = list()

for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros)
print(numeros_dobrados)

# Exemplo usando compreensão de lista [expr for item in lista]
numeros_dobrados = [num * 2 for num in numeros]
print(numeros_dobrados)

# Usando funcao e compreensão de listas
def dobro(numero):
    return numero*2

numeros_dobrados = [dobro(numero) for numero in numeros]
print(numeros_dobrados)

# Exemplo com string de nomes, compreensão de listas com condicional
nomes = ['Ana', 'Paulo', 'Maria', 'Amanda']

nomes_maisculo = [nome.upper() for nome in nomes if nome[0] == 'A']
print(nomes_maisculo)