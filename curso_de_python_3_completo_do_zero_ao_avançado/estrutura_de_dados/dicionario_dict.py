"""
-> estrutura de "chave" : valor
-> Nome das chaves devem ser sempre strings - os valores podem receber qualquer tipo de dado
-> Podem ser acessados via chave
-> É possivel utilizar a palavra reservada in ou not in para avaliar true ou false se existe uma chave no dicionario

"""

# Declaração
qualquer = {"nome": "usuario", "idade": 20}

# Para adicionar item: valor
qualquer["telefone"] = "32456789"

print(qualquer)

# Para deleção de item : valor utiliza
del qualquer["telefone"]

print(qualquer)

# Para listar de forma ordenada as chaves
print(sorted(qualquer))

# Pegar um valor a partir de uma chave do dicionario
print(qualquer.get("nome"))

# retorna uma lista dict keys
print(qualquer.keys())

#Retrona uma lista de dict values
print(qualquer.values())

# retorna uma lista de tuplas de dict_itens
print(qualquer.items())
