'''
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''

hours = int(input("How many hours did your work? "))
price = int(input("How much per hour? "))

print(f"You will get paid: {hours * price} dollars")