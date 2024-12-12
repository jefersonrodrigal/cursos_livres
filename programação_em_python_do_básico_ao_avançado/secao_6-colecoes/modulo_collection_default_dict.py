from collections import defaultdict


# Criação de dicionarios
dicionaro = {'curso':'Programação de Python Essencial'}

print(dicionaro)
print(dicionaro['curso'])

dicionario_default = defaultdict(lambda : None)

dicionario_default['curso'] = 'Desenvolvimento Web'

print(dicionario_default)

print(dicionario_default['aluno'])

print(dicionario_default)