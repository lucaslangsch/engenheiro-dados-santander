#strings segunda parte

cumprimento = 'Olá, '
nome = 'Felipe'

print(cumprimento + nome)

print(nome * 5)

idade = 35
filhos = 2
print(nome + ' tem ' + str(idade) + ' anos e ' + str(filhos) + ' filhos.')

print('{} tem {} anos e {} filhos.'. format(nome, idade, filhos)) #concatenação através do método format, ele concatena e formata

precoGasolino = 3.476
print('O preço da gasolina subiu e está em R$ {:.2f}'.format(precoGasolino)) #:. indica a seleção de casas decimais, 2 o número e f o tipo float. o método também arredonda

print(f'{nome} tem {idade} anos e {filhos} filhos') #atalhos pro método format