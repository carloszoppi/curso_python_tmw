# inclua a quantidade de água no problema anterior

texto = """
Escolha a sua água para comprar
(1) Água mineral natual - R$ 1.50
(2) Água mineral com gás - R$ 2.50
"""
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a opção correta")
else:
    qtde = input("Quantas garrafas: ")
    qtde = int(qtde)
    print("valor do item", valor_item)
    print("quantidade", qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu ", valor_total)
