nome = 'Hello World'
lista = [1,2,3,4,5,6,7,8,9]

# Estrutura for em strings
for letra in nome:
    print(letra)

print()
# Estrura for em listas
for numero in lista:
    print(numero)

print()
# estrutura for em range
"""
A função range aceita 3 parametros
range(start=0, end, stop=1)
Vai até o valor final -1
"""
print()
for n in range(1,10, 2):
    print(n)

print()
"""
O enumerate
Quando se tem dois valores onde um podemos descartar podemos substituir o mesmo pelo _
"""
for i, v in enumerate(nome):
    print(nome[i])