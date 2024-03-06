lista = list()

for i in range(0, 5):
    valor = int(input("Digite um número: "))
    if len(lista) == 0:
        lista.append(valor)
    else:
        for index, value in enumerate(lista):
            if valor < value:
                lista.insert(index, valor)
                break
            elif valor > lista[-1]: 
                lista.insert(len(lista), valor)
                break
            
print(lista)