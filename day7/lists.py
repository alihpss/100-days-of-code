my_list = ["elemento um", "elemento dois", "elemento tres"]

my_list.append("elemento quatro")
my_list.insert(0, "elemento zero")
my_list.pop(4)

for cont in range(4, 6):
    my_list.append(cont)

valores = list(range(4, 10))

#for index, element in enumerate(my_list):
#    print(f"Encontrei o {element} na posição {index}")

ligacao_lista = [2, 4, 5]
ligacao_da_lista = ligacao_lista

ligacao_da_lista[1] = 3


copia_lista = ligacao_lista[:]
copia_lista[1] = 9

print(f'Muda as duas listas, olha como funciona a ligação: {ligacao_da_lista} {ligacao_da_lista}')
print(f'Muda apenas uma lista, olha como funciona a copia: {ligacao_lista} {copia_lista}')
    