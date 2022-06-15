from time import sleep 

Soma = 0
vz = int(input("Insira quantos números pretende inserir: "))
x = 1
for x in range(vz):
    val = int(input("Insira o %s número: " %(x + 1)))
    while val > 20:
        print("Valor inválido!")
        val = int(input("Insira o %s número: " %(x + 1)))
        
    Soma = Soma + val

Med = Soma / vz
print("A calcular a média...")
sleep(1)
print("A média dos valores é %s " %(Med))
