# solicite um número para o usuário e solicite seu fatorial

numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = 1
contador = 1
while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é {fatorial}")