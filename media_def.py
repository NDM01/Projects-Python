def med(vl1, vl2):
    media = (vl1 + vl2) / 2
    print(f'A média dos valores é: {media}')
    return

num1 = input('Insira o primeiro número a calcular: ')
num2 = input('Insira o segundo número a calcular: ')

while not num1.isnumeric() and not num2.isnumeric():
    print('Valor inválido\nInsira novamentos o números:\n')
    num1 = input('Insira o primeiro número a calcular: ')
    num2 = input('Insira o segundo número a calcular: ')

num1 = int(num1)
num2 = int(num2)

med(vl1 = num1, vl2= num2)
    