# Faça um programa que recebe 4 alturas usando um laço
# de repetição e realize a soma dessas alturas


soma = 0   # valor final
qtde_entradas = 4     # contador de entradas

while qtde_entradas > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qtde_entradas  -= 1   # reduz uma entrada

print("Soma das alturas:", soma)
