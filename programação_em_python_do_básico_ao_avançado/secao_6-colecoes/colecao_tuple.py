# Definição
tupla = (1, 2, 3, 4, 5, 6)

# O interpretador Python considade como tupla
tupla_2 = 1, 2, 3, 4, 5, 6, 7

# Representação de tupla com um unico elemento
tupla_3 = (1,)

# Gerando tuplas com range
tupla_4 = tuple(range(11))

# Desempacotamento de tupla
tupla_5 = ('Hello', 'World')
palavra1, palavra2 = tupla_5

# Calculando a soma - maximo - min - tamanho
soma = sum(tupla_2)
maximo = max(tupla_2)
minimo = min(tupla_2)
tamanho = len(tupla_2)

# É possivel concatenar tuplas com o operador +
tupla_6 = tupla_2 + tupla_4

# Iteração em tuplas
# for n in tupla_6:
#     print(n)

# Utilizando o enumerate
# for k, v in enumerate(tupla_6, 1):
#     print(k, v)

# Convertendo uma string para tupla
print(tuple('Hello World'))

# copiando uma tupla
tupla_7 = tupla_6
print(tupla_6)
print(tupla_7)