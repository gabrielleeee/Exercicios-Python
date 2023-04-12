#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sinal = input("Digite o sinal da operação matemática(+,-,*,/): ")

if sinal == "+":
    print(num1 + num2)
elif sinal == "-":
    print(num1 - num2)
elif sinal == "*":
    print(num1 * num2)
else:
    print(num1 / num2)