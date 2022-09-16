#Operadores numéricos

x = 50
y = 2

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y #sempre retorna tipo float
exponenciacao = x ** y
divisaoInteira = x // y #ignora casas depois da vírgula NÃO ARREDONDA, retorna tipo int
resto = x % y

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(exponenciacao)
print(divisaoInteira)
print(resto)

#operadores lógicos

temCafe = True
temPao = False

print(not temCafe) #inverte o operador
print(temCafe and temPao) #todos valores dever sem true para retornar true
print(temCafe or temPao) #ao menos um valor deve ser true para retornar true

#operadores relacioanais
print('comparação de valores')

print(x > y)
print(x < y)
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)