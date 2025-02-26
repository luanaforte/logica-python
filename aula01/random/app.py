# SORTEIO DE UM NÚMERO ALEATÓRIO 

# A função random.randint(a, b) gera um número inteiro aleatório entre a e b.

import random 

inicio = int(input("Digite o valor de início do intervalo: "))

fim = int(input("Digite o valor de fim do intervalo: "))

numero_aleatorio = random.randint(inicio, fim)

print(f"O número sorteado entre {inicio} e {fim} é: {numero_aleatorio}")