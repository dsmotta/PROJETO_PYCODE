meu_dicio = {} #criando variavel que vai conter o dicionario na memoria 

meu_dicio = {'nome':'Douglas', 'idade':'40', 'profissao':'Developer'}

meu_dicio['nome'] # acessando valores 

meu_dicio.get('profissao') # outra forma de acessar os valores do dicionari usando o get() e passando a chave

meu_dicio.pop('idade') # remove o elemento 

meu_dicio.keys() # lista todas as chaves

meu_dicio.values() # mostra todos os valores

meu_dicio.clear() # deleta tudo que esta no dicionario

# Exemplos
pessoa = {
    'nome':'Felipe',
    'idade':25,
    'profissão':'Developer',
    'interesses':['python', 'Programacao', 'Banco Dados'],
    'pet':{
        'nome':'Mel',
        'idade':2,
        'peso':'2'
    }
}

#buscando no dicionario
print(pessoa)
print(pessoa['nome']) # acessando valores dos dicionarios sem uso de funções
print(pessoa.get('nome')) # acessando valores dos dicionarios usando get

# buscando na lista que esta dentro do dicionario
print(pessoa.get('interesses')) # acessa a chave que possui uma lista mostra todos os valores da lista
print(pessoa.get('interesses')[1]) # acessa a chave que possui uma lista e mostra o valor de acordo com o indice
print(pessoa['interesses']) # acessa valores da lista sem o uso da funcao get()
print(pessoa['interesses'][2]) # acessa valores da lista sem o uso do get() apenas usando o indice

# buscando em um dicionario dentro de outro dicionario
print(pessoa.get('pet').get('nome')) # usando o get()
print(pessoa['pet']['peso']) # sem uso de função get()

#adcionando valores no dicionario
pessoa['ano_nasc'] = 1997 # criando a chave e passando valor
pessoa['cores_favoritas'] = ['Azul', 'Verde', 'Laranja'] # adcionand uma chave e uma lista de valores
# adcionando uma nova chave ao dicionario e esta chave tambem é um dicionario
pessoa['mae'] = {   
    'nome':'Maria',
    'idade':58
}

print(pessoa)
