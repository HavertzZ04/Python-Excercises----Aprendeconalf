'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

quotient = n1 // n2 
remainder = n1 % n2

print(f"The quotient is: {quotient}\nThe remainder is: {remainder}")