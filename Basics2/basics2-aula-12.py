#iteração for loop

nomesCidades = ['Sao Paulo', 'Londres', 'Paris', 'Toquio'] #laço para navegar na lista, tupla ou dicionario para trazer o elementos
for nome in nomesCidades:
    print(nome)

contador = 0 #construção usando while mas com mesma função do for, necessita mais linhas de código
while contador < len(nomesCidades):
    print(nomesCidades[contador])
    contador = contador + 1

nomesCidades = 'Sao Paulo', 'Londres', 'Paris', 'Toquio' #laço para navegar na tupla. igual em lista
for nome in nomesCidades:
    print(nome)

cidade = {
    'nome' : 'Sao Paulo',
    'estado' : 'Sao Paulo',
    'populacao': 12.2
}
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')  #laço for para dicionários

nomesCidades = ['Sao Paulo', 'Londres', 'Paris', 'Toquio'] #tentativa de nova atribuição, porém a variável nome criada é apenas uma cópia, logo o valor 'rio de janeiro' não é atribuído a lista
for nome in nomesCidades:
    nome = 'Rio de Janeiro'
print(nomesCidades)

for posicao in range(len(nomesCidades)): #atribuição correta de novos valores usando a função for
    print(posicao)
    nomesCidades[posicao] = 'Rio de Janeiro'
print(nomesCidades)

print(range(10)) #função range, traz os valores até o número chamado
print(list(range(10))) #se trazido a uma lista, retorna do index 0 até o décimo, que é o número 9
print(list(range(2,10))) #traz o range de um valor inicial até o final
print(list(range(2,10,2))) #traz o range de um valor inicial até o final com steps