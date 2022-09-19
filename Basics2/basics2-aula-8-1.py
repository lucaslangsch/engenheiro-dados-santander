#Tuplas

#Semelhantes a listas, porém seus elementos uma vez definidos não podem mais ser alterados. Possui algumas implementações especiais e armazena uma quantidade de dados menores

nomesPaises = ('Brasil', 'Argentina', 'China', 'Canada', 'Japao') #uso de parenteses ou não
print(nomesPaises, type(nomesPaises))

nomeEstado = 'São Paulo',
print(nomeEstado, type(nomeEstado))

print(len(nomesPaises)) #função len igual

print(nomesPaises[1]) #funções de slice são iguais

b, a, c, ca, j = nomesPaises #unpack, atribuir novas varíaveis oriundas da tupla
print(b, c, j)

print(*nomesPaises) #impressão de todos os elementos, porém não mais em forma de tupla