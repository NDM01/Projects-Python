from time import sleep

valor = input('Insira o valor: ')

while not valor.isnumeric():
    
    print('Valor inválido!')

    valor = input('Insira o valor: ')




