#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
   #Después debe mostrar por pantalla la paga que le corresponde.

print("\n***************Calculo salarial*************** \n")
horas = input("        Ingrese horas trabajadas: " ) 
coste = input("        Ingrese el coste por hora: ")
print("")
print("        Su salario total es: " + str((float(horas) * float(coste))) + " USD$ \n \n**********************************************")