#Faça um programa que peça para o usuário digitar uma palavra e imprima cada letra em uma linha.

nome = input('Digite uma palavra:')

for carac in nome:
    if carac == ' ':
        continue ##caso seja um nome composto ou seja dado excessivos espaços, a função ignora
    print(carac)