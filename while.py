
while True:

    Actual = input("Incerte el año actual: ")
    Any = input("Incerte un año cualquiera: ")
    if Actual > Any:
        print("Han pasado " + str(int(Actual) - int(Any)) + " años ")
    elif Any > Actual:
        print("Faltan "+ str(int(Any) - int(Actual)) + " años ")
    else:
        print("Son el mismo año")
    respuesta = input("desea continuar (si/no): ")
    if respuesta == "no":
        break
    elif respuesta == "si":
        print()
    else:
        print ("ERROR respuesta no valida ")
        
        
