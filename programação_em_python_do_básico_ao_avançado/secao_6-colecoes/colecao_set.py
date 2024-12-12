# Definição
conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto)
print(type(conjunto))

# Iteração
for n in conjunto:
    print(n)

# Adicionar elemento
conjunto.add(9)
print(conjunto)

# Remover elemento
conjunto.remove(7)
print(conjunto)

# Retorna None se o valor não for encontrado
conjunto.discard(10)
print(conjunto)

# Copiando conjunto
conjunt_2 = conjunto.copy()
print(conjunt_2)

# Metodos
turma_A = {'Marcos', 'Pedro', 'Ellen', 'Julia', 'Guilherme'}
turma_B = {'Fernanda', 'Gustavo', 'Heitor', 'Julia', 'Ana'}

# União->  union ou | -> Retorna a união de dois sets
unicos = turma_B.union(turma_A) # Forma 1
unicos_2 = turma_B | turma_A # Forma 2
print(unicos)
print(unicos_2)

# Interseção ou & -> Retorna elementos comuns entre os sets
ambos = turma_B.intersection(turma_A)
print(ambos)

# Diferença -> Retorna os elementos incomuns entre os sets
diferente = turma_A.difference(turma_B)
print(diferente)


# Utilizando o sum, max, min, len em conjuntos que possuam dados inteiros somente.
c = set(range(1,20))

print(c)

print(sum(c))
print(max(c))
print(min(c))
print(len(c))