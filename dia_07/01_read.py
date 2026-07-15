
# %%
nome_arquivo = "historia.txt"

open_file = open(nome_arquivo)
# %%
print(open_file)

# %%
# Não está rodando porque o arquivo não está na mesma pasta que o script
# Pra confirmar que o arquivo não está na mesma pasta que o script, podemos usar a biblioteca os para ver qual é a pasta atual.
import os
print("Pasta atual:", os.getcwd())

# %%
# Caminho relativo (subindo uma pasta e entrando em dia_07)
# ele serve para quando a gente quer abrir um arquivo que está em outra pasta, mas que está dentro do mesmo projeto.

nome_arquivo = "../dia_07/historia.txt"

with open(nome_arquivo, "r", encoding="utf-8") as open_file:
    conteudo = open_file.read()
    print(conteudo)

# %%
# PAra mudar de pasta, podemos usar a função os.chdir() para mudar a pasta atual do script.
import os
print("Pasta atual:", os.getcwd())
# %%
import os

# Mudar para a pasta dia_07
os.chdir("../dia_07")

print("Nova pasta atual:", os.getcwd())
# %%
# Caminho relativo (subindo uma pasta e entrando em dia_07)

# %%
nome_arquivo = "historia.txt"

# Abre arquivo em forma de leitura
open_file = open("historia.txt")

# agora está funconando, mas não abre o conteúdo do arquivo, porque não estamos lendo o conteúdo do arquivo, estamos apenas abrindo o arquivo.

# %%

# Lê o conteúdo do arquivo e armazena na variável conteudo
conteudo = open_file.read()

# open_file é um objeto do tipo TextIOWrapper, que é um objeto que representa um arquivo aberto em modo de leitura. O método .read() lê o conteúdo do arquivo e retorna uma string com o conteúdo do arquivo.
# como estamos usando o read, ele retorna um objeto .read 
# .read é uma função que lê o conteúdo do arquivo e retorna uma string com o conteúdo do arquivo.

print(conteudo)

# %%

# Fecha o arquivo
open_file.close()

# É importante fechar o arquivo depois de abrir, porque se não fechar, o arquivo fica aberto e pode causar problemas no sistema operacional. 
# Além disso, se o arquivo estiver aberto, não podemos abrir outro arquivo com o mesmo nome.
# Pode corromper o arquivo, porque o sistema operacional não consegue gerenciar dois arquivos com o mesmo nome abertos ao mesmo tempo.
# Para garantir que o arquivo foi fechado, podemos usar a função os.path.isfile() para verificar se o arquivo ainda está aberto.


# %% 

# Como nós podemos esquecer de fechar o arquivo, 
# a forma acima não é a melhor estrutura para se utilizar.
# A melhor forma de abrir um arquivo é usando o with, que garante que o arquivo será fechado automaticamente depois de ser usado.

nome_arquivo = "historia.txt"

with open(nome_arquivo, "r", encoding="utf-8") as open_file:  # o "r" é de read, que é o modo de abrir o arquivo para leitura. O "w" é de write, que é o modo de abrir o arquivo para escrita. O "a" é de append, que é o modo de abrir o arquivo para adicionar conteúdo no final do arquivo.
    conteudo = open_file.read()
    # o whith abre o arquivo e então é possível atribuir o conteúdo do arquivo a uma variável, e depois fecha o arquivo automaticamente.
# nós atribuimos o conteúdo do arquivo a variável  open_file e processa os dados em conteudo, e depois fechamos o arquivo automaticamente, sem precisar usar o open_file.close().
# em .read o conteúdo do arquivo é lido e armazenado na variável conteudo, que é uma string com o conteúdo do arquivo.
print(conteudo)


# %%
