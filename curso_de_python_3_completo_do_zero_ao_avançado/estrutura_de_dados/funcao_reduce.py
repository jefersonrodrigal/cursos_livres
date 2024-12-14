"""
Não é mais nativo a partir da versão 3 deve fazer o seguinte import

from functools import reduce

"""

from functools import reduce

numeros = range(1, 10)

soma = reduce(lambda x, y : x + y, numeros)

print(soma)