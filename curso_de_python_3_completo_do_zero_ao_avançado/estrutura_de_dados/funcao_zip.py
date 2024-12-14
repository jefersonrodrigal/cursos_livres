"""
Utilizado para unir listas
"""

# implementação -> a função split em string transforma a string em uma lista separando os elementos por espaço
lista_1 = "batata couve frango abobora".split()
lista_2 = "fruta legume verdura carne".split()

print(lista_1)
print(lista_2)

lista_unificada = zip(lista_1, lista_2)

print(lista_unificada) # É gerado um objeto do tipo zip object

# para ver a união das duas listas deve se utilizar a seguinte implementação
x = list(lista_unificada)

print(x)