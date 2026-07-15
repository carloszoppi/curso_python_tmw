# %%

# Quais numeros são divisíveis por 4
# no intervalor [4-100]?

count = 4
while count <= 100:
    resto = count % 4  #mostra o resto da divisão de count por 4
    if resto == 0:
        print(count)

    count +=1

    