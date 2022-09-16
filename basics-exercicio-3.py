#Vamos fazer um programa para verificar quem é o assassino de um crime.Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
#a. Mora perto da vítima?
#b. Já trabalhou com a vítima?
#c. Telefonou para a vítima?
#d. Esteve no local do crime?
#e. Devia para a vítima?
#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados

contador = 0

print('Responda as perguntas a seguir com s para sim e n para nao')

resposta1 = input('Mora perto da vitima? ')
resposta2 = input('Ja trabalhou com a vitima? ')
resposta3 = input('Telefonou para a vitima? ')
resposta4 = input('Esteve no local do crime? ')
resposta5 = input('Devia para a vitima? ')

if resposta1 == 's':
    contador = contador + 1
if resposta2 == 's':
    contador = contador + 1
if resposta3 == 's':
    contador = contador + 1
if resposta4 == 's':
    contador = contador + 1
if resposta5 == 's':
    contador = contador + 1

if contador == 5:
    print('E o assassino')
elif contador < 5 and contador > 2:
    print('E suspeito')
else:
    print('Liberado')