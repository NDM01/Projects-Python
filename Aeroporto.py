import os
from time import sleep

def menu():

    print("-----------------------------")
    print("1 - Consultar Voos")
    print("2 - Consultar Aviões")
    print("3 - Consultar Aeroportos")
    print("4 - Consultar Pilotos")
    print("5 - Consultar Tripulação")
    print("6 - Consultar Passageiros")
    print("7 - Sair")
    print("-----------------------------")
    

print("Bem-Vindo!") 
sleep(1)
print("\n" * os.get_terminal_size().lines)

programa = True

while programa == True:
    
    menu()

    programa = False
    
    

    


    


