dados = dict()

dados2 = {'nome': 'Ali', 'idade': 23}
dados2['sexo'] = 'M'

del dados2['idade']

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

for k, value in filme.items():
    print(f'o k é {k} e o valor {value}')