# DESAFIO - JOGO DA ADIVINHAÇÃO

# Crie um programa onde o computador escolhe um número aleatório entre 1 e 100. o usuário deve adivinhar o número.

# O programa deve informar se o palpite do usuário 

import random

numero_correto = random.randint(1, 100)

tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    
    if palpite < numero_correto:
        print("O número correto é maior. Tente novamente.")
    elif palpite > numero_correto:
        print("O número correto é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break  
