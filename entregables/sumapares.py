numeros = []

numero = 0
while numero<100:
    numero+=1
    if numero%2 != 0:
        numeros.append(numero)
print(sum(numeros)) 