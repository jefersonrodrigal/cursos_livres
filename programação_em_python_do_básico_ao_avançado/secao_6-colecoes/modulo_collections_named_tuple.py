from collections import namedtuple

tupla = tuple(range(1,10))

print(tupla)

# declaração namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')

gato = namedtuple('gato', 'idade, raca, nome')

peixe = namedtuple('peixe', ['idade', 'raca', 'nome'])


# Usando
rex = cachorro(idade=2, raca='pincher', nome='rex')
bichano = gato(idade=2, raca='perca', nome='ursinho')

print(rex)
print(bichano)

# Acessando os valores das propriedades
print(rex.nome)
print(bichano.idade)