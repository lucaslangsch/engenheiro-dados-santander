#Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
#Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].

lista1 = eval('[' + input("Digite sua lista 1 com valores separados por ', ' ") + ']')
lista2 = eval('[' + input("Digite sua lista 2 com valores separados por ', ' ") + ']')
lista3 = []
contador = 0

if len(lista1) < len(lista2):
    while len(lista1) < len(lista2):
        lista1.append(0)
elif len(lista1) > len(lista2):
    while len(lista1) > len(lista2):
        lista2.append(0)


while contador < len(lista1):
        lista3.append(lista1[contador] + lista2[contador])
        contador = contador + 1
print(lista3)