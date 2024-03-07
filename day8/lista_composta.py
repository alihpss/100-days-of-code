pessoas = list()

pesados = list()
leves = list()

while True:
    nome = str(input("Insira o nome: "))
    peso = int(input("Insira o peso: "))
    
    pessoa = [nome, peso]
    pessoas.append(pessoa[:])
    
    opcao = str(input("Deseja continuar? [S/N]"))
    
    if opcao.lower() == 'n':
        break
    
    continue

for index, pessoa in enumerate(pessoas):
    if index == 0:
        pesados.append(pessoa)
    elif pessoa[1] > pessoas[index -1][1]:
        pesados.append(pessoa)
    elif pessoa[1] < pessoas[index -1][1]:
        leves.append(pessoa)
    elif pessoa[1] == pessoas[index -1][1]:
        if leves.__contains__(pessoas[index -1][1]):
            leves.append(pessoa)
        else:
            pesados.append(pessoa)
            
        
print(pesados)
print(leves)