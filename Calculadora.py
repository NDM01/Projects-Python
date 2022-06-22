num1 = input("Insira o primeiro número: ")

op = input("Insira o operador: ")

num2 = input("Insira o segundo número: ")

resultado = 0

if not num1.isnumeric() or not num2.isnumeric():
    print("Só são aceites números!")

num1 = int(num1)
num2 = int(num2)

if op == '+':
    resultado = num1 + num2
    print(f'O resultado é: {resultado}')

elif op == '-':
    resultado = num1 - num2
    print(f'O resultado é: {resultado}')
elif op == '*':
    resultado = num1 * num2
    print(f'O resultado é: {resultado}')
elif op == '/':
    resultado = num1 / num2
    print(f'O resultado é: {resultado}')
else:
    print("Operador inválido!")
    