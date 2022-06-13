from time import sleep
n = int(input("Insira o número em que pretende que a contagem começe: "))
for x in range(n):
    print(x+1)
    sleep(1)
else:
    print("FIM")