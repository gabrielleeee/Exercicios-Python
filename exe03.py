#Escreva um programa que resolva uma equação de segundo grau
import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b**2) - (4 * a) * c
if delta <=0:
    print("Delta negativo")
else:
    x1 = (-b - math.sqrt(delta)) / (a * 2)
    x2 = (-b + math.sqrt(delta)) / (a * 2)

print("Delta é igual a: ",delta,", O resultado de x1 é: ",x1,", E x2 é igual a: ",x2)


