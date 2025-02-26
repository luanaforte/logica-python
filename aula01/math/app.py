# CALCULAR O FATORIAL DE UM NÚMERO

# A função math.factorial() calcula o fatorial de um número. O fatorial de um número n é o produto de todos os números inteiros de 1 até n (exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120).

import math 

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = math.factorial(numero)

print(f"O fatorial de {numero} é {fatorial}.")