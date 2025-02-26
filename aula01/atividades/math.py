# DESAFIO
# Calcule a raiz quadrada de um número fornecido pelo usuário

import math 

numero = float(input("Digite um número para calcular a raiz quadrada: "))

raiz_quadrada = round(math.sqrt(numero), 2)

print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")