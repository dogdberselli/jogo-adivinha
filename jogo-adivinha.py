import random

# Menu principal
def menu():
    print('Seja bem vindo ao jogo do adivinha!')
    maximo = int(input('Escolha qual o limite de números você quer? Conforme maior, mais difícil vai ser adivinhar! '))
    adivinha = int(input('Qual é seu chute? '))
    tentativas = int(input('Quantas tentativas você gostaria de dar? '))
    return maximo, adivinha, tentativas

# Jogo de adivinha, importando o random e pegando como base informações do usuário
def jogo(maximo, adivinha, tentativas):
    numero = random.randrange(maximo)

    while tentativas > 0:
        if adivinha == numero:
            print('Parabéns, você conseguiu acertar o número!')
            break
        else:
            tentativas -=1
            if tentativas > 0:
                print(f'Você errou! você tem mais {tentativas} tentativa(s) restante(s)')
                adivinha = int(input('Insira seu novo chute: '))
            else:
                print(f'Você esgotou todas as tentativas, o número era o {numero}')
    return

# Chamando a função de menu
maximo, adivinha, tentativas = menu()

# Chamando a função de jogo com as informações inseridas no menu
jogo(maximo, adivinha, tentativas)

# Chamando a função se o usuário quiser jogar novamente
while True:
    novamente = int(input('Você gostaria de jogar novamente?\n 1 - Sim\n 2 - Não\n'))
    if novamente == 1:
        maximo, adivinha, tentativas = menu()
        jogo(maximo, adivinha, tentativas)
    elif novamente == 2:
        print('Obrigado por jogar!')
        break # Fim de Jogo
    else:
        print('Você digitou uma opção incorreta')
