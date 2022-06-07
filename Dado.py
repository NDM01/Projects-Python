from time import sleep
from random import choice

lado=['1', '2', '3', '4', '5', '6']

while True:
      
    
    fl=input("Selecione ENTER para rodar o dado")
    print("-----------")
    print("")
    print(choice(lado))
    print("")
    print("-----------")
    if fl==str:
        print(choice(lado))
        continue
    
    