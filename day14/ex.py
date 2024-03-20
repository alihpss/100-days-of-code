def contador(inicio, fim, passo):
    aux = 0
    
    if passo < 0:
        passo *= -1
    
    if inicio > fim:
        aux = inicio
        while aux >= fim:
            print(aux)
            aux -= passo
        print("FIM")
    else:
        aux = inicio
        while aux <= fim:
            print(aux)
            aux += passo
        print("FIM")

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

help(print)