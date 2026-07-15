# %%
# Uma lista é uma coleção de itens ordenada e mutável. 
# Ela é definida usando colchetes [] e os itens são separados por vírgulas.
idade = [25, 30, 35, 40]
print(idade)

# listas não são arrays, mas podem conter diferentes tipos de dados
# as listas podem carregar o mesmo tipo de elementos,
# mas não se rotula listas como arrays, pois elas são mais flexíveis e podem conter diferentes tipos de dados
# Ex. não se fala lista de inteiros, mas sim lista de números ou lista de objetos

# listas são mutáveis, ou seja, podemos alterar seus elementos após a criação

# Listas podem ser comparadas a um molho de chaves:
# cada chave está em uma posição e cada uma abre um porta diferente.
Teo = ["Teo", 25, "Engenheiro", "São Paulo"]

# %%
# Acessando elementos da lista
Teo = ["Teo", 25, "Engenheiro", "São Paulo"]
print(Teo[0])  # Acessa o primeiro elemento da lista
print(Teo[1])  # Acessa o segundo elemento da lista
print(Teo[2])  # Acessa o terceiro elemento da lista
print(Teo[3])  # Acessa o quarto elemento da lista
# Tem que acessar cada elemento individualmente, não tem 
# como acessar a lista inteira de uma vez só

#O índice começa em 0, então o primeiro elemento da lista é acessado com o índice 0, o segundo elemento com o índice 1, e assim por diante.


# %%
idade = [25, 30, 35, 40]
# A lista possui algumas propriedades e métodos que podem ser usados para manipular os dados.
print(len(idade))  # Retorna o número de elementos na lista
print(sum(idade))  # Retorna a soma dos elementos da lista
print(max(idade))  # Retorna o maior elemento da lista
print(min(idade))  # Retorna o menor elemento da lista
print(sorted(idade))  # Retorna uma nova lista com os elementos ordenados
# não há média, mas podemos calcular a média usando a função sum() e len()
media = sum(idade) / len(idade)

print("Idade máxima:", max(idade))
print("Idade mínima:", min(idade))
print("Média das idades:", media)

# o valor não fica armazenado na lista, mas sim em uma variável separada, 
# pois a média é um valor calculado a partir dos elementos da lista, e não um elemento da lista em si.

# pode procurar na internet as funções padrão do python

# %%
teo = ["Teo Calvo", 32,
       True, "Casado",
       ["Ana","Maria","Claudia"]]

print("Tamanho de Teo: ", len(teo))

print(teo[4][0]) #qual a primeira namorada de Teo

#pode ser escrito como abaixo também, o resultado é o mesmo

exs = teo[4]
primeira_ex = exs[0]
print(primeira_ex)


# %%

# se eu quiser acessar o último elemento da lista
tamanho = len(teo)  #fornece o tamanho da lista
pos = tamanho - 1 # isso porque a posição no python começa no zero e não no um
teo[pos]  #vai mostrar qual é o último elemento da lista
teo[pos][0]


# %%
# para saber o tamanho da lista exnamoradas
teo = ["Teo Calvo", 32,
       True, "Casado",
       ["Ana","Maria","Claudia"]]


tamanho = len(teo)
pos = tamanho-1
exs = teo[pos]

teo[pos][len(exs)-1]



# %%
# ou seja, o -1 é o último elemento da lista

teo[-1]

# %%
teo[-1][-1]
# acessa o último elemento da lista dentro da lista

# %%
teo[-1][-2]
#Acessa a penúltima

# %%
# Para pegar os 4 primeiros elementos da lista

teo[0:4] # como o phyton considera o intervalo aberto, tem que 
         # considerar o 4

# %%
teo = ["Teo Calvo", 
       32,
       True, 
       "Casado",
       ["estagiario", "jr", "pl", "sr", "head"],
       ["Ana","Maria","Claudia"]]

teo[4][3:5]

teo[4][-2:]  # quando acaba nos 2 pontos eu vou até o final da lista
teo[4][:4]   # quando começa com 2 pontos significa que é o começo da lista

# teo[ start : stop] 

#%%

teo = ["Teo Calvo", 
       32,
       True, 
       "Casado",
       ["estagiario", "jr", "pl", "sr", "head"],
       [1000, 2000, 5000, 7500, 10000],
       ["Ana","Maria","Claudia"]]

salario = teo[5]
salario[::-1] # executa a lista na ordem inversa

# teo[ start : stop : step]
# O step pode definir ordem ou o passo de quantos em quantos avança




# %%
