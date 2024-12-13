# Utilização de *args
def soma_numeros(*args):
    print(args)
    return sum(args)


# Utilizando parametros obrigatorios e *args
def nome_completo(nome, sobrenome, *args):
    print(nome, sobrenome)
    return args


# Utilização **kwargs
def corros(**kwargs):
    print(kwargs)

corros(portas=4, rodas=4, passageiros=2, marca='Ford', modelo='Focus', ano=2000, ativo=True)

# Utilizando  parametros em ordem correta
# parametros obrigatorios
# parametros opcionais
# *args
# **kwargs

# Desempacotamento kwargs
def mostra_nome(**kwargs):
    return f'Nome- { kwargs['nome']} Sobrenome- {kwargs['sobrenome']}'

obj = {'nome': 'Hello', 'sobrenome': 'World'}

print(mostra_nome(**obj))