# SOMAR NÚMEROS POSITIVOS

# crie um programa que continue pedindo números ao usuário até que ele digite 0. O programa deve somar todos os números positivos e exibir o resultado.

# Inicializa a soma como 0
soma = 0

# Usa while para pedir números ao usuário
while True:
    numero = int(input("Digite um número positivo (ou 0 para sair): "))
    
    if numero == 0:
        break  # Sai do laço se o número for 0
    elif numero > 0:
        soma += numero  # Adiciona o número à soma
    else:
        print("Por favor, digite um número positivo.")

# Exibe o resultado da soma
print(f"A soma de todos os números positivos é: {soma}")
