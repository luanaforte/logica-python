# Desafio: Ordenando Três Números

# Peça ao usuário para digitar três números e depois imprima-os em ordem crescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificando qual é o maior e qual é o menor
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        maior = num3
    else:
        medio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        maior = num3
    else:
        medio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        medio = num1
        maior = num2
    else:
        medio = num2
        maior = num1

print(f"Ordem crescente: {menor}, {medio}, {maior}")
