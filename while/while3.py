#El usuario ingresa una cantidad de numeros para definir una media 

n = int(input("Ingrese la cantidad de numeros a calcular su media:  "))

i = 0
suma = 0

while i < n:
    i += 1
    suma += int(input("Ingrese un numero a sumar:  "))
print("La media es", suma/n)