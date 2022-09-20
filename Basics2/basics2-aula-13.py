#Funções - uma sequencia de comandos que fica salva e roda quando chamamos

def hello (): #primeiro bloco é a definição da função
    print('Olá Mundo!') #O que a função fará
hello() #chamada da função

def calculaMedia(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media #linha que retorna o valor, mas sem impressão
resultado = calculaMedia(10,9,8)
print(resultado)

resultado2 = calculaMedia(valor1=10, valor2=9, valor3=8) #outra forma de atribuir valores
print(resultado2)

print('Olá', end=' ') #por padrão toda função tem quebra de linha, se utilizado o end='' a quebra de linha será substituída pelo valor contido nas aspas
print('Pietro')

def calculaMedia(valor1=0, valor2, valor3=0): #se utilizar valores default, neste caso zero, a construção correta é (valor2, valor1=0, valor3=0), com os default após o valor variável
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media
resultado = calculaMedia(10)
print(resultado)
