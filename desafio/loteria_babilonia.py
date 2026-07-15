# Construa um programa que realiza sozinho o sorteio de um número de 1 a 15, ´
# O usuário terá 3 chances de acertar o número sorteado.
# A cada tentativa, o programa deve informar se o número digitado é maior ou menor que o número sorteado.
# Caso o usuário acerte o número, o programa deve informar que ele acertou e encerrar.

numero_sorteado = 7

for i in range(3):

    while True:
        try:
            numero_usuario = int(input("Digite um número de 1 a 15: "))
            if not 1 <= numero_usuario <= 15:
                print("Número inválido. Digite um número de 1 a 15.")
                continue
            break
        except ValueError as error:
            print("Entrada inválida. Digite um número inteiro.")

# da linha 10 a linha 18 é a vaidação do input, que garante que o usuário digite um número inteiro entre 1 e 15. Se o usuário digitar um valor inválido, o programa vai pedir para ele digitar novamente.


    if numero_usuario == numero_sorteado:
        print("Parabéns! Você acertou o número sorteado!")
        break # precisa do break para encerrar o loop, caso contrário, ele vai continuar pedindo o número mesmo que o usuário tenha acertado.

    elif numero_usuario > numero_sorteado:
        print("O número digitado é maior que o número sorteado. Tente novamente.")

    else:
        print("O número digitado é menor que o número sorteado. Tente novamente.")

else:  #existe um else no for, que é executado quando o loop termina sem o break, ou seja, quando o usuário não acertou o número sorteado.
    print("Suas chances acabaram. O número sorteado era:", numero_sorteado)

