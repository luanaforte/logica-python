# CONVERSOR DE TEMPERATURA

# crie um código que converta a temperatura fornecida pelo usuário de celsius para fahrenheit, ou vice-versa, dependendo da escolha do usuário

temperatura = float(input("Digite a temperatura: "))
escala = input("Escolha a escala para conversão (C para Celsius ou F para Fahrenheit): ").upper()

if escala == "C":
    temperatura_convertida = (temperatura - 32) * 5/9
    print(f"{temperatura} ºF é igual a {temperatura_convertida:.2f}ºC")
elif escala == "F":
    temperatura_convertida = (temperatura * 9/5) + 32
    print(f"{temperatura}°C é igual a {temperatura_convertida:.2f}°F.")
else:
    print("Escala inválida. Escolha 'C' ou 'F'.")