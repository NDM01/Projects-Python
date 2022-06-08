from time import sleep
from traceback import print_tb
ponto=0
fl=input("ENTER para começar ")
print("1- Qual é o carro mais rapido do mundo?")
print("1- Toyota Supra\n2- C63s\n3- 488 pista\n4- Buggati Chiron")
p1=int(input("Resposta: "))
print("A validar resposta...")
sleep(1)

if p1 == 4:
    print("Resposta certa! :)")
    ponto = ponto + 1

else:
    print("Resposta errada :(")

sleep(1)
print("2- Qual é a marca mais valiosa atual?")
print("1- Mercedes\n2- Ferrari\n3- Tesla\n4- Toyota")
p2=int(input("Resposta: "))
print("A validar resposta...")
sleep(1)

if p2 == 4:
    print("Resposta certa! :)")
    ponto = ponto + 1

else:
    print("Resposta errada :(")

sleep(1)
print("3- Qual foi a primeira marca de carros a ser criada?")
print("1- Mercedes\n2- Fiat\n3- Ford\n4-n Renault")
p3=int(input("Resposta: "))
print("A validar resposta...")
sleep(1)

if p3 == 3:
    print("Resposta certa! :)")
    ponto = ponto + 1

else:
    print("Resposta errada :(")

print("A gerar qualificação...")
sleep(2)
if ponto == 3:
    print("Parabéns acertou todas as perguntas :)")
    sleep(2)
    quit()

elif ponto == 2:
    print("Acertou 2 de 3, nada mau! :|")
    sleep(2)
    quit()

elif ponto ==1:
    print("Acertou apenas 1, mais sorte para a próxima vez :(")
    sleep(2)
    quit()

elif ponto == 0:
    print("Não acertou nenhuma pergunta :(")
    sleep(2)
    quit()