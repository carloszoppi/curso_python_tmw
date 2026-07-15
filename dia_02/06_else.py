# %%

idade = 18

if idade >= 18:
    print("Você pode beber cerveja")
    print("Beba com moderação")

else:
    print("Você não pode beber cerveja")
    print("Vá para casa beber leite")

# A importância em colocar else ao invés de outro if
# é que o código é otimizado.
# com dois if o código roda os dois sem necessidade
# já que ele já sabia que a primeira
# condição estava aceita. Ou seja, o código 
# precisa utilizar o dobro de processamento se não 
# tiver o else.
# Se a primeira condição já é aceita o python
# pula tudo a partir do else.