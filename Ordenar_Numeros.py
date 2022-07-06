from time import sleep
print("Ordenar 4 números ")
sleep(1)

A=int(input("Insira o primeiro número: "))
B=int(input("Insira o segundo número: "))
C=int(input("Insira o terceiro número: "))
D=int(input("Insira o quarto número: "))

num = [A,B,C,D]
num_ord = sorted(num)

print(num_ord)