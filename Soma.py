import os

x=input("Insira o primeiro número: ")

while not x.isnumeric():

    print("Valor inválido, insira um número!")

    x=input("Insira o primeiro número: ")

y=input("Insira o segundo número: ")

while not y.isnumeric():

    print("Valor inválido, insira um número!")

    y=input("Insira o primeiro número: ")


soma= int(x) + int(y)

print("\n" * os.get_terminal_size().lines)

print("O resultado da soma é " +str(soma))
