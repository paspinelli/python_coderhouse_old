

#numero = int(input('Ingresa hasta que numero queres sumar?'))
#suma = 0
#for num in range (numero):
#    num += 1
#    suma += num
#print(suma)


suma = 0 
while True:
    numero = int(input('Ingresa hasta que numero queres sumar? '))
    if numero != 0:
        suma += numero
    else:
        break
print(suma)