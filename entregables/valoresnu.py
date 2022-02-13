def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    return 0

print(relacion(5, 10), relacion(10, 5), relacion(5, 5))


def intermedio(num1, num2):
    return (num1 + num2) / 2

intermedio(-12, 24)


def recortar(num, lim_inf, lim_sup):
    return max(min(num, lim_sup), lim_inf)

recortar(-2, 0, 10)



def separar(*args):
    lista = sorted(args)
    pares = []
    impares = []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares

pares, impares = separar(*numeros)
print(pares)   
print(impares)  
