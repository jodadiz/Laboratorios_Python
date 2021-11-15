#!/usr/bin/python3
'''
Jose David Diaz Perez
Metodo para formar matrices de x tamaño con todos los datos
con valor de 0
'''

class Matriz:

#Constructor de la clase
    def __init__(self, filas_n, colum_m):

        if filas_n < 0:
            raise Exception(
            'No se puede realizar una cantidad de filas negativas'
        )
        if colum_m < 0:
            raise Exception(
            'No se puede realizar una cantidad de columnas negativas'
        )

        self.filas = filas_n
        self.colum = colum_m

#Permite obtener el elemento en coordenada
    def get (self):
        pass

#Permite Asignar valor a un elemento dado coordenada
    def set (self):
        pass

#Representacion como string
    def __str__(self):

        for i in range(self.filas):
            print ('')

            for j in range(self.colum):
                print (0, end =' ')



if __name__ == '__main__':

#Imprimir la matriz en 0
    print('El tamaño de la matriz en valores 0:')
    matriz = Matriz(3,3)
    print(matriz)

#Metodo get
    # fila = 2
    # columna = 2
    # valor = matriz.get(fila, columna)
    # print (valor)
