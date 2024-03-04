from random import randint

player_option = str(input("insert paper, scissor or rock: "))

options = ["paper", "rock", "scissor"]

random_choice = randint(0, 2)

machine_choice = options[random_choice]

if player_option not in options:
    print("Erro, insira um valor valido.")
elif player_option == machine_choice:
    print("Empate, sua escolha foi {} e a da máquina foi {}".format(player_option, machine_choice))
elif player_option == "scissor" and machine_choice == "rock" or player_option == "rock" and machine_choice == "paper" or player_option == "paper" and machine_choice == "rock":
    print("Derrota, sua escolha foi {} e a da máquina foi {}".format(player_option, machine_choice))
else:
    print("Vitória, sua escolha foi {} e a da máquina foi {}".format(player_option, machine_choice))
    