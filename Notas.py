from ast import Num

media = 0
soma = 0
al = list()
num = list()
n = list()

num_alunos = input('Insira o número de alunos: ')

while not num_alunos.isnumeric():
    
    print("Só são aceites números!\nInsira um número válido!")
    num_alunos = input('Insira o número de alunos: ')

num_alunos = int(num_alunos)

for x in range(num_alunos):
    
    aluno = input(f'Insira o nome do {x + 1} aluno: ')
    nota = input('Insira a nota: ')

    while not nota.isnumeric():

        print("Valor inválido, insira um valor válido!")
        nota = input('Insira a nota do aluno: ')
    
    nota = int(nota)
    while nota > 20:
     print("Valor inválido, insira um valor válido!")
     nota = int(input('Insira a nota do aluno: '))
    
    al.append(aluno)
     
    num.append(x)

    n.append(nota)

    soma += nota

media = soma / num_alunos

print()
print('Notas:')

for y in range(num_alunos):
 print(f'{al[y]} : {n[y]} valores')

print(f'A média das notas é {media}')

notmax=max(n)

notmin=min(n)

print(f'A nota mais alta foi {notmax}\nA nota mais baixa foi {notmin}')