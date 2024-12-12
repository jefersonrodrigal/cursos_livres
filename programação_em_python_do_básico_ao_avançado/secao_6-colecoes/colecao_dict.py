# Definição
dicionario = {}

# Exemplo
paises = {'br':'Brasil', 'eua': 'Estados unidos', 'py': 'PAraguai'}

# Exemplo de outra definição
pais = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

# Acessando elementos via chave
print(paises['br'])

# Acessando elementos via get
print(paises.get('br'))

# Metodo get com dois parametros - Valor padrão
print(paises.get('ru', 'Não encontrado'))

# Verificando se existe determinada chave no dicionario
print('ru' in paises)

# Adicionar elementos
receita = {'Janeiro': 200.00, 'Fevereiro': 300.00}
receita['Março'] = 800.00
print(receita)

novo_dado = {'Abril': 1000.00}
receita.update(novo_dado)
print(receita)

# Atualizar dados
receita['Abril'] = 550.00
print(receita)

receita.update({'Abril': 650.00})
print(receita)

# Remover dados com o metodo pop - ao remover um objeto o valor vinculado a chave é retornado.
receita.pop('Janeiro')
print(receita)

# Se a chave não existir, será gerado uma exceção KeyError
del(receita['Março'])
print(receita)

# Outros metodos
dias_semana = {1: 'Segunda', 2:'Terça', 3: 'Quarta'}

# copiar um dicionario para outro
novo = dias_semana.copy()
dias_semana[4] ='Quinta'
print(dias_semana)
print(novo)

# Limpar dados
dias_semana.clear()
print(dias_semana)

# Possibilita criar chaves a partir de uma lista e atribuir a elas o valor que é passado como segundo parametro.
usuario = {}.fromkeys(['nome','sobrenome', 'email', 'profile'], 'desconhecido')
print(usuario)

# Iterando em dicionarios
for key in receita:
    print(key)

for key in receita:
    print(receita[key])

# Acessar todas as chaves -> retorna uma lista com a chaves do dicionario
print(receita.keys())

# Modo mais usual de acessar valor de chave em dicionario.
for key in receita.keys():
    print(receita[key])

# Acessar os valores do dicionario
print(receita.values())

# Fazer acesso a os valores por iteração
for value in receita.values():
    print(value)

# Desempacotamento de dicionario - o metodo .items retorna  uma lista de tuplas contendo chave e valor
print(receita.items())

for key, value in receita.items():
    print(f'chave= {key} e valor= {value}')

# Retornando soma, min, max e o tamanho
print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))