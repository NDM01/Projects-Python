
from unicodedata import numeric

Soma = 0

def lista():

    print()

    print('Lista')

    print('--------------')

    print('1 - Café')

    print('2 - Croissant')

    print('3 - Sumo')

    print('4 - Pão')

    print('5 - Donnut')

    print('--------------')

lista()

print()

while True:

    produto = input('Insira o número do produto: ')

    if produto == '1':
        
        qtd = input('Insira a quantidade: ')

        while not qtd.isnumeric():
            
            print('Quantidade inválida!')

            qtd = input('Insira a quantidade: ')
        
        qtd = int(qtd)

        c = 0.65 * qtd

        Soma = Soma + c
  
    elif produto == '2':
                
        qtd2 = input('Insira a quantidade: ')

        while not qtd2.isnumeric():

            print('Quantidade inválida!')

            qtd2 = input('Insira a quantidade: ')

        qtd2 = int(qtd2)

        cr = 0.80 * qtd2

        Soma = Soma + cr
    
    elif produto == '3':

        qtd3 = input('Insira a quantidade: ')

        while not qtd3.isnumeric():

            print('Quantidade inválida!')

            qtd3 = input('Insira a quantidade: ')
        
        qtd3 = int(qtd3)

        s = 1 * qtd3

        Soma = Soma + s
    
    elif produto == '4':
        
        qtd4 = input('Insira a quantidade: ')

        while not qtd4.isnumeric():
            
            print('Quantidade inválida!')

            qtd4 = input('Insira a quantidade: ')
        
        qtd4 = int(qtd4)

        p = 0.10 * qtd4

        Soma = Soma + p
    
    elif produto == '5':
        
        qtd5 = input('Insira a quantidade: ')

        while not qtd5.isnumeric():

            print('Quantidade inválida!')

            qtd5 = input('Insira a quantidade: ')

        qtd5 = int(qtd5)

        d = 0.35 * qtd5

    else:
        print('Produto inválido!')

        print('A canceçaar operação')


    



                
