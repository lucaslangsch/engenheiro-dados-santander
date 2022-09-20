#Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = 0
for numero in listaNumeros:
    if numero % 2 == 0:
        pares = pares + 1
print('A quantidade de números pares é de {}.'.format(pares))
