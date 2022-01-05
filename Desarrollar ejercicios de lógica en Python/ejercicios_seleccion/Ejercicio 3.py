#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.


a=int(input("Un número:"))
b=int(input("Otro número:"))
if a<b:
    print("El primero es menor")
elif b<a:
    print("El segundo es menor")
else:
    print("Son iguales")