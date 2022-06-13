from time import sleep
print("Ordenar 4 palavras ")
sleep(1)

A=input("Insira a primeira palavra: ")
B=input("Insira a segundo palavra: ")
C=input("Insira a terceiro palavra: ")
D=input("Insira a quarto palavra: ")

pal = [A,B,C,D]
pal_ord = sorted(pal)

print(pal_ord)