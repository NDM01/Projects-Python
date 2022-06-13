x=int(input("Insira o primeiro número: "))
y=int(input("Insira o segundo número: "))

if x>y:
    print("%s é maior que %s" %(x,y))
elif x == y:
    print("%s é igual a %s" %(x,y))
elif y>x:
    print("%s é maior que %s" %(y,x))
