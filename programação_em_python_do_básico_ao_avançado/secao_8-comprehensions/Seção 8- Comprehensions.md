# Seção 8- Comprehensions

Além de list é possivel utilizar comprehension com  dict  set

### **List Comprehensions**

Utilizando esse recurso é possivel gerar novas listas com dados processados a partir de um iteravel

Sintaxe

```python
variavel = [dado for dado in iteravel]
```

Observação → Para entendimento, ler do final para o começo

É possivel adicionar estruturas condicionais logicas

Sintaxe 

```python
variavel = [dado for dado in iteravel if condicao_true]
```

```python
variavel = [dado processamento condicional_true condicional_false for dado in iteravel]
```