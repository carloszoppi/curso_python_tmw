# %%

texto = "Meu novo Arquivo de Texto"

nome_arquivo = "historia_02.txt"
with open(nome_arquivo, mode="w") as open_file:
    open_file.write(texto)

# o modo "w" de write, que é o modo de abrir o arquivo para escrever conteúdo no arquivo. Desta forma o que já está escrito no arquivo será apagado, e o novo conteúdo será escrito no arquivo.
# por default o modo de abrir o arquivo é "r" de read, que é o modo de abrir o arquivo para ler conteúdo do arquivo. Desta forma o que já está escrito no arquivo não será apagado, e o novo conteúdo será adicionado no final do arquivo.

# %%
# Agora se for para acrescentar mais texto no arquivo, podemos usar o modo "a" de append, que é o modo de abrir o arquivo para adicionar conteúdo no final do arquivo.
# Desta forma o que já está escrito no arquivo não será apagado, e o novo conteúdo será adicionado no final do arquivo.

texto = "Já testei\nAgora vou testar de novo\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(texto)

# o \n no final do texto é para quebrar uma linha, senão o texto vai ficar tudo na mesma linha.



# %%
