# %%

nome = "Carlos Zoppi"

for letra in nome:    # A letra está percorrendo cada elemento do nome
    print(letra)

# o for vai percorrer os elementos de um objeto.

# %%
nome = "Carlos Zoppi"

for i in nome:    # A letra está percorrendo cada elemento do nome
    print(i)

# se substituir letra por i não altera nada

# %%

# brincadeira da tabuada

numero = 2
max_numero = 100

for i in range(1, max_numero+1):  # range é uma estrutura do python que cria uma 
                    # sequência do numero inicial até o final
# como o range trabalha com step, ou seja, intervalo aberto,
# ele não considera o último valor que seria 100.
    print(numero, "x", i, "=", numero *i)


# %%

# Quais números são divisíveis por 4 no intervalo
# [4-100] ?

for i in range(4,101):
    if i % 4  == 0:
        print(i)

        
# %%

