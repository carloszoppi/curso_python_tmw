# Dicioinários são pares de chave-valor, onde 
# cada chave é única e é usada para acessar o valor 
# correspondente. Eles são mutáveis, o que significa 
# que você pode adicionar, remover ou modificar 
# os itens após a criação do dicionário.

# %%
dados_teo = {
    "nome": "Teo",
    "sobrenome": "Silva",
    "idade": 30,
    "cidade": "São Paulo"
}
print(dados_teo["idade"])

# %%
cidade = ["indaituba", "são paulo", "rio de janeiro"]
print(cidade[1])

# %%
cidade = {
    "cidade1": "indaituba",
    "cidade2": "são paulo",
    "cidade3": "rio de janeiro",
    "bairros": ["centro", "jardim", "vila"]
}
print(cidade["cidade2"])
print(cidade["bairros"][1])
print(cidade["bairros"][-1])

# %%
dados_teo["profissão"] = "Engenheiro"
print(dados_teo)
# adicionou a profissão ao dicionário

# %%
cidade = {
    "cidade1": "indaituba",
    "cidade2": "são paulo",
    "cidade3": "rio de janeiro",
    "bairros": ["centro", "jardim", "vila"],
    "população": [{"cidade1": 100000}, {"cidade2": 120000}, {"cidade3": 80000}]
}

cidade["população"][1]

# %%
cidade["CEP"] = ["12345-678", "98765-432", "54321-098"]
print(cidade)


# %%
cidade.keys()  # Retorna as chaves do dicionário
cidade.values()  # Retorna os valores do dicionário

print("chaves:", cidade.keys())
print("valores:", cidade.values())
# %%
cidade.items()  # Retorna os pares chave-valor do dicionário
print("itens:", cidade.items())


# %%

