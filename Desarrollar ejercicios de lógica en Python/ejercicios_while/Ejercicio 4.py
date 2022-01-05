#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma)