from time import sleep
import random

erro = 1

def acertou_palavra():
    print("Parabén acertou na palavra!!")
    print(" :)")
    sleep
    quit()

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca v2.0!***")
    print("*********************************")

mensagem_abertura()

print("A gerar palavra...")

sleep(1)

lista = ['gato','escola','kiwi','hospital','aluno','cola','pneu','barco','garraga','monitor','quadro','estrada','caneta','computador','carteira','mesa','carro','galinha','casa','mota','capacete','lancheira','janela','telhado','borracha','churrasco','luz','estojo']

pal = random.choice(lista)

print("Lista de palavras:\n %s " %(lista))

resp = input("Insira a resposta: ")

while resp != pal:
    print("Errado!")
    resp = input("Insira a resposta: ")
    if resp != pal:
        erro = erro + 1
    if erro == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif erro == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif erro == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif erro == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif erro == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif erro == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print(" |            ")
        print("_|___         ")
    elif erro == 7:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print("Perdeu!")
        quit()
        
if resp == pal:
   acertou_palavra()  




