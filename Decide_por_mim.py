from operator import truediv
from random import choice

answers=['Sim!', 'Não!', 'Talvez', 'Não acho boa ideia', '100% SIM', 'Naaah', 'Acho uma excelente ideia']

while True:
      
      question=input("Insira a sua pergunta: ")

      if question.isalpha() != True and not '?' in question:
          print('Ei, faça uma pergunta!')
          continue
      else:
          print(choice(answers))
