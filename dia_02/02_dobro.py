numero = input("Entre com o númeero para encontrar o seu dobro: ")

dobro = numero * 2

print("O dobro de", numero, "é: ", dobro)
# desta forma o número informado será repetido e não multiplicado
# isso acontece porque numero está como string
# é preciso converter esta string para inteiro


numero = input("Entre com o número para encontrar o seu dobro: ")
numero = int(numero)
dobro = numero * 2

print("O dobro de", numero, "é: ", dobro)
# se o usuário escrever dois ao invés de 2 o 
# programa vai apresentar um erro
# é possível travar que evitar erro do usuário
# isso será visto mais tarde no curso