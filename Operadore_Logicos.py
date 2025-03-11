# Operadores == AND OR !=

nome = 'Douglas'
idade = 40
peso = 90

# Testa a igualde retorna verdaeiro ou falso
if idade == 45: 
    print('CORRETO')
else:
    print('INCORRETO')

# testa o inverso ou seja se o valor testado for igual o retorno e falso 
if nome != 'Douglas': 
    print('SIM')
else:
    print('NAO')

# as duas condições precisam ser verdadeiras 
if idade == 40 and nome == 'Douglas': 
    print('TRUE')
else:
    print('FALSE')

# somente uma das condições precisam ser verdadeiras 
if idade == 45 or nome == 'Douglas': 
    print('TRUE')
else:
    print('FALSE')

# operadores compostos
if (nome == 'Marcos' or idade == 25) and peso != 90:
    print('TRUE')
else:
    print('FALSE')