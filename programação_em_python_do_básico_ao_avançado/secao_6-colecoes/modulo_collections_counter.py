from collections import Counter
# Utilização - Exemplo 1
lista = list(range(1,50))
print(lista)
res = Counter(lista)
print(res)

# Utilizando com string -> Para cada um dos caracteres é criado uma chave e seu valor é aquantidade de ocorrencias
print(Counter('Hello World'))

texto = '''
Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython.
'''
resp = Counter(texto)
print(resp)

# Mostra a ocorrencia mais repetidas
print(resp.most_common(10))
