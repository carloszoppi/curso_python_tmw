# Faça um programa que receba um número inteiro
# e calcule a sua raiz quadrada e exiba o resultado

numero = input("Entre com o número inteiro: ")
numero = int(numero)

raiz = numero ** (1/2) # ou seja, número elevado a meio
raiz = round(raiz, 4)
print("Raiz quadrada de", numero, "é:", raiz)

