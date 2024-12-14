"""
- strings são imutaveis
"""

# acessando por index
palavra = "Palavra"

# Acessa o primeiro caractere da cadeia de caracteres
print(palavra[0])

# Acessa o ultimo caractere da cadeia de caractere
print(palavra[-1])

# Slicing
print(palavra[0:2]) # Funciona pegando o indice inicial e o final -1
print(palavra[:2]) # Pega todos os caracteres iniciais até o indice final -1
print(palavra[2:]) # Pega a partir do indice dois até o final

# O metodo len() calcula o tamanho da string
print(len(palavra))
