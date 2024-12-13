# Definição
# {key: value for value in iteravel}

# Manipulando os valores do dicionario
numeros = {'a': 1, 'b':2, 'c':3}
valor_ao_quadrado = {key: value **2 for key, value in numeros.items()}
print(valor_ao_quadrado)

# Transformando uma lista em dicionario
list_for_dict = {value: value ** 2 for value in list(range(1,10))}
print(list_for_dict)

# Aplicando logica condicional composta
res = {num: ('par' if num % 2 == 0 else 'impar') for num in range(1,10)}
print(res)