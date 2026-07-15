# Construa um programa que realiza sozinho o sorteio de um número de 1 a 15, ´
# O usuário terá 3 chances de acertar o número sorteado.
# A cada tentativa, o programa deve informar se o número digitado é maior ou menor que o número sorteado.
# Caso o usuário acerte o número, o programa deve informar que ele acertou e encerrar.

# é o mesmo exercício, apenas aplicando o conceito de função e 
# deixando o código mais organizado e legível.

# para gerar um número aleatório, podemos usar a biblioteca random, que já vem instalada no Python.
import random

# a validação do número do usuário passa a ser uma função separada, que retorna o número digitado pelo usuário, caso seja válido.
def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um número de 1 a 15: "))
            if not 1 <= numero_usuario <= 15:
                print("Número inválido. Digite um número de 1 a 15.")
                continue
            return numero_usuario
        except ValueError as error:
            print("Entrada inválida. Digite um número inteiro.")


numero_sorteado = random.randint(1, 15) # gera um número aleatório entre 1 e 15

for i in range(3):

    numero_usuario = get_input()
        

    if numero_usuario == numero_sorteado:
        print("Parabéns! Você acertou o número sorteado!")
        break # precisa do break para encerrar o loop, caso contrário, ele vai continuar pedindo o número mesmo que o usuário tenha acertado.

    elif numero_usuario > numero_sorteado:
        print("O número digitado é maior que o número sorteado. Tente novamente.")

    else:
        print("O número digitado é menor que o número sorteado. Tente novamente.")

else:  #existe um else no for, que é executado quando o loop termina sem o break, ou seja, quando o usuário não acertou o número sorteado.
    print("Suas chances acabaram. O número sorteado era:", numero_sorteado)

