#estrutura de repetição while
'''
contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, 'item limpo')
    else:
        print(contador, 'itens limpos')
print ('Fim da repeticao do bloco while')

contador = 0

while True: #sempre sera verdadeiro, induz um loop infinito
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, 'item limpo')
        else:
            print(contador, 'itens limpos')
    else:
        break #quebra forcada do loop
print ('Fim da repeticao do bloco while')

texto = input('Digite a sua senha:')

while texto != 'LetsCode':
    texto = input('Senha invalida, tente novamente: ')

print("Acesso permitido")
'''
contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue #ignora o primeiro if e dá continuidade
    else:
        print(contador, 'itens limpos')
print ('Fim da repeticao do bloco while')