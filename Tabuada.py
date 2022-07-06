from time import sleep

cal = 0

tab = int(input("Insira o número que prentende saber a tabuada: "))

print("Calculando...")

sleep(1)

for x in range(11):

    if x == 0:
        print("Tabuada:")
    else: 
    
     cal = tab * x

     print("%s x %s = %s" %(tab, x, cal))


