'''
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
'''

v1 = [1, 2, 3]
v2 = [-1, 0, 2]

total = 0

for i in range(len(v1)):
    total += v1[i] * v2[i]
    
print(f"The escalated product is: {total}")

