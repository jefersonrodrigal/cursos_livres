# Utilização para criar lista
result = [numero for numero in range(1,10)]
print(result)

# Realizando processamento
result_process = [numero * 2 for numero in range(1,10)]
print(result_process)

# Exemplo video
result_lista = [bool(valor) for valor in [0,[], '', True, 1, 3, 14]]
print(result_lista)

# condicionais - simples
numeros_pares = [numero for numero in range(1,90) if numero % 2 == 0]
print(numeros_pares)

# Condicional - composta
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in range(1,20)]
print(res)