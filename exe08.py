#Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números
# de 1 até ao número digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).int()

from functools import reduce

num = int(input("Digite um número: "))

a = num
lista = []

while a > 0:
    lista.append(a)
    a = a - 1

def soma(x,y):
    return x+y

resultado = reduce(soma,lista)
print(resultado)