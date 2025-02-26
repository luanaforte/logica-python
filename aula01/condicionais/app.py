# ESTRUTURAS DE CONTROLE (if, elif, else)

idade = 20

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você é menor de idade, mas pode votar.")
else: 
    print("Você é menor de idade e não pode votar.")

# VERIFICANDO TEMPERATURA
temperatura = 10  

if temperatura < 0:
    print("Está muito frio! Coloque um casaco pesado.")
elif temperatura >= 0 and temperatura <= 15:
    print("Está frio! Use um casaco leve.")
elif temperatura > 15 and temperatura <= 25:
    print("Está ameno! Pode usar uma blusa.")
else:
    print("Está quente! Use roupas leves.")

#CALCULANDO DESCONTO
preco = 150  

if preco >= 100:
    print(f"Preço com desconto de 20%: {preco * 0.8}")
elif preco >= 50:
    print(f"Preço com desconto de 10%: {preco * 0.9}")
else:
    print(f"Preço sem desconto: {preco}")

#VERIFICANDO SE É PAR OU ÍMPAR
numero = 7

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# CALCULADORA SIMPLES
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print(f"A soma é: {num1 + num2}")
elif operacao == "-":
    print(f"A subtração é: {num1 - num2}")
elif operacao == "*":
    print(f"A multiplicação é: {num1 * num2}")
elif operacao == "/":
    if num2 != 0:
        print(f"A divisão é: {num1 / num2}")
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")
