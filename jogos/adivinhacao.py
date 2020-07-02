print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 28

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou...")

print("Fim do jogo.")