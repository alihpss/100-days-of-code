estado = dict()
brasil = list()

for i in range(0, 3):
    estado['uf'] = str(input("Digite o nome do estado: "))
    estado['sigla'] = str(input("Digite o nome da UF: "))
    brasil.append(estado.copy())
    
for e in brasil:
    for key, value in e.items():
        print(f'o campo {key} tem valor {value}')
