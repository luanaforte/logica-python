# DESAFIO

# Crie um programa que sorteie um nome de uma lista de estudantes e exiba o vencedor.

import random 

estudantes = ["Ana", "Carlos", "Maria", "João", "Pedro", "Julia"]

vencedor = random.choice(estudantes)

print(f"O vencedor do sorteio é: {vencedor}")