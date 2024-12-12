# Seção 2 - Introdução a linguagem Python

## SEÇÃO 2

### PEP8 - Boas Praticas

**Conhecendo o IDE** 

**Conhecendo o ester-egg**

Ao digitar no console python 

```python
import this
```

É gerado um  ester-egg com o poema  “The Zen of Python, by Tim Peters”

***The Zen of Python, by Tim Peters***

> Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aninhado.
Esparso é melhor que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que seja explicitamente silenciado.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deveria haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa forma possa não ser óbvia à primeira vista, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja melhor do que *agora*.
Se a implementação for difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia - vamos fazer mais deles! ”
> 

PEP 0 – Index of Python Enhancement Proposals (PEPs)

Propostas de aprimoramento do Python

Referencia → [PEP 0 – Index of Python Enhancement Proposals (PEPs) | peps.python.org](https://peps.python.org/)

**Conhecendo a PEP 8**

Propostas de melhorias para linguagem python

A ideia dessa PEP é escrever codigos python de forma “Pythonica”

1- Utilize camel case para nomes de classes - CamelCase

2- Utilize nomes em minusculo separados por underline para funções e variaveis - snake_case

3 - Utilize 4 espaços para identação

4 - Utilizar 2 linhas em branco para separar definição de função e definição de classe

5 - metodos dentro de uma classe devem ser separados em uma linha em branco

6 - imports devem sempre ser feitos em linhas separadas

Caso haja mais de um pacote no import deve ser feito da seguinte forma.

```python
from types import (
    StringType,
    ListType,
    SetType
)
```

Imports devem ser colocados no topo do arquivo após quais quer comentarios ou docstrings

E antes de constantes e variaveis globais

7- Não utilizar espaços em expressões e instruções

8 - Terminar instrução com uma nova linha

### Dir e Help

**Definição**

Utilitarios python para auxiliar na programação

dir(tipo_dado / variavel) → mostra todos os atributos, metodos disponiveis para determinado tipo de dado ou variavel

```python
print(dir("geek"))
```

help() → apresenta documentação / como utilizar atributos / propriedades e funções / metodos disponiveis para determinado tipo de dado ou variavel

```python
print(help('geek'.lower))
```

### Recebendo dados de usuarios

input() → 

builtins → Recursos integrados da linguagem

Casting → conversao de dado para outro tipo

OBS: Todo dado recebido via input é uma string