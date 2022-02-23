# escriba un programa que pida al usuario un numero mayor que 5
# si el usuario ingresa un numero mayor que 5 que continue ejecutandose
# si el usuario ingresa un numero menor que 5 que se detenga

while True:
    num1 = input("Inserte un numero mayor a 5 ")
    if int(num1) < 5:
        break