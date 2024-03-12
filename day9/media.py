aluno = dict()

aluno['nome'] = str(input("Insira seu nome: "))
aluno['media'] = float(input(f"Insira a media de {aluno['nome']}: "))

if aluno['media'] >= 5:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
    
print(aluno)