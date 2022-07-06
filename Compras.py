from time import sleep

con = True

lst = list()

print('Lista de compras:')

print()

print('Selecione a tecla 2 para gerar a lista!')

while con == True:
    comp = input('Insira o nome do produto que pretende comprar para adicionar a lista: ')
    
    lst.append(comp)

    if comp == '2':

        print('A gerar lista...')

        break

sleep(1)

print('Lista:')

lst.pop(-1) # Remove o número que estiver entre ()

print()

for palavra in lst:
    print(palavra)    

print()