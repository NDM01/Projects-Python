import random
from time import sleep

print("Bem-Vindo ao gerador de passwords")

char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£§€{[]*`^ª~º+´.-,/965874321"#$%&/()=?!|'

number=int(input("Quantidade de passwords a gerar: "))

length=int(input("Tamanho da password: "))

print("A gerar passwords:\n ")
sleep(2)

for pwd in range(number):
    passwords = ''
    for c in range(length):
       passwords += random.choice(char)
    print(passwords)
    print("")