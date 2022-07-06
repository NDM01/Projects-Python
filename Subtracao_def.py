def func(n1,n2):
    sub = n1 - n2
    print(f'O valor da subtração é {sub}')
    return

nm1 = input('Insira o primeiro número: ')

while not nm1.isnumeric():
    print('Número inválido!')
    nm1 = input('Insira o primeiro número: ')

nm2 = input('Insira o segundo número: ')

while not nm2.isnumeric():
    print('Número inválido!')
    nm2 = input('Insira o segundo número: ')

nm1 = int(nm1)
nm2 = int(nm2)

func(n1= nm1,n2= nm2)