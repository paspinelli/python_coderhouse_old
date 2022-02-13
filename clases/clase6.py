grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
print(grupo)
grupo.update(('Ana', 'Ramon', 'David', 'Esteban', 'Eric'))
print(grupo)
grupo.remove('Mario')
grupo.remove('Miguel')
grupo.discard('Esteban')
print(grupo)