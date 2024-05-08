'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''

n = int(input("Number: "))

for i in range(2, n):
    if n % i == 0:
        break
    
if(i + 1) == n:
    print("prime")
else:
    print("no prime")