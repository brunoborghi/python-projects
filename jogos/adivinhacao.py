import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

nome = input("Digite seu nome: ")

numero_secreto = random.randrange(1, 101)
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_tentativas))
    chute = int(input(f"{nome}, digite um número entre 1 e 100: "))
    print(f"{nome}, você digitou ", chute)

    if(chute < 1 or chute > 100):
        print(f"{nome}, você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print(f"{nome}, você acertou!")
        break
    else:
        if(maior):
            print(f"{nome}, você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print(f"{nome}, você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo.")