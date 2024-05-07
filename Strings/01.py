"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

name = input("Enter your name: ")
number = int(input("Enter a number: "))

for i in range(number):
    print(name)