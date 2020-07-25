import random

def jogar():

    imprime_mensagem_abertura()
    nome = input("Qual o seu nome? ")

    dados_palavra_secreta = define_palavra_secreta()
    palavra_secreta = dados_palavra_secreta[0]
    indice_palavra_secreta = dados_palavra_secreta[1]
    palavra_secreta_traducao = busca_traducao_palavra_secreta(indice_palavra_secreta)

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = chute_jogador(nome)

        if (chute in palavra_secreta):
            letras_acertadas = registra_acerto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        # Perdeu o jogo. Sai do laço
        enforcou = erros == 7

        #Ganhou o jogo. Sai do laço
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        imprime_mensagem_letras_faltando(letras_acertadas, nome)

    if (acertou):
        imprime_mensagem_ganhador(nome, palavra_secreta, palavra_secreta_traducao)
    else:
        imprime_mensagem_perdedor(nome, palavra_secreta)

    print("Fim do jogo.")

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo no jogo de Forca!***")
    print("*********************************")

def define_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    indice = random.randrange(0, len(palavras))
    nome = palavras[indice].upper()
    dados_palavra = (nome, indice)
    return dados_palavra

def busca_traducao_palavra_secreta(indice_palavra_secreta):
    palavra_traducao = ""
    index = 0
    arquivo = open("palavras_traducao.txt", "r")
    for linha in arquivo:
        if(index == indice_palavra_secreta):
            palavra_traducao = linha.strip().upper()
            break
        index += 1
    arquivo.close()
    return palavra_traducao

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def imprime_mensagem_letras_faltando(letras_acertadas, nome):
    letras_faltando = str(letras_acertadas.count("_"))
    print(f"{nome}, ainda faltam acertar {letras_faltando} letras")

def chute_jogador(nome):
    chute = input(f"{nome}, Qual letra? ")
    chute = chute.strip().upper()
    return chute

def registra_acerto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_ganhador(nome, palavra_secreta, palavra_secreta_traducao):
    print(f"Parabéns, {nome}! Você ganhou!")
    print(f"E a tradução de {palavra_secreta} é '{palavra_secreta_traducao}'!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(nome, palavra_secreta, palavra_secreta_traducao):
    print(f"Puxa, {nome} você foi enforcado!")
    print(f"A palavra era {palavra_secreta} ({palavra_secreta_traducao})")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()