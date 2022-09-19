#Listas

nomesPaises = ['Brasil', 'Argentina', 'China', 'Canada', 'Japao'] #estrutura de uma lista
print(nomesPaises)

print('Tamanho da lista: ', len(nomesPaises))

print('Pais: ', nomesPaises[4]) #acesso ao elemento de indice 4, lembrando que o primeiro elemento e 0

print('Pais: ', nomesPaises[-1]) #acesso ao ultimo item, nessa ordem é contabilizado a partir do -1

print('Pais: ', nomesPaises[-2]) #acesso ao penúltimo 

nomesPaises[4] = 'Colombia' #substituição de elemento na posicao chamada, neste caso posicao 4
print(nomesPaises[4])

print(nomesPaises[1:3]) #slicing, fatiação, fracionamento de uma lista. Neste caso da posição 1 até a 2, a posição 3 é ignorada

print(nomesPaises[1:-1])# da posição 1 até a penultima, diferente do acesso aqui a posição -1 é a penultima

print(nomesPaises[1:]) #para acessar até a ultima o slice deve ter o ultimo indice omitido

print(nomesPaises[:3]) #para acessar a partir da posição zero o primeiro índice pode ser omitido

print(nomesPaises[:]) #se ambos os indices forem omitidos, toda a lista é chamada

print(nomesPaises[::2]) #chamar apenas os indices num determinado número de intervalo e dando saltos (primeiroindice:ultimoindice:quantidadepulos)

print(nomesPaises[::-1]) #inversao da lista

print('Brasil' in nomesPaises) #pesquisa de valores dentro da lista, lembrando que strings diferenciam maiuculas e minusculas. Retorna valor boolean

print('Brasil' not in nomesPaises) #pesquisa se valor está dentro da lista. Retorna valor boolean

listaCapitais = [] #cria uma lista vazia
listaCapitais.append('Brasilia') #adiciona um elemento na lista. A adição de novos elementos acontece no primeiro índice vazio, neste caso de uma lista vazia o primeiro índice é o zero
listaCapitais.append('Buenos Aires')
listaCapitais.append('Pequim')
listaCapitais.append('Bogota')

print(listaCapitais)

listaCapitais.insert(2, 'Paris') #insere um elemento na posição chamada, os outros elementos são deslocados para a direita
print(listaCapitais)

listaCapitais.remove('Buenos Aires') #remove o elemento chamado
print(listaCapitais)

removido = listaCapitais.pop(2) #remove o elemento no indice chamado e guarda o valor removido
print(listaCapitais, removido)