# Seção 6- Coleções

### **Listas - list**

As listas são representadas por colchetes → []

Funcionam como vetores, matrizes, arrays

São dinamicas - mutaveis

Aceitam qualquer tipo de dado

Fazemos o acesso aos elementos de forma indexada

É possivel converter uma lista em uma tupla

A o utilizar a função copy() a lista se dá por uma lista diferente da original

deep_copy

shallow_copy → Copia via atribuição modifica as duas listas , tanto a original quanto a criada a partir da atribuição

Suporta desempacotamento

Obedece a ordem da entrada dos dados

Os metodos sum, max min → só se aplicam a elementos do tipo numericos inteiros

---

### **Tuplas - tuple**

Tuplas são representadas por ()

Na definição o que representa uma tupla é a virgula (quando há um unico elkemento)

São imutaveis

Aceita diferentes tipos de dados

Suporta desempacotamento

Metodos de remoção e adição de elementos nas tuplas. Não existem - append(), remove() e clear()

Tuplas são imutaveis porem podemos sobrescrever seus valores

Podemos acessar elementos por index

Na tupla não existe shallow_copy

Obedece a ordem da entrada dos dados

Pode se dizer que esse tipo de coleção é dada por referencia

Os metodos sum, max min → só se aplicam a elementos do tipo numericos inteiros

---

### **Dicionarios - dict**

São coleções do tipo chave : valor

São representados por {}

Chave e valor, podem ser de qualquer tipo de dado

Chave e valor são separados por :

Podemos misturar tipos de dados

Dicionarios não são indexados

Em caso de acesso a uma chave inexistente é levantado a exceção KeyError

Utilizando o metodo get() para acessar um elemento, caso a chave não exista retorna None

A forma de incluir elementos e atualizar elementos em um dicionario é a mesma.

Não aceitam chaves duplicadas

É possivel iterar sobre dicionarios

Obedece a ordem da entrada dos dados

**observação:**

 None →  conhecido como um tipo sem tipo → NoneType

O tipo None sempre será falso

Os metodos sum, max min → só se aplicam a elementos do tipo numericos inteiros

---

### **Conjuntos - set**

Não possuem elementos duplicados - duplicidade não gera erro

Não ordena elementos

Elementos não são acessados pelo indice (Não são indexados)

Ao criar um conjunto com valores duplicados as duplicidades  serão ignoradas e não farão parte do conjunto

É possivel converter uma string para um set

É possivel converter uma lista para um set

É possivel converter uma tupla para um set

Aceitam variados tipos de dados

São mutaveis

Ao tentar remover um valor que não existe será gerado o erro KeyError

Pode se dizer que esse tipo de coleção é dada por referencia

**observação**

deep_copy = cria dois objetos independentes

shallow_copy = o objeto copiado é dependente do objeto original e vice versa

Os metodos sum, max min → só se aplicam a elementos do tipo numericos inteiros

---

### **Modulo Collection Counter**

Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter parecido com um dicionario

contendo como chave o elemento da lista passada como parametro e como valor a quantidade

de ocorrencias desse eleemnto

Para cada elemento da lista é criado uma chave e colocou e inseriu como valor a quantidade de ocorrencias

---

### **Default Dict**

Tudo que existe em um dict vale para default dict

Na criação de um dicionario é informado o valor default podendo utilizar um lambda

Esse valor será utilizado sempre que não houver um valor definido 

Caso tentemos acessar uma chave que não existe. Será criada com o valor default definido 

---

### Ordered dict

É uma estrutura do tipo dict que leva em consideração a ordem dos elementos

---

### Named Tuple

São tuplas diferenciadas onde especifica-se nome e parametros

A partir do que se cria um namedtuple é criado um tipo de dado personalizado.

É possivel acessar as propreidades por notação de ponto

---

### Deque

São listas de alta performance

É possivel adicionar elementos no fim ou no começo da lista criada - utilizando o metodo appendleft()