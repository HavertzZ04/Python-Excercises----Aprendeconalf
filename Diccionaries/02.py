'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

name = input("Name: ")
age = int(input("Age: "))
phone_number = int(input("Phone number: "))
address = input("Address: ")

user_info = {"name": name, "age": age, "phone": phone_number, "address": address}

print(f"{user_info['name']} tiene {user_info['age']} years, vive en {user_info['address']} y el numero de telefono es {user_info['phone']}")