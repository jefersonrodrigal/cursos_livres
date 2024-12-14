"""
O bloco try / except ->
-> É possivel ter except encadeados
-> raise lança uma exceção
-> finaly executa o codigo independentemente se houver erro ou não
-> else Só é executado se não der erro
"""

# Implementacao try except
try:
    pass
except ZeroDivisionError as erro:
    pass


# Implementacao except encadeado
try:
    pass
except ValueError as error:
    pass
except ZeroDivisionError as erro:
    pass


# Implementação raise
try:
    raise NameError("Sou um erro")
except NameError as error:
    print(erro)


# Implementação finaly
try:
    pass
except ValueError as error:
    pass
except ZeroDivisionError as erro:
    pass
finally:
    pass

# implementação com else
try:
    pass
except ValueError as error:
    pass
except ZeroDivisionError as erro:
    pass
else:
    pass