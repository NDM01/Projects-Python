from ast import While


print('Menu disponíveis: ')
print('1 -- Pizza 2,50€')
print('2 -- Doublecheese 3,50€')
print('3 -- Batata 1,50€')
print('4 -- Sumo 1€')

while True:
    sel = input('Insira o produto que pretende: ')
    if not sel.isnumeric:
        print('Produto inválido!')
        print('Insira o número de um produto válido!')
        # return

#  print()