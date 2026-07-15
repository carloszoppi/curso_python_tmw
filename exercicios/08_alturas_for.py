# Faça um programa que recebe 4 alturas usando um laço
# de repetição e realize a soma dessas alturas

# %%

soma = 0   # valor final
qtde_entradas = 4     # contador de entradas

for i in range(qtde_entradas): # range(0,qtde_entradas) ele está pegando 0,1,2,3 não entra o 4
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas:", soma)
