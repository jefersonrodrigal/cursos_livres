"""
Retorna os itens de uma lista e o index dos mesmos

"""
alfabeto = list("abcdefghijlmnopqrstuvxz")

print(alfabeto)

# Implementação
for index, letra in enumerate(alfabeto, 1):
    print(f"{index} - {letra}")
