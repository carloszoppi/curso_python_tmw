# DICA: Comando crt+d seleciona
# Se quiser pode usar seta para baixo e marcar
# os demais.
# Depois pode se quiser deletar e substituir o
# texto ou variável.

# %%

# Escreva a tabuada do 2 até 100
numero = 2
count = 1    # count não é função, é variável. É comum usar o count ou o i para contador 
while count <= 100:
    print(numero, "X", count, "=", numero * count)
    count = count + 1 # pode escrever count +=1  que o resultado é o mesmo

print("Acabou!")  # tem que estar fora do while senão ele
                 # vai aparecer em todas as linhas do resultado