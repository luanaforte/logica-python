# Exercício Prático:
# Crie um programa que verifica a idade e imprime:

# "Você é maior de idade" 
# "Você é adolescente" 
# "Você é criança" 

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é adolescente.")
else:
    print("Você é criança.")