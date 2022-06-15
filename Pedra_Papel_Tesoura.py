import random

resp = input("R - Pedra\nT - Tesoura\nP - Papel\nInsira a sua opção: ")
computador = random.choice(['R','T','P'])

if resp == 'R' and computador == 'T':
    print("Ganhou!")
elif resp == 'T' and computador == 'P':
    print("Ganhou!")
elif resp == 'P' and computador == 'R':
    print("Ganhou!")
elif resp == 'T' and computador == 'R':
    print("Perdeu!")
elif resp == 'P' and computador == 'T':
    print("Perdeu!")
elif resp == 'R' and computador == 'P':
    print("Perdeu!")
elif resp == 'R' and computador == 'R':
    print("Empate!")
elif resp == 'T' and computador == 'T':
    print("Empate!")
elif resp == 'P' and computador == 'P':
    print("Empate!")

