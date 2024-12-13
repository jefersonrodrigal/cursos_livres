# Utilização
numeros = {num for num in range(1,7)}
print(numeros)

# Com processamento
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Gerando um dicionario
numeros = {key: key ** 2 for key in range(10)}
print(numeros)

# Com string
letras = {letra for letra in 'Hello World'}
print(letras)