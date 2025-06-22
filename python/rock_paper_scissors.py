import random

name = input("ingresa tu nombre:")
opciones = ("rock", "paper", "scissors")
game = True

while game:
    intento = input("que eleijes (rock - paper - scissors) :").lower()
    pc = random.choice(opciones)

    print(f"la maquina saco {pc}")

    if (intento == "rock" and pc == "scissors" or intento == "paper" and pc == "rock" or intento == "scissors" and pc == "paper"):
        print (f"ganastre {name}")
    elif (pc == "rock" and intento == "scissors" or pc == "paper" and intento == "rock" or pc == "scissors" and intento == "paper"):
        print (f"perdiste {name}")
    else:
        print (f"empate")
    
    new_try = int(input("quieres volver a jugar? "))

    if new_try == 0:
        game = False
