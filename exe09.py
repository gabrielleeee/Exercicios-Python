#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salárioFaça um programa que calcule o aumento de um salário. 
#Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

salario = float(input("Digite o salário: "))
porc = float(input("Digite a porcentagem do aumento do salário: "))

calculo = (salario * porc) / 100

salarioNovo = salario + calculo

print("O valor do aumento foi de: R${:.2f}".format(calculo), "resultando em um salário de: R${:.2f}".format(salarioNovo))
