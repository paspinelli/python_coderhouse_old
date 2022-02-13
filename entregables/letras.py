lista_a = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_b = ["h",'o','l','a',' ', 'l','u','n','a']

lista_c = []

for letra in lista_a:
    if letra in lista_b and letra not in lista_3:
        lista_c.append(letra)

print(lista_c)

