"""
Tudo o que for possivel realizar iteração é possivel utilizar a função map

"""

numeros = range(1, 10)

# Implementação map
quadrado_map = list(map(lambda x : x**2, numeros))
print(quadrado_map)

# OBS -> o que se faz com o map é possivel fazer de forma otimizada com comphension de listas
quadrado_comprhension = [z **2 for z in numeros]
print(quadrado_comprhension)