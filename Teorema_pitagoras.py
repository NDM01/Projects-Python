cat1 = input('Insira o valor do cateto 1:')

while not cat1.isnumeric():
    print('Insira um valor válido!')
    cat1 = input('Insira o valor do cateto 1:')

cat2 = input('Insira o valor do cateto 2:')

while not cat2.isnumeric():
    print('Insira um valor válido!')
    cat2 = input('Insira o valor do cateto 2:')

cat1 = int(cat1)
cat2 = int(cat2)

hip = (cat1 * cat1) + (cat2 * cat2)

print(f'O valor da hipotenusa é {hip}')