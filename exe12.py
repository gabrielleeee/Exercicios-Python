#3) Com o código do exercício 2, crie um novo programa que contenha um menu que estará em loop, 
#com as seguintes opções: 1- Mostrar tabuada 2- Sair. No qual a primeira opção pedirá para o 
#usuário digitar o número que será mostrada a tabuada de 1 a 10 e a segunda encerrará a execução.

opcao = int(input("Digite a opção desejada: \n 1-Mostrar Tabuada \n 2-Sair \n"))

while opcao == 1:
    num = int(input("Digite o número desejado para gerar a tabuada: "))

    contador = 1
    lista = []

    while contador <=10:
        resultado = num * contador
        contador = contador + 1
        lista.append(resultado)


    for i, nome in enumerate(lista):
        print(i+1, "x", num, "=",nome)

    opcao = int(input("Digite a opção desejada: \n 1-Mostrar Tabuada \n 2-Sair \n"))