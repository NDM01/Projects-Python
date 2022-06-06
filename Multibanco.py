import random
import getpass
from time import sleep
m= random.randrange(1,5000)
print("Insira o cartão")
sleep(1.3)
password=getpass.getpass("PIN:")
if password.isnumeric():
    print("PIN Correto")
else:
    print("PIN INVÁLIDO")
    print("A CANCELAR OPERAÇÃO...")
    sleep(1)
    quit()
sleep(1)
def CriarTabela():
    print("--------------------------------------------")
    print("1- Levantamentos         2- Consultas")
    print("3- Serviços MBNET        4- Transferências")
    print("5- Pagamentos e          6- Depósitos e\nOutros Serviços          Outras Operações")
    print("--------------------------------------------")
CriarTabela()
block=int(0)
sel=int(input("Selecione uma opção: "))
while sel>=7 or sel==0:
     sel=int(input("Selecione uma opção: "))
     block=block+1
     if block>3:
         print("OPERAÇÃO ANULADA")
         sleep(1)
         quit()
if sel==1:
    lev=int(input("Insira o montante a levantar: "))
    if lev>m:
        print("A quantia que está a tentar levantar é superior ao saldo disponível na conta\nA CANCELAR OPERAÇÃO")
        sleep(1)
        quit()
    m=m-lev
    print("Retire o seu dinheiro")
    print("Deseja consultar o saldo?\n1- SIM 2- NAO")
    c=int(input())
    if c==1:
        print("Saldo disponível: %s" %(m))
        fl=input("Selecione ENTER para fechar operação ")
        if fl==str:
          sleep(0.5)
          quit()
    elif c==2:
        print("A fechar operação")
        sleep(0.5)
        quit()
elif sel==2:
    print("Saldo disponível: %s" %(m))
    print("Prentende levantar dinheiro?\n1- Sim 2- Não ")
    lvt=int(input())
    if lvt==1:
        levantar=int(input("Insira o montante a levantar: "))
        if levantar>m:
            print("A quantia que está a tentar levantar é superior ao saldo disponível na conta\nA CANCELAR OPERAÇÃO")
            sleep(2)
            quit()
        print("Retire o seu dinheiro")
        sleep(2)
        quit()
    elif lvt==2:
        print("A fechar operação")
        sleep(0.5)
        quit()
elif sel==3:
      mb=int(input("Limite máximo de carregamento: 20,00€\nLimite mínimo de carregamento: 10,00€\nInsira o montante a carregar no cartão MBNet "))
      if mb>20:
          print("Montante inválido\nExcedeu o limite por carregamento")
          sleep(0.5)
          print("A CANCELAR OPERAÇÃO")
          sleep(1)
          quit()
      elif mb<10:
          print("Montante inválido\nNão corresponde com o mínimo permitido")
          sleep(0.5)
          print("A CANCELAR OPERAÇÃO")
          sleep(1)
          quit()
      card= random.randint(123456789,987654321)
      print("A gerar o cartão...")
      sleep(2)
      print(" __________________________")
      print("|MBNet                     |")
      print("|                          |")
      print("|  %s               |" %(card))
      print("|             Montante:%s€ |" %(mb))
      print("|__________________________|")
      fl=input("Selecione ENTER para fechar operação ")
      if fl==str:
          sleep(1)
          quit()    
elif sel==4:
    tr=int(input("Insira o montante a transferir:"))
    if tr>m:
        print("A quantia excede o saldo disponível na conta")
        sleep(1.5)
        quit()
    conta=int(input("Insira o número da conta a transferir dinheiro: "))
    sleep(1)
    print("Transferência efetuada com sucesso")
    sleep(1)
    quit()
elif sel==5:
    print("---------------")
    print("1- Transportes")
    print("2- Telemóveis")
    print("---------------")
    op=int(input(""))
    if op==1:
        passe=int(input("Insira o número do passe que pretende carregar: "))
        mnt=int(input("Insira o montante que pretende carregar: "))
        if mnt>m:
            print("A quantia que está a tentar carregar é superior ao saldo disponível na conta\nA CANCELAR OPERAÇÃO")
            sleep(2)
            quit()
        print("Transferência efetuada com sucesso")
        sleep(1.5)
        quit()
    elif op==2:
        tlmv=input("Insira o número que pretende carregar: ")
        ver=len(tlmv)
        if ver>=10 or ver<=8:
            print("Número inválido\nA CANCELAR OPERAÇÃO")
            sleep(2)
            quit()
        mnt=int(input("Insira o montante que pretende carregar: "))
        if mnt>m:
            print("A quantia que está a tentar carregar é superior ao saldo disponível na conta\nA CANCELAR OPERAÇÃO")
            sleep(2)
            quit()
        print("Transferência efetuada com sucesso")
        sleep(1.5)
        quit()
elif sel==6:
      print("Só é permitido o depósito de notas!")
      dep=int(input("Insira o montante que pretende depositar: "))
      if dep<5:
          print("Quantia inválida, a quantia mínima são 5 euros")
          print("A CANCELAR OPERAÇÃO")
          sleep(1.3)
          quit()
      print("Insira o dinheiro")
      sleep(3)
      print("Transação concluida")
      print("A fechar operação")
      sleep(1)
      quit()


