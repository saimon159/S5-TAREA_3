#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


numero=int(input("numero: "))
totalPares=0
totalImpares=0
while numero!=0:
   pares=0
   impares=0
   while numero!=0:   
       ultimodigito=numero%10
       if ultimodigito%2==0:
           pares+=1
           totalPares+=1
       else:
           impares+=1
           totalImpares+=1
       numero=numero//10
   print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
   numero=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)