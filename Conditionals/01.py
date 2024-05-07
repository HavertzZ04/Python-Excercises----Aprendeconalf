'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

age = int(input("Enter you age: "))

if age >= 18:
    print("You are adult")
else:
    print("You are underage")