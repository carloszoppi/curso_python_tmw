# Faça um programa que venda uma garrafa de água:
# Se o cliente quiser água natural será cobrado R$1,50
# Se o cliente quiser água com gás será cobrado R$2,50

# Para escrever uma string nós usamos aspas duplas
# Mas se quiser escrever várias linhas pode 
# utilizar 3 aspas duplas

texto = """
Escolha a ua água para comprar
(1) Água mineral natual
(2) Água mineral com gás
"""
opcao = input(texto)

if opcao == "1":
    print("Sua conta deu: R$ 1,50)")

elif opcao == "2":
    print("Sua conta deu R$2,50")

# se não utilizar o elif e for direto para o else
# o usuário pode responder qualquer coisa
# e o python vai retornar sempre sua conta deu R$2,50

else:
    print("Entre com a opção correta")

# %%

# Outra forma de escrever este código

texto = """
Escolha a ua água para comprar
(1) Água mineral natual
(2) Água mineral com gás
"""
opcao = input(texto)

conta = 0   # declaração da variável com valor zero
if opcao == "1":
    conta = 1.5

elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Entre com a opção correta")
else:
    print("Sua conta é: R$", conta)

