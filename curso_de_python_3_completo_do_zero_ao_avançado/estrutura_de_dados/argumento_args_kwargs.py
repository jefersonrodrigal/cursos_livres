"""
-> *args -> estrutura de tupla
-> **kwargs -> estrura de dicionario

"""

# implementação *args
def soma_valores(*args):
    return sum(args)

x = soma_valores(1, 2)

print(x)

# implementação *kwargs
def objeto(**kwargs):
    return kwargs


obj = objeto(nome="Jeferson", idade=23, ativo=True, online="online")

print(obj)
