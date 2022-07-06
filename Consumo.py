cons = 0

litros = input('Insira a quantidade em litros que colocou: ')

while not litros.isnumeric():
    print('Valor inválido!')
    litros = input('Insira a quantidade em litros que colocou: ')

litros = int(litros)

km = input('Insira quantos kms fez: ')

while not km.isnumeric():
    print('Valor inválido!')
    km = input('Insira quantos kms fez: ')

km = int(km)

cons = km / litros

print(f"O consumo do carro é: {cons}km por litro")

