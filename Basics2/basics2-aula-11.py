#dicionários

dadosCidade = {
    'nomes' : 'São Paulo',
    'estado' : 'São Paulo',
    'area' : 1521,
    'populacao' : 12.18
}

print(type(dadosCidade))
print(dadosCidade)

dadosCidade['pais'] = 'Brasil' #acréscimo de dado
print(dadosCidade)
print(dadosCidade['nomes'])

dadosCidade['area'] = 1500 #nova atribuição, essa alteração é permanente
print(dadosCidade)

dadosCidade2 = dadosCidade.copy() #copia de dados para novo dicionario
dadosCidade2['nomes'] = 'Santos' #alteração de dado
print(dadosCidade)
print(dadosCidade2)

novosDados = {    #atualizacao de dados
    'populacao' : 15,
    'fundacao' : '25/01/1554'
}
dadosCidade.update(novosDados)
print(dadosCidade)

print(dadosCidade.get('prefeito')) #consulta se existe a variável chamada

print(dadosCidade.keys()) #retorna uma lista de chaves de um dicionário
print('espacamento')
print(dadosCidade.values()) #retorna uma lista de valores de um dicionario
print('espacamento')
print(dadosCidade.items()) #retorna uma lista de tuplas (chave,valor) de um dicionário
