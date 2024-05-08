'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''

number = int(input("Enter a number: "))

for i in range(number + 1):
    print("*" * i)
