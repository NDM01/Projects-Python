x=input("Insira o seu nome: ")
while x.isnumeric():
     print("Nome inválido!")
     x=input("Insira o seu nome: ")
print("Bem vindo " + x)
print("Futebol -> 1 \nTénis -> 2 \nPing-Pong -> 3 \nKaraté -> 4 \nNatação -> 5")
y=int(input("Insira o desporto que pretende praticar: "))
while y>5 or y==0:
    print("Desport Inválido")
    y = int(input("Insira o desporto que pretende praticar: "))
if y==1:
    print("Parabéns %s está inscrito em futebol!" %(x))
elif y==2:
    print("Parabéns %s está inscrito em ténis!" %(x))
elif y==3:
    print("Parabéns %s está inscrito em ping-Pong!" %(x))
elif y==4:
    print("Parabéns %s está inscrito no karaté!" %(x))
elif y==5:
    print("Parabéns %s está inscrito na natação!" %(x))
