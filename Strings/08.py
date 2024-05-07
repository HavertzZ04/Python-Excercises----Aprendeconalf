'''
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''

price = input("Enter the product's price: ")

print(f"The mount is {price[:-3]} euros and {price[-2:]} cents")