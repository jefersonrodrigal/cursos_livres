"""
-> A estrutura if executa o bloco de codigo se dada condição for True
-> A estrutura else deve ser sempre atrelada a um if e executa o bloco de codigo caso a condição de if for False
-> a estrutura elif possibilita avaliar uma condição diferente

"""
devo_continuar = True

# definição if e else
if devo_continuar:
    print("Continuando")
else:
    print("Nao continua")


# definição de elif
if devo_continuar:
    print("Continuando")
elif devo_continuar != 0:
    print("Eh diferente de zero")
else:
    print("Nao continua")
