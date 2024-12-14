"""

"""

minha_lista = [0, 1, 2, 3, 4]

# Usando list comprhension
lista = [x for x in range(5)]

print(minha_lista)
print(lista)

# Usando list comprhension + condicional
lista_cond = [x for x in range(30) if x % 2 == 0]
print(lista_cond)

# Utilizando mais de um for

amigos_fred = ["josi", "felipe", "pedro", "paulo"]
amigos_davi = ["manu", "pedro", "josi", "danilo"]

amigos_em_comum = [af for af in amigos_fred for ad in amigos_davi if af == ad]
print(amigos_em_comum)