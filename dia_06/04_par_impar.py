# Criar uma função que diga se o número é par ou ímpar.

# Primeiro define a função 'par_impar'
def par_impar(numero:int):
    if numero % 2 == 0:
        print("É par!")
    else:
        print("É impar!")

# O input não fica dentro da função porque o ideal é que 
# uma função tenha apenas uma funcionalidade, que neste caso é dizer se 
# é par ou impar.
# Se uma função precisar fazer muita coisa, seria melhor 
# dividir estas funcionalidades em várias funções.

# Essa função não retorna nada. Só exibe o print na tela.
# Se o objetivo é armazenar o resultado em algum lugar, então
# seria importante retornar ou seja, usar o return
# caso contrário, se for só para exibir usar print()

# Depois recebe o número do usuário
numero = input("Entre com um número: ")
numero = int(numero)

# Então passa o número dado pelo usuário pela função par_impar.
par_impar(numero)