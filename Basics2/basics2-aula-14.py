#args e kwargs

def calculaMedia(*args): #por convenção utliza-se a string args, mas pode ser qualquer nome. Este tipo de função é reconhecido como uma tupla, logo pode-se fazer qualquer operação que se faz em tuplas
    soma = sum(args)
    media = soma / len(args)
    return media
print(calculaMedia(10, 9 ,8))

def calculaMedia(*args, margem): #se quiser adicionar um valor fora da tupla, o mesmo deve ser definido e chamado no return
    soma = sum(args)
    media = soma / len(args)
    return media + margem
print(calculaMedia(10, 9 ,8, margem=0.1))

def infoDados(**kwargs): #essa função é reconhecida como um dicionário
    print(kwargs, type(kwargs))
infoDados(nome='Pietro', sobrenome='Ribeiro')