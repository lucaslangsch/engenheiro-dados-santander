#strings

empresa = "Let's Code" #uso de aspas duplas para usar strings com aspas simples
print(empresa)

frase = "O Diego da Let's Code disse: \"Hoje a piza eh por minha conta\". " #uso de contra barra para usar aspas duplas dentro da string
print(frase)

empresa = 'Google'
print(empresa[0]) #acessar o caracter na posição chamada
print(empresa[:3]) #slice

nomesCidades = 'Sao Paulo, Belo Horizonte, Rio de Janeiro, Brasilia'
print(nomesCidades)

nomesCidades = nomesCidades.split(', ') #função para quebrar a string em diferentes strings
print(nomesCidades)

cabecalho = '        MENU PRINCIPAL'
print(cabecalho)
print(cabecalho.strip()) #remove caracteres. função não é permanente, apenas ocorre quando chamada
print(cabecalho)

nomeCidade = 'rIO dE JanEIRO'

print(nomeCidade.title()) #Formata com apenas as primeiras palavras da frase em maiuscula
print(nomeCidade.capitalize()) #Apenas a primeira letra da frase em maiuscula
print(nomeCidade.lower()) #todos em minuscula
print(nomeCidade.upper()) #todos em maiuscula

nomeCidade = input('Que cidade é conhecida como cidade maravilhosa?: ')
nomeCidade = nomeCidade.strip()
while nomeCidade.lower() != 'rio de janeiro':
    print("Tente novamente: ")
    nomeCidade = input('Que cidade é conhecida como cidade maravilhosa?: ')

print('Acertou')

mensagem = 'Voce viu o que Pietro falou ontem na sala?'
print('Pietro' in mensagem) #localização de strings ou caracteres dentro da string completa