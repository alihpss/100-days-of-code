from time import sleep

pessoas = list()
mulheres = list()
acima_media = list()

while True:
    lista_pessoas = dict()
    
    lista_pessoas['nome'] = str(input("Digite o nome: "))
    lista_pessoas['sexo'] = str(input("Digite o sexo: "))
    lista_pessoas['idade'] = int(input("Digite a idade: "))
    
    pessoas.append(lista_pessoas)
    
    res = str(input("Quer continuar? [S/N]"))
    
    if res == 'n':
        break
    
media = 0
auxiliar_media = 0

for i in range(0, len(pessoas)):
    calcula_media = 0
    
    if pessoas[i]['sexo'] == 'f':
        mulheres.append( pessoas[i]['nome'])
    
    media += pessoas[i]['idade']
    auxiliar_media += 1
    print(f'mediaaaaa {media} {auxiliar_media}')
    
    
media = media / auxiliar_media

for k, value in enumerate(pessoas):
    if value['idade'] > media:
        acima_media.append(pessoas[k])
    
print(f"Ao todo temos {len(pessoas)} cadastradas")
print(f"A média de idade é {media}")
print(f"A mulheres da lista são {mulheres}")
print(f"As pessoas com idade acima da média são {acima_media}")
