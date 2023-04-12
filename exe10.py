#Fazer um algoritmo que ao receber o salário atual de um funcionário, 
# calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
# SALARIO ATUAL              REAJUSTE
# abaixo de 500               15%
# de 500 até 1000             10%
# acima de 1000               5%

salario = float(input("Digite seu salário: "))

if salario < 500:
    calculo = (salario * 15) / 100
    salarioNovo = calculo + salario
    print("O salário com reajuste é de R${:.2f}".format(salarioNovo))
elif salario >= 500 and salario < 1000:
    calculo = (salario * 10) / 100
    salarioNovo = calculo + salario
    print("O salário com reajuste é de R${:.2f}".format(salarioNovo))
else:
    calculo = (salario * 5) / 100
    salarioNovo = calculo + salario
    print("O salário com reajuste é de R${:.2f}".format(salarioNovo))