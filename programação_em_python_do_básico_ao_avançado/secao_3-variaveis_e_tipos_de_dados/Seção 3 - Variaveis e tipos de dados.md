# Seção 3 - Variaveis e tipos de dados

### Tipo numerico

**Operadores aritimeticos**

Adicição ————→ +

Subtração  ————→ -

Divisão ————→ /

Divisão inteira ————→ //

Modulo ————→ %

Exponenciação ————→ **

**Incremento**

+= Incrementa 

-= decremeta

**A função type**

type(variavel) → Retorna o tipo de dado da variavel

### Tipo float

Tipo real , decimal

Possui casas decimais

O separador é o ponto , não a virgula

Ao converter float para inteiros, perde se precisão

### Tipo booleano

Representado pelos valores True  e False 

True = Verdadeiro

False = Falso

**comparação logica**

not →  Inverte a o retorno da expressão logica

or →  Um dos dois valores da comparação deve ser verdadeiro para a expressão retornar verdadeiro

and → Os dois valores da comparação devem ser verdadeiros para a expressão retornar verdadeiro

**operadores de comparação**

maior que >

igual a <

maior ou igual a ≥

menor ou igual a ≤

igua a ==

### Tipo string

Em Python um dado é considerado do tipo string sempre que estiver entre 

Aspas simples → uso mais comum

Aspas duplas 

Aspas simples triplas

Aspas duplas triplas

**observações**

\n → salta uma linha

\ → caractere de escape

**Metodos usuarios**

upper()

→ Explicação

O objeto chama a função e essa função através da notação de ponto trabalha em cima do objeto que a chamou e retorna uma copia da string convertida em caixa alta

split()

→ Explicação:

O objeto chama a função e essa função através da notação de pontotrabalha em cima do objeto que a chamou  e retorna uma lista de strings

strip()

→ Explicação

Remove espaços em branco contidos no inicio e no fim de qualquer string

**Fatiamento de strings(slice de string)**

Como strings são objetos indexados é possivel fazer o acesso pelo seu indice

Utilizando slicing é possivel inverter uma string facilmente conforme abaixo

```python
palavra[::-1]
```

### Escopo de variaveis

Escopo → Limitação de algo

variaveis global → Seu escopo compreende a todo o programa

variaveis local → Seu escopo compreende ao bloco onde foi declarada

OBS: Python por ser uma linguagem dinamica, não é necessario na declaração de uma variavel definir o seu tipo. O interpretador Python é capaz de inferir o tipo da variavel no momento de sua atribuição.

Caso acesse uma variavel inexistente o interpretador python retorna uma exceção do tipo NameError