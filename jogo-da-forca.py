from random import choice

palavras = ['python', 'sapato', 'borboleta', 'laranja', 'trator', 'pipoca', 'mulher', 'garoto', 'rapaz', 'jogador', 'bola', 'ovo', 'letra', 'geladeira', 'gol', 'trabalho', 'gerenciamento']
palavra_escolhida = choice(palavras).lower()
letras_usuario = []
chances = 5
ganhou = False

print ('*******************************************')
print ('***************JOGO DA FORCA***************')
print ('*******************************************')

while True:
    for letra in palavra_escolhida:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra_escolhida.lower():
        chances -= 1
    ganhou = True
    for letra in palavra_escolhida:
        if letra.lower() not in letras_usuario:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra_escolhida}")
else:
    print(f"Você perdeu! A palavra era: {palavra_escolhida}")