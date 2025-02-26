# CHEQUE SE UM NÚMERO É DIVISÍVEL POR 3 E POR 5

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} é divisível por 3 e 5.")
elif numero % 3 == 0:
    print(f"{numero} é divisível por 3.")
elif numero % 5 == 0:
    print(f"{numero} é divisível por 5.")
else:
    print(f"{numero} não é divisível por 3 nem por 5.")