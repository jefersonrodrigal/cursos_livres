"""
-> A palavra reservada continue em qualquer laço de repetição passa para a proxima iteração do laço ao ser executada
"""

for num in range(10):
    if num % 2 == 0:
        print(f"{num} é par")
        continue
    print("O num não é par")