valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor de seu salario: "))
anos_pgto = int(input("Digite em quantos anos quer pagar: "))

valor_prestacao = valor_casa / (anos_pgto * 12)

if(valor_prestacao > salario * 0.3):
    print("Prestacao {} por mes para o salario {} negada".format(valor_prestacao, salario))
else:
    print("Pode aceitar")

