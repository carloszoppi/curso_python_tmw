# Faça um programa que receba uma quantidade indefinida 
# de valores correspondentes a "saldo em conta",
# mas quando o usuário apertar "enter" sem digitar valor algum
# o programa para de receber valores, e exibe a soma
# de todos os vlores digitados anteriormente.

saldo_total = 0

while True:
    saldo = input("Entre com o saldo: ")
    if saldo == "":
        break #maneira forçada de sair do laço while

    saldo_total += float(saldo)   #transforma para float porque tem casas decimais

print("Saldo Total: ", saldo_total)
