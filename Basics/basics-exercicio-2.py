#Faça um programa que leia a validade das informações:
#a. Idade: entre 0 e 150;
#b. Salário: maior que 0;
#c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação inválida

idade = input('Informe uma idade entre 0 e 150 anos: ')

while int(idade) < 0 or int(idade) > 150:
    idade = input('Erro, o valor deverá ser maior que 0 e menor que 150. Digite novamente: ')

print("Idade aceita")

salario = input('Informe seu salario: ')

while float(salario) <= 0.0:
    salario = input("Erro, seu salario devera ser maior que 0. Digite novamente: ")

print('Salario aceito')

sexo = input('Informe aqui seu sexo: ')

while sexo !='M' and sexo !='F' and sexo !='Outro':
    sexo = input('Erro, o sexo informado deve ser M, F ou Outro. Tente novamente: ')

print("Sexo aceito")