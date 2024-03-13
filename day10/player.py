
from time import sleep

player = dict()

player['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f"Quantas partidas {player['nome']} jogou? "))

lista_gols = list()

for i in range(0, partidas):
    partida_atual = int(input(f"Quantos gols {player['nome']} fez na partida { i + 1}? "))
    lista_gols.append(partida_atual)
    
player['gols'] = lista_gols[:]
player['total'] = sum(lista_gols)

print(f"O jogador {player['nome']} jogou {len(player['gols'])} partidas")
sleep(1)
for i in range(0, len(player['gols'])):
    print(f"Na partida {i + 1} o jogador marcou {player['gols'][i]} gols")
    sleep(1)
print(f"Foi um total de {player['total']} gols")

