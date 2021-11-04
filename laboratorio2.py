#!/usr/bin/python3
"""
Jose David Diaz Perez C02638
Receptor de nombres: Se reliaza su debido formato al nombre, permite
solamente nombres de 3 o 4 componentes y cuando se desea salir
imprime los nombres escritos correctamente en columna.
"""

lista_nom = []

while(True):

    nombre = input('Escriba el nombre o SALIR para salir: ')
    primera_mayus = nombre.title()
    lista = nombre.split(' ')
    compo = len(lista)

    if nombre == 'SALIR':
        for x in lista_nom:
            print(x)

        break

    elif compo >= 3 and compo <= 4:
        lista_nom.append(primera_mayus)

    else:
        print('ERROR: Debe digitar nombres de 3 o 4 componentes.')
        
