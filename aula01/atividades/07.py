# CALCULE O IMC 
# Crie um programa que calcula o IMC de uma pessoa com base no peso e altura fornecidos e classifica o resultado em diferentes categorias

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print(f"Seu IMC é {imc:.2f}. Você está com o peso ideal.")
elif 25 <= imc < 29.9:
    print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está obeso.")