# Definindo função com parametro obrigatorio
def quadrado(numero):
    return numero ** 2

print(quadrado(2))

# Função com mais de um parametro
def mais_de_um(num, letra, ativo):
    return num, letra, ativo

print(mais_de_um(1,'a', False))

# Parametros nomeados - keywords arguments
def nome_completo(nome, sobrenome):
    return nome + sobrenome

print(nome_completo(nome='Hello', sobrenome='World'))

