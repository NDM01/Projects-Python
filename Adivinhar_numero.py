import random
from time import sleep
n1= random.randrange(10,20)
n2= random.randrange(10,20)
m= random.randrange(10,3000)
print("A gerar número...")
sleep(1)
ma=m+n1
mi=m-n1
tn=int(0)
print("O número encontra-se entre %s e %s" %(mi, ma))
tent=int(input("Adivinhe o número: "))
while tent != m:
    tent=int(input("Adivinhe o número: "))
    tn=tn+1
if tent==m:
    print("Parabéns acertou no número! Ao fim de %s tentativas" %(tn))