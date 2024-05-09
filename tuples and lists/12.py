'''
Escribir un programa que almacene las matrices


en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
'''
import numpy as np

A = np.array([
     [1, 2 ,3],
     [4, 5, 6]
])

B = np.array([
     [-1, 0],
     [0, 1],
     [1, 1]
])

C = np.dot(A, B)

print(C)    
