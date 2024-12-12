
# Definição de lista
lista = [1,99,4,27,44,42, 90]

# Lista  apartir de um range
lista_1 = list(range(11))
print(lista_1)

# Lista a partir de uma string
lista_2 = list('HelloWorld')
print(lista_2)

# Checando se um elemento está presente na lista
if 8 in lista_1:
    print(True)

if 'H' in lista_2:
    print(True)

# Metodos para listas
# sort() -> modifica a lista retornando uma nova lista ordenada
lista.sort()
print(lista)

# Contar o numero de ocorrencia de um elemento em uma lista
print(lista_2.count('l'))

# Adicionar elementos na lista
lista.append(100)
print(lista)

# Adiciona uma lista em outra - elemento por elemento - só aceita iteraveis como argumento
lista_1.extend(lista)
print(lista_1)

# Adicionar elementos na lista informando a posição
lista.insert(0,1000)
print(lista)

# Juntando duas listas com o operador + - Funciona equivalente ao metodo extend
lista_3 = lista + lista_1
print(lista_3)

# Imprimindo uma lista inversa - Modifica a lista e retorna uma lista de ordem inversa
lista_1.reverse()
print(lista_1)

# Lista inversa por slice
print(lista[::-1])

# fazer copia de uma lista
lista_4 = lista.copy()
print(lista_4)

# remove o ultimo elemento de uma lista  e o retorna - altera a lista original
print(lista_4)
print(lista_4)

# É possivel passar o indice de um elemento especifico para ser removido.
# Caso não haja elemento no indice informado teremos a exceção IndexError
lista_4.pop(2)
print(lista_4)

# Para remover todos os eleemntos de uma lista
lista_4.clear()
print(lista_4)

print(lista_2)

# Criando uma string a partir de uma lista
lista_5 = ''.join(lista_2)
print(lista_5)

# Iterando sobre listas utilizando for
for elemento in lista:
    print(elemento)

# Forma eficiente de criar uma lista numerica
numeros = list(range(1, 6))
print(numeros)

# Fazendo acesso por indice
cores = ['Amarelo', 'Azul', 'Branco', 'Verde', 'Preto', 'Laranja']
print(cores[0])

# Acessando o ultimo elemento da lista
print(cores[-1])

# Remove um elemento especifico da lista
cores.remove('Amarelo')
print(cores)

# Usando a função enumerate - como segundo argumento é possivel passar o valor de inicio do indice - Esse valor é opcional
for i, cor in enumerate(cores, 1):
    print(i, cor)

# Encontrar indice de elemento - Caso haja elemnto duplicado, retorna o indice do primeiro elemento encontrado
lista_6 = list(range(10, 51))
print(lista_6.index(50))

# Soma os Elementos de uma lista
print(sum(lista_6))

# Encontrar o valor maximo em uma lista
print(max(lista_6))

# Encontrar o valor minimo em uma lista
print(min(lista_6))

# verificar o tamanho da lista
print(len(lista_6))

# Desempacotamento de elementos
lista_7 = list(range(1,4))

num1, num2, num3 = lista_7

print(num1)
print(num2)
print(num3)
