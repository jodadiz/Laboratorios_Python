#!/usr/bin/python3

#listas
pares = [0,2,4,6,8]

#valores
cant = int(input('Altura de la piramide: '))
simb = input('Caracter con el que desea realizar la piramide: ')


if cant in pares:

    for x in range(1,cant+1):
        print('')

        for y in range(1,x+1):
            print(simb, end=' ')
else:

#El -1 en el rango indica sera descontando apartir de cant

    for x in range(cant,0,-1):
        print('')

        for y in range(1,x+1):
            print(simb, end=' ')

