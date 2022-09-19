#estruturas condicionais
#programa para decidir se pego uber ou não

valorPassagem = 4.00
valorCorrida = input('Informe o valor da corrida: ')
valorAceite = valorPassagem * 5
valorEspera = valorPassagem * 6

if float(valorCorrida) <= valorAceite: #uso de : para espaçar corretamente e permancer no bloco condicional
    print('Pague a corrida')
elif float(valorCorrida) <= valorEspera:
    print('Espere um momento, o valor pode abaixar')
else:
    print('Pegue um onibus')