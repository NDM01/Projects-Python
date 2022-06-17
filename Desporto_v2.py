from time import sleep
import random
from turtle import circle

processo = random.randrange(123456789,987654321)

ftnum = random.randrange(1,60)

n = input("Insira o seu nome: ")

nome = n.title()

idade = int(input("Insira a sua idade: "))

if idade <= 6:
    print("Idade inválida!")
    print("A encerrar operação...")
    sleep(1)
    quit()
elif idade >= 90:
    print("Idade excede o limite permitido")
    print("A encerrar operação...")
    sleep(1)
    quit()

print("Modalidades disponíveis:")
print("----------------------------")
print("1- Karaté       2- Futebol")
print("3- Dança        4- Box")
print("5- Natação      6- Ciclismo")
print("7- Corrida      8- Escalada")
print("----------------------------")

resp = int(input("Insira a modalidade pretendida: "))

if resp == 1:
    print("Está inscrit@ no Karaté!")
    print("Já praticou alguma vez karaté federado?\n1 - Sim  2 - Não")
    karesp=int(input(""))
    if karesp == 1:
        grad =input("Insira a sua graduação: ")
        sleep(1)
        print("Gravado")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
elif resp == 2:
    if idade >= 35:
        escalao = 'Veteranos'
    elif idade >= 19 or idade <= 34:
        escalao = 'Seniores'
    elif idade == 17 or idade == 18:
        escalao = 'Juniores'
    elif idade == 16 or idade == 15:
        escalao = 'Juvenis'
    elif idade == 14 or idade == 13:
        escalao = 'Iniciados'
    elif idade == 12 or idade == 11:
        escalao = 'Infantis'
    elif idade == 10 or idade == 9:
        escalao = 'Minis'
    elif idade == 8 or idade == 7:
        escalao = 'Bambis'
    print("Está inscrit@ no Futebol!")
    print("O seu número é o %s" %(ftnum))
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
    print("Escalão: %s" %(escalao))
elif resp == 3:
    print("Está inscrit@ em Dança!")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
elif resp == 4:
    print("Está inscrit@ no Box!")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
elif resp == 5:
    print("Está inscrit@ em Natação!")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
elif resp == 6:
    print("Escolha uma das opções:\n1 - BTT\n2 - Downhill\n3 - Estrada" )
    cicles = int(input(""))
    while cicles> 3:
            print("Escolha uma das opções:\n1 - BTT\n2 - Downhill\n3 - Estrada" )
            cicles = int(input(""))
    if cicles == 1:
        print("Está inscrit@ em BTT!")
        print("A gerar número de processo...")
        sleep(1)
        print("Nome: %s" %(nome))
        print("Número de processo: %s" %(processo))
    elif cicles == 2:
        if idade <= 18:
            print("Idade inválida, tem que ter no mínimo 18 anos para poder praticar este desporto")
            print("A cancelar operação...")
            sleep(1)
            quit()
        print("Está inscrit@ em Downhill!")
        print("A gerar número de processo...")
        sleep(1)
        print("Nome: %s" %(nome))
        print("Número de processo: %s" %(processo))
    elif cicles == 3:
        print("Está inscrit@ em Ciclismo de Estrada")
        print("A gerar número de processo...")
        sleep(1)
        print("Nome: %s" %(nome))
        print("Número de processo: %s" %(processo))
elif resp == 7:
    print("Está inscrit@ em Corrida!")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
elif resp == 8:
    print("Está inscrit@ em Escalada")
    print("A gerar número de processo...")
    sleep(1)
    print("Nome: %s" %(nome))
    print("Número de processo: %s" %(processo))
else:
    print("Modalidade inválida!")
    print("A encerrar operação...")
    sleep(1)
    print("OPERAÇÃO CANCELADA")
    quit()
        


