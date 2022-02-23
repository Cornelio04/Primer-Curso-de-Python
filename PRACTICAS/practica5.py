# escriba un programa que pregunte al usuario un numero y si el numero es mayor a 9
# Imprima "el numero ingresado es mayor a 9" y si no que imprima "el numero ingresado es menor a 9

number = int(input("\nIngrese un numero "))
if number > 9:
    print("\nEl numero ingresado es mayor que 9 \n")
elif number < 9:
    print("\nEl numero ingresado es menor que 9\n")
else:
    print("\nel numero es 9\n")