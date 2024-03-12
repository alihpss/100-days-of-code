from random import randint
from time import sleep
from operator import itemgetter

results = dict()

for i in range(0,4):
    results[i+1] = randint(1, 6)
    print(f'o jogador {i + 1} tirou {results[i+1]} ')
    sleep(1)

ranking = list()

ranking = sorted(results.items(), key=itemgetter(1), reverse=True)
    
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: jogador {v[0]} com {v[1]} pontos')
    sleep(1)