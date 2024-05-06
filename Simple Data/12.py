'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''

bread = 3.49
discount = 0.60

amount = int(input("Enter the amount of bread that you bought: "))

print(f"Bread price: {bread}€")
print(f"Discount: {discount * 100}%")
print(f"Total amount: {round(bread * amount * (1 - discount), 2)}€")



