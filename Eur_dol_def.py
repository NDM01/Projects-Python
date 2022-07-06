from time import sleep

def converter(eu):
    dollar = 0.96
    val = eu * dollar
    print(val)

    return

valor = input('Insira o valor em euros que pretende converter: ')

while not valor.isnumeric():
    print('Insira apenas números!')
    valor = input('Insira o valor em euros que pretende converter: ')

print('A converter...')
sleep(1)
valor = int(valor)
converter(eu= valor)