num = input("Insira o número para verificar se é par ou ímpar: ")

if num.isdigit():
   num = int(num)
   if num % 2 == 0:
     print("O número é par")
   else:
     print("O número é ímpar")
else:
    print("Número inválido!")
    quit()
