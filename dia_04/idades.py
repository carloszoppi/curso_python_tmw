# %%
idades = [25, 30, 35, 40]
print(idade)

# %%
idades.append(32) #adiciona um elemento no final da lista
print(idades)
# %%
idades = [] #cria uma lista vazia

while True:
    idade = input("Entre com a idade: ")
    if idade == "":
        break #maneira forçada de sair do laço while

    idades.append(int(idade))   #transforma para inteiro porque não tem casas decimais
print(idades)
# %%
media = sum(idades) / len(idades)
print("Idade máxima:", max(idades))
print("Média das idades:", media)
# %%
