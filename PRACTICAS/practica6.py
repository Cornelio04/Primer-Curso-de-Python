#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo 
#   si la división es exacta o no. 

number1 = int(input("\ningrese dos numeros \n"))
number2 = int(input())

if (number1 % number2) == 0: 
    print("\nLa división es exacta \n")
else:
    print("\nLa división no es exacta \n")