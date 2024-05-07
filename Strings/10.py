'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''

products_list = input("Enter your list separated by commas: ").split(",")

for i in products_list:
    print(i)
