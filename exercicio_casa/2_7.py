# peça para o usuário entrar com o nome de uma fruta
# e responda com o valor da fruta

fruta = input("Entre com o nome da fruta: ").strip().capitalize()  # Remove espaços em branco e capitaliza a primeira letra

frutas = {
    "Pera": "R$ 2,00",
    "Maçã": "R$ 3,00",
    "Uva": "R$ 4,00",
    "Limão": "R$ 1,50"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Fruta não encontrada")
