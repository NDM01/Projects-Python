prom = '25%'

valor = int(input("Insira o montante da compra: "))

if valor >= 100:
    desc = valor * 0.25 
    total = valor - desc
    print("A compra ultrapassa os 100€, portanto tem direito a %s de desconto\nFicando por: %s€" %(prom,total))
else:
    print("A compra não ultrapassa os 100€, não tendo direito a desconto\nFicando por: %s€" %(valor))