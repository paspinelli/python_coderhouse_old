#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
#  debe repetirse el proceso hasta que lo introduzca correctamente.


numeros = [1, 3, 7, 9]

numero = int(input("Ingrese un numero menor de 10 "))

while numero not in numeros:
    numero = int(input("Ingrese un numero impar "))
print("Felicitaciones, es correcto")

