'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
#eval

name = input("Enter the product name: ")
price = float(input("Enter the product price: "))
amount = int(input("Enter the amount: "))

total = price * amount

print(f"Product: {name}")
print(f"Price: {price:,.2f}")
print(f"Amount: {amount:3d}")
print(f"Total Cost: {total:,.2f}")