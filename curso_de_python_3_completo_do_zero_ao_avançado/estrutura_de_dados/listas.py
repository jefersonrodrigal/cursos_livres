"""
-> São objetos indexaveis
-> São mutaveis
"""

# declaracao
lista = [1, 2, 3, 4, 5, 6, 6, 2]

# append() -> Adicionar elementos a lista
lista.append(10)
print(lista)

# pop() -> Retorna e remove o ultimo elemento da lista
print(lista.pop())

# Para modificar pelo index
lista[0] = 20
print(lista)

