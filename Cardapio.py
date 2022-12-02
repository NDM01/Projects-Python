from ast import Return, While
from time import sleep

l = True

print('--------------------------')
print('Menu disponíveis: ')
print('1 -- Pizza 2,50€')
print('2 -- Doublecheese 3,50€')
print('3 -- Batata 1,50€')
print('4 -- Sumo 1€')
print('--------------------------')

while l==True:
    sel = input('Insira o produto que pretende: ')
    if not sel.isnumeric():
        print('Produto inválido!')
        print('Insira o número de um produto válido!')
        # return
    sel=int(sel)    
    if sel > 4:
        print('Produto inválido!')
        print('Insira o número de um produto válido!')
        Return
    
    # else:

    #     print('teste')
    #     l = False

        
    

print()