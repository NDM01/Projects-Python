Soma= 0
Somapos = 0
Somaneg = 0

print('Insira a quantida de números: ')

N = int(input())

while N < 0:
  print('Número inválido!')

  N = int(input('Insira o número: '))

I = 0

for I in range(N):
  Num = int(input('Insira o número: '))
  if Num < 0:
    Somaneg = Somaneg + Num
    Soma = Soma + 1
  elif Num >= 0:
    Somapos = Somapos + 1

if Soma > 0:
  perc = Somaneg / Soma

percp = Somapos / N * 100

print('A média dos números negativos é', perc, 'e a percentagem de positivos é', percp)
            