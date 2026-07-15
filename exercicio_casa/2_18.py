# Escreva um programa que solicite ao usuário frases.
# Para parar de solicitar frases, ele pode apenas apertar
# enter sem digitar nada. O programa deve apresentar cada frase
# e quantas vezes a frase foi repetida.

#para contar quantas vezes a frase foi repetida, podemos usar um dicionário, onde a chave é a frase e o valor é a contagem de vezes que a frase foi digitada.
dados = {}  #dicionário para armazenar as frases e suas contagens
            #ele inicia vazio, e a cada nova frase digitada, ele vai ser atualizado com a contagem de vezes que a frase foi repetida. Se a frase já existir no dicionário, a contagem será incrementada em 1. Caso contrário, a frase será adicionada ao dicionário com uma contagem inicial de 1.

while True:
    frase = input("Digite uma frase (ou aperte enter para sair): ").strip()
    if not frase:     #tambem poderia ser if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1  # Adiciona a frase ao dicionário com contagem 1
    else:
        dados[frase] += 1  # Incrementa a contagem da frase existente

# Apresenta as frases e suas contagens
for frase, contagem in dados.items():
    print(f"Frase: {frase} - Repetida {contagem} vez(es)")
 # poderia ser também
 # for i in dados:
    #     print(i, "->", dados[i])

# %%
# Se quiser ordenar a resposta do dicionário por ordem alfabética das frases, podemos usar a função sorted() para ordenar as chaves do dicionário antes de iterar sobre ele. Aqui está um exemplo de como fazer isso:
  #for frase in sorted(dados.keys()):
  #   print(f"Frase: {frase} - Repetida {dados[frase]} vez(es)")

dados = {
    "Olá, mundo!": 3,
    "Python é incrível.": 5,
    "Aprender a programar é divertido.": 2,
    "Python é foda": 10
}

items = list(dados.items())
items.sort()
items

# vai ordenar por ordem alfabética da chave

# Se quiser ordenar por ordem numérica de valor:

items = list(dados.items())
items.sort(key=lambda x:x[-1], reverse=True)

# o x é como se fosse cada elemento do item, ou seja,
# é como se fosse cada tupla. Estamos dizendo que para 
# o item x é para pegar o último valor, que no cado da tupla
# é o segundo valor.

for i,j in items:
    print(i, "-.", j)


# %%
