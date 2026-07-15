
# criar uma função para calcular o imposto de um produto
# preço e valor do imposto são obrigatórios informar.

# %%
def calc_imposto(preco:float, tx_imposto_base: float):
    return preco * tx_imposto_base


# %%

calc_imposto(100, 0.05)


# %%
# se quiser fazer uma função que preveja outros impostos
# tem que usar o **kwargs
# o args a gente pegava um conjunto indefinido de elementos e 
# atribuia tudo isso a args e virava uma tupla ou uma lista
# Quando coloca ** no lugar de ser uma ista isso é um dicionário
# É como se eu tivesse argumentos nomeados na função calc_imposto
# que eu posso adicionar quando vou invocar chave:valor


def calc_imposto(preco:float, tx_imposto_base: float, **kwargs): 
    imposto =  preco * tx_imposto_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

# ele vai correr os novos impostos, calcular e somar ao imposto inicial

    return imposto

# %%
calc_imposto(100, 0.03, municipio = 0.01)

# %%

# posso ir acrescentando os outros impostos sem alterar a função calc_imposto

calc_imposto(100, 0.03, municipio = 0.01, estado = 0.005, ipi = 0.01)

# %%

# Uma outra forma de fazer é criar um dicionário
# para impostos gerais

impostos_gerais = {
    "municipio": 0.01,
    "estadual": 0.005,
    "nacional": 0.001
}





# %%
calc_imposto(100, 0.03, **impostos_gerais)
calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001 ) # é iagual a linha de cima



# %%
