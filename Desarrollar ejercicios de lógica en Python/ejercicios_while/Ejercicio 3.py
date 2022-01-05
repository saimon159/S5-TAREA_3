#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


mayor=-1
n=int(input("Número positivo:"))
while n>=0:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)