#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

anioInicio=int(input("Año inicial:"))
anioFin=int(input("Año final:"))
for anio in range(anioInicio, anioFin+1):
   if not anio%10==0:
       continue
   if not anio%4==0:
       continue
   if anio%100!=0 or anio%400==0:
       print(anio)