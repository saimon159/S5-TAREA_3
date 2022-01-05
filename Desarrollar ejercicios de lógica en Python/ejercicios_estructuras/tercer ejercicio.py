#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
#- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
#- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#-Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def cargarNombres(alumnos):
   nombre=input("Nombre: ")
   while nombre!="x":
       alumnos.add(nombre)
       nombre=input("Nombre: ")
   return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)