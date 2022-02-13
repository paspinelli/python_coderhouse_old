texto = ('gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies ' 
        '  -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista')

lista = texto.split('&')
for indice, item in enumerate(lista):
    lista[indice] = item[0].upper() + item[1:]
texto = '&'.join(lista)
texto = texto.replace('&', '.\n  ')
texto = texto.replace('.', '...', 1)
print(texto)
