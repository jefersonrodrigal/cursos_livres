# Exemplo de função onde a passagem de parametro é opcional
def quadrado(numero=None):
    if numero is None:
        return
    return numero ** 2


print(quadrado())


# Passando função como parametro
def soma(x, y):
    return x + y


def mat(num1, num2, function=soma):
    return function(num1, num2)

# Escopo utilizando variaveis globaix

total = 0

def incrementa():
    global total
    total = total + 1
    return  total

print(incrementa())


# Função dentro de função
def out_side():
    count = 0

    def in_side():
        nonlocal count

        count = count +1
        return count
    return in_side()

print(out_side())