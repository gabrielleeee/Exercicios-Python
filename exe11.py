#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km = float(input("Digite a quantidade de Km percorridos com o carro: "))
dias = int(input("Digite a quantidade de dias que o carro ficou alugado: "))

calculo = (dias * 60) + (0.15 * km)

print('O valor a ser pago é: ',calculo)