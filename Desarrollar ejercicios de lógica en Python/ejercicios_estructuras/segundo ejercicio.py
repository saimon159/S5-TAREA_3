#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#-Agregar pasajeros a la lista de viajeros.
#-Agregar ciudades a la lista de ciudades.
#-Dado el DNI de un pasajero, ver a qué ciudad viaja.
#-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#-Dado el DNI de un pasajero, ver a qué país viaja.
#-Dado un país, mostrar cuántos pasajeros viajan a ese país.
#-Salir del programa.

def agregarPasajeros(pasajeros):
    nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

#programa principal
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")