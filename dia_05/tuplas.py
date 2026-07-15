# %%

dados_teo = [32, 1, "Casado", "dev goLang"]

dados_teo
print(dados_teo[0])  # Acessando o primeiro elemento da lista

# %%

dados_teo.append("3241,43")  # Adicionando um novo elemento à lista
dados_teo


# %%

# tuppl_teo = 32, 1, "Casado", "dev goLang"
# é o mesmo que:
tupla_teo = (32, 1, "Casado", "dev goLang")
print(tupla_teo)

print(type(tupla_teo))  # Verificando o tipo da variável

# %%
tupla_teo #é um objeto do tipo tupla, que é imutável, ou seja, não pode ser alterada após a criação.
            # tupla é imutável. É um objeto que não suporta assinatura de itens, ou seja, não é possível adicionar, remover ou modificar os itens após a criação da tupla.
            # tupla não possui metodos como append, remove ou pop, que são comuns em listas. Isso ocorre porque as tuplas são imutáveis e não permitem alterações após a criação.
            # Em vez disso, as tuplas são usadas para armazenar dados que não devem ser alterados, como coordenadas geográficas, datas ou outras informações que precisam permanecer constantes ao longo do tempo.

# Agora, se eu tenho dentro da tupla um elemento mutável, como uma lista, eu posso alterar os itens dessa lista, mesmo que a tupla em si seja imutável. Isso ocorre porque a imutabilidade da tupla se aplica apenas à estrutura da tupla, não aos objetos mutáveis que ela contém.
tupla_teo = (32, 1, "Casado", "dev goLang", [1, 2, 3])
tupla_teo[-1].append(4)  # Adicionando um elemento à lista dentro da tupla
print(tupla_teo)  # A tupla em si permanece imutável, mas a lista dentro dela foi modificada


# %%

# não dá para atribuir outro valor. Dá erro. Por exemplo:
tupla_teo[-1] = [4, 5, 6]  # Tentando atribuir um novo valor à posição -1 da tupla
# Isso resultará em um erro do tipo TypeError, indicando que a tupla não suporta atribuição de itens, ou seja, não é possível modificar os elementos da tupla após a sua criação.


# %%
