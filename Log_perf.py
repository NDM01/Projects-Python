from time import sleep
from datetime import date
import os
import getpass


nome = input("Insira o seu nome: ")

gmail = input("Insira o seu gmail: ")
ob = '@gmail.com'

while not ob in gmail:
    print("Gmail inválido!")
    gmail = input("Insira o seu gmail: ")

password = getpass.getpass("Insira a sua password: ")
psl = list()

teste = int(input("Insira o ano: "))

mes = int(input("Insira o mes: "))

dia = int(input("Insira o dia: "))

def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 

psl.append(password)

c = 0
b = []
for palavra in psl:
    linha = []
    for letra in palavra:
        linha.append(letra)
    b.append(linha)
c = len(linha)

print("Login efetuado")

print()

print("A redirecionar para o perfil...")

sleep(1)

print("\n" * os.get_terminal_size().lines)

print("PERFIL")

print('--------------------------')

print(f'Nome: {nome.title()}')

print(f'Gmail: {gmail}')

print('Idade: ',calculateAge(date(teste, mes, dia)), "anos")

print(f'Password: ', c * '*')

print('--------------------------')

