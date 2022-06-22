lista = list()

palavra = input("Insira a palavra: ")

lista.append(palavra)

b = []
for pal in lista:
    linha = []
    for letra in pal:
        linha.append(letra)
    b.append(linha)
print(b)