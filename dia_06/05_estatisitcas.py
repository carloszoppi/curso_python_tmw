
# definir uma função de soma

def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a,b) / 2    # uma função dentro de função

a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))

print("Média: ", media(a,b))


# Outra forma de fazer isso para deixar a possibilidade
# da função rodar com mais valores

def soma(a:float, b:float, *args)->float: # args é uma convensão, poderia ser qualquer nome
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args) ->float:
    return soma(a,b, *args) / len(args)+2

a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))
c= float(input("entre com o valor de c: "))
d= float(input("entre com o valor de d: "))

# os valores de "c" e "d" são capturados pelo args.
# a vantagem aparentemente é que não preciso alterar o código
# da função, apenas o código da entrada. Posso acrescentar
# quantas entradas eu quiser.

print("Média: ", media(a,b,c,d))



