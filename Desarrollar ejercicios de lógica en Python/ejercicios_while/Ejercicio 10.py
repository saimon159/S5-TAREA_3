#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
#**Ejemplo de ejecución:**
#Libro: Los 3 mosqueteros
#Libro: Historia de 2 ciudades
#Libro: /
#Línea completa. Aparecen 2 dígitos numéricos.
#Libro: 20000 leguas de viaje submarino
#Libro: El señor de los anillos
#Libro: /
#Línea completa. Aparecen 5 dígitos numéricos.
#Libro: 20 años después
#Libro: *
#Fin. Se leyeron 2 líneas completas.


lineas=0
digitos="0123456789"
cantidadDigitos=0
cadena=input("Cadena: ")
while cadena!="*":
    for caracter in cadena:
        if caracter in digitos:
            cantidadDigitos+=1
    if cadena=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    cadena=input("Cadena: ")
print("Se leyeron ",lineas," líneas completas")