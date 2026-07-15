# %%

arquivo = "data.csv"

with open(arquivo)as open_file:
    conteudo = open_file.read()
    
print(conteudo)

# o resultado do print quando se usa .read é uma string com o conteúdo do arquivo, mas sem a formatação de tabela, porque o .read lê o conteúdo do arquivo como uma string, e não como uma tabela.

# %%

# Outra forma é utilizar o .readlines() que lê o conteúdo do arquivo e retorna uma lista com cada linha do arquivo como um elemento da lista.

with open(arquivo)as open_file:
    conteudo = open_file.readlines()

print(conteudo)

# %%

with open(arquivo)as open_file:
    conteudo = open_file.readlines()

for linha in conteudo:
    print(linha)

# cada linha do arquivo é um elemento da lista, e o print vai imprimir cada elemento da lista em uma linha diferente.

#  %%

# Posso criar um dicionário com o conteúdo do arquivo, onde a chave é o nome da coluna e o valor é uma lista com os valores da coluna.

with open(arquivo)as open_file:
    conteudo = open_file.readlines()

for linha in conteudo:
    linha = linha.strip() # remove os espaços em branco no início e no final da linha
    linha = linha.split(",") # separa a linha em uma lista de valores, usando a vírgula como separador
    print(linha) # imprime a lista de valores da linha


# %%

# Criar um dicionário com o conteúdo do arquivo, onde a chave é o nome da coluna e o valor é uma lista com os valores da coluna.
with open(arquivo)as open_file:
    conteudo = open_file.readlines()

for linha in conteudo:
    print(linha)

chaves = conteudo[0]
chaves
# tem que tirar o \n do final da linha, senão vai dar erro na hora de criar o dicionário

chaves = conteudo[0].strip("\n").split(";") # remove os espaços em branco no início e no final da linha
# split separa a linha em uma lista de valores, usando o ponto e vírgula como separador
# ou seja, ele vai separa onde ele encontra o tipo de separador que a gente definiu, que no caso é o ponto e vírgula.



# %%
# criar um dicionário com todas as chaves

dados = dict()

chaves = conteudo[0].strip("\n").split(";")
for c in chaves:
    dados[c] = [] # cria uma lista vazia para cada chave do dicionário

dados 

# Primeiro nós criamos um dicionário vazio, 
# depois nós pegamos a primeira linha do arquivo, que contém os nomes das colunas,
# ou seja, o cabeçalho,  então percorremos cada um deles e criamos uma chave no dicionário com o nome da coluna, e atribuímos a ela uma lista vazia, que vai receber os valores da coluna.

# %%
# Agora precisamos alimentar o dicionário com os valores das colunas, que estão nas linhas seguintes do arquivo.
# Até agora só usamos o cabeçalho posição [0], que é a primeira linha do arquivo, mas agora precisamos percorrer as linhas seguintes do arquivo, que são os valores das colunas.

for data in conteudo[1:]: # percorre todas as linhas do arquivo, começando da segunda linha, que são os valores das colunas
    data = data.strip("\n").split(";") # para cada linha, começando com a [1] remove os espaços em branco no início e no final da linha + o separador de linhas e separa a linha em uma lista de valores, usando o ponto e vírgula como separador (o csv está divido em ;)
    for i in range(len(chaves)): # percorre as chaves do dicionário que até aqui estão vazias, e para cada chave do dicionário, adiciona o valor correspondente da coluna na lista da chave do dicionário.
                                 # percorre a quantidade de valores da linha, que é igual a quantidade de chaves do dicionário, e para cada valor da linha, adiciona o valor na lista correspondente à chave do dicionário.
                                 # o i começa com valor zero e vai até o tamanho da lista de chaves, que é igual ao tamanho da lista de valores da linha, e para cada valor da linha, adiciona o valor na lista correspondente à chave do dicionário. Neste caso o valor vai de [0] a [2], porque temos 3 colunas no arquivo csv.
        dados[chaves[i]].append(data[i]) # adiciona o valor da coluna na lista correspondente à chave do dicionário
                                         # está falando: dados nesta posição i que começa com zero, que é a primeira chave do dicionário, que é a primeira coluna do arquivo csv, adiciona o valor da primeira coluna da linha atual, que é a posição i da lista de valores da linha atual. E assim por diante para as outras colunas.
                                         # ou seja, [chaves[i] ou chave na posição zero é o nome. Dados no nome é uma lista que vai fazer um append do nome da primeira linha, e assim por diante. Chave na posição 1 é idade, valor na posição 1 na primeira linha é 32 anos, etc. 
dados   
# %%
# Veja que a idade aparece como string no dicionário, porque o csv é um arquivo de texto, e tudo que está no arquivo de texto é lido como string. Se quisermos que a idade seja um número inteiro, precisamos converter a string para inteiro usando a função int().

idades = []
for idade in dados["idade"]:
    idades.append(int(idade)) # converte a string para inteiro e adiciona na lista idades

# %%

# calcular a média

media = sum(idades) / len(idades) # soma todos os valores da lista idades e divide pelo tamanho da lista idades, que é a quantidade de elementos na lista idades
media
# %%
