# LAÇO DE REPETIÇÃO (while)

contador = 0
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1 

# contagem regressiva
contador = 10
while contador >= 0:
    print(f"Contagem regressiva: {contador}")
    contador -= 1  

# Somando números até atingir um valor
soma = 0
numero = 1
while soma < 50:
    soma += numero
    numero += 1
    print(f"Soma até o momento: {soma}")

# Verificando a validade de uma senha
senha_correta = "python123"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta! Tente novamente.")

print("Senha correta! Acesso liberado.")

# imprimindo números pares até 10
numero = 0
while numero <= 10:
    if numero % 2 == 0:
        print(f"Número par: {numero}")
    numero += 1

# crie um programa que peça ao usuário para inserir números. Os números acumulados devem ser somados quando o usuário quebrar o laço usando break.
soma = 0

while True:
    numero = int(input("Digite um número para somar (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma total é: {soma}")

# contando até o número desejado
numero = int(input("Digite um número para contar até ele: "))
contador = 1

while contador <= numero:
    print(contador)
    contador += 1

