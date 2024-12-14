"""
Similar ao map ele recebe uma função e uma lista
"""

numeros = range(1, 10)

# Implementação filter
numeros_filtrados = filter(lambda x : x > 5, numeros)

print(numeros_filtrados) # Retorna um objeto filter

print(list(numeros_filtrados))

# Implementação list comprhension
filtrados = [x for x in numeros if x > 5]
print(filtrados)