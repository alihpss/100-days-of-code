from random import randint

n_maquina = randint(0, 5)

n_user = int(input("Digite um número de 0 a 5: "))

if (n_maquina == n_user):
    print("Você venceu! Seu número foi {} e o da máquina {}".format(n_user, n_maquina))
else:
    print("\033[4;30;31mVocê errou. Seu número foi {} e o da máquina {}".format(n_user, n_maquina))