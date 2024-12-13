# Seção 7 - Funções

**Definição de funções**

São pequenos trechos de codigos que realizam tarefas especificas

Pode ou não receber entradas de dados e retornar uma saida de dados

São uteis para executar procedimentos similares por repetidas vezes

Toda função que ja vier integrada na linguagem é chamada de built-in

Principio Dry → Dont Repeat Yourself

Em python, a forma geral de definir uma função é 

Nomenclatura

→ nome de funcao com letra minuscula 

→ caso seja nome composto, separar as palavras por underline - snake_case

→ parametros de entrada são opcionais

→ caso tenha mais de um os mesmos devem ser separados por virgula

→ podendo ser opcionais ou não

Para definir uma função é utilizado a palavra reservada def

É possivel usar funções dentro de uma função

É possivel criar uma variavel que recebe uma  função e executar a função pela variavel.

---

### **Funções com retorno**

Quando uma função não retorna nenhum valor, o retorno é None

Funções python que retornam valores devem retorna-los com a palavra reservada return

Não precisamos necessariamente criar uma variavel para receber o retorno de uma função.

É possivel passar a execução da função para outras funções

Utilizando o return tem se mais flexibilidade para utilizar o resultado da função

Palavra return

→ Finaliza a função → sai da execução da função

→ Em uma função é possivel ter mais de um return

→ É possivel retornar qualquer tipo de dado

→ É possivel retornar uma tupla com varios valores 

### **Funções com parametros**

Funções podem ter n parametros de entrada e são separados por virgula

A ordem dos parametros importam

OBS: Na definição da função a nomeclatura é definida por 'parametro'
     Na chamada da função a nomeclatura é 'argumentos'

### **Funções com parametros padrões**

Funções onde a passagem de parametros seja opcional

Os parametros com valores padrões sempre devem estar no final da função.

Pode ser usado para parametros default qualquer tipo de dado

É possivel passar função como parametro opcional

A variavel local se sobrepóes a variavel global

Fora do seu escopo uma variavel não pode ser acessada, retornando a exceção NameError

É possivel ter funções que são declaradas dentro de funções

observação → evitar variavel global

→ a palavra reservada nomlocal refere-se a  variaveis que estão em uma função fora da função que esteja declarada mais internamente.

---

### Docstrings

Representada por → “”””””

Utilizado para documentar unidades de codigos (metodos, funções e classes)

---

### *args e  **kwargs

*args - tupla

 → É um parametro especial de funções que acopla n parametros de entrada de uma função em uma tupla

O * passado como argumento de uma chamada de função + seu identificador, informa que está sendo passado uma coleção de dados.

observação → Caso haja parametros obrigatorios na função que utiliza *args. Os parametros obrigatorios devem vir primeiro, em seguida utilizar o *args

**kwargs- dicionario

→ Exige que utilizemos argumentos nomeados na chamada da função e dessa forma transforma esses argumentos em um dicionario

Não são parametros obrigatorios

OBS: Os nomes das chaves do dicionario, devem ser os mesmos nomes de argumentos da função.