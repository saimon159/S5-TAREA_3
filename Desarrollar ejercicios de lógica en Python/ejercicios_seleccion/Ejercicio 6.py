#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.


nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
posicion_final_nombre1=len(nombre1)-1
posicion_final_nombre2=len(nombre2)-1
if nombre1[0] == nombre2[0] or nombre1[posicion_final_nombre1] == nombre2[posicion_final_nombre2]:
    print("coincidencia")
else:
    print("no hay coincidencia")