#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros,
#  aceitar virgulas na entrada do usuário

metros = input("Digite o valor em metros: ")

metrosNovo = metros.replace (",",".")
cm = float(metrosNovo) * 100

print("O valor em cm é igual a: ",cm)

