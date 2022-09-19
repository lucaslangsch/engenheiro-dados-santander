idade = input('Insira aqui sua idade: ')
print(idade, type(idade)) #função input sempre retorna tipo string

idade = int(idade) #int() transforma a variável para o tipo chamado inteiro
print(idade, type(idade))

int(123abc) #o valor deve obedecer os parâmetros da classe para que haja a conversão

print(float(125)) #transforma em decimal
print(str(125), type(str(125))) #transforma em string
print(bool('')) #vazio retorna false (0)
print(bool('abc')) #contem valor retorna true (1)
print(bool(0)) #atribuido 0 retorna false (0)
print(bool(3)) #atribuido 3 retorna true (1)

