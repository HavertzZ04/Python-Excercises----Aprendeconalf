'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''

date = input("Enter your date of birth in this format (dd/mm/yyyy): ")
date_list = date.split('/')

print(f"Day: {date_list[0]}")
print(f"Month: {date_list[1]}")
print(f"Year: {date_list[2]}")
