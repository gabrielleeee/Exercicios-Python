#Faça um programa em Python que leia um valor inteiro e mostre a tabuada (de 1 a 10 ) do valor lido.

num = int(input("Digite um número: "))

contador = 1
lista = []

while contador <=10:
    resultado = num * contador
    contador = contador + 1
    lista.append(resultado)


for i, nome in enumerate(lista):
    print(i+1, "x", num, "=",nome)
