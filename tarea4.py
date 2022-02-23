
tarea = input("Selecione una tarea 1,2 o 3 \n")
print()
if tarea == "1":
    #1) Imprimir todos los numeros, del 0 al 9, utilizando una repetición for.
    for num1 in range(10):
        print(num1)
elif tarea == "2":
    #2) Imprimir todos los números entre el 100 y el 199.
    for num2 in range(100,200):
        print(num2)
elif tarea == "3":
    #3) Imprimir los números entre el 5 y el 20, saltando de tres en tres
    for num3 in range(5,21,3):
        print(num3)
else:
    print("ERROR")