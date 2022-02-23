#Escriba un programa que pida tres números y que escriba si son los tres iguales, 
#   si hay dos iguales o si son los tres distintos.

num1 = input("\ningrese tres numeros\n")
num2 = input()
num3 = input()
if num1 == num2 == num3:
    print("\nLos tres numeros son iguales\n")
elif num1 == num2:
    print("\nHay dos numeros iguales\n")
elif num1 == num3:
    print("\nHay dos numeros iguales\n")
elif num2 == num3:
    print("\nHay dos numeros iguales\n")
else:
    print("\nLos tres numeros son distintos\n")