#Crear un programa para gestionar datos de los socios de un club, permitiendo:
#-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
#Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
#Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
#-Informar cantidad de socios del club.
#-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
#-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
#-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
#-Imprimir el listado de socios completo.

def cargarSocios(socios):
   numero=int(input("Número de socio (0 para cortar): "))
   while numero!=0:
       nombre=input("Nombre y apellido: ")
       fecha=input("Fecha de ingreso (DDMMAAAA): ")
       cuota=input("¿Cuota al día? s/n: ")
       socios[numero]=[nombre,fecha,cuota.lower()=="s"]
       numero=int(input("Número de socio (0 para cortar): "))
   return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
   for numero,datos in socios.items():
       print("-Número:",numero)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formatoFecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

imprimirListado(socios_activos)