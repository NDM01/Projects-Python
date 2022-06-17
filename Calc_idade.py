from datetime import date 

teste = int(input("Insira o ano: "))
mes = int(input("Insira o mes: "))
dia = int(input("Insira o dia: "))
  
def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
          
print(calculateAge(date(teste, mes, )), "anos")