'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

if n2 == 0:
    print("Error!")
else:
    print(n1 / n2)