# Entrada de dados
print("Qual seu nome")
nome = input()

print("Seja bem vindo(a) %s" %nome) # Exemplo print python 2x
print("Seja bem vindo(a) {0}".format(nome))  # Saida de dados a partir das versões 3x
print(f"Seja bem vindo(a) {nome}") # saida mais atualizada
print("Qual sua idade")
idade = input()

print("%s tem %s anos" %(nome, idade)) # Exemplo print python 2x
print("{0} tem {1} anos".format(nome, idade)) # Saida de dados a partir das versões 3x
print(f"{nome} tem {idade} anos") # saida mais atualizada

# Casting
int(idade)

# Entrada de dados simplificado
input_simplificado_nome = input("Qual seu nome? ")
input_simplificado_idade = int(input("Qual sua idade? "))
