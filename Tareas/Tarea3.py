#Escriba un programa que pida el año actual y un año cualquiera y que escriba 
#   cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

Actual = input("Incerte el año actual: ")
Any = input("Incerte un año cualquiera: ")
if Actual > Any:
    print("Han pasado " + str(int(Actual) - int(Any)) + " años ")
elif Any > Actual:
    print("Faltan "+ str(int(Any) - int(Actual)) + " años ")
else:
    print("Son el mismo año")