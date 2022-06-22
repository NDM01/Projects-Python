def tab(num):
    for x in range(10):
        print(f'{num} x {x + 1} = {num * (x + 1)}')
    return

n = input('Insira o número: ')

while not n.isnumeric():
    print('Caracter inválido\nInsira um número!')
    n = input('Insira o número: ')

n = int(n)

tab(num=n)