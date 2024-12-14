"""
expressoes lambdas == funcoes anonimas

-> Na definição de uma expressao lambda utiliza se a palavra reservada lambda arg : return
-> a mesma deve ser atribuida a uma variavel para ser executada ou manipulada
"""

# definicao
variavel = lambda : print("ola")

# chamada de função
variavel()

# lambda com argumentos
eleva_ao_quadrado = lambda x : print(x** 2)

eleva_ao_quadrado(2)

soma_dois = lambda a, b : print(a + b)

soma_dois(5, 5)

retorna_impar_par = lambda x : print("par") if x % 2 == 0 else print("impar")

retorna_impar_par(2)