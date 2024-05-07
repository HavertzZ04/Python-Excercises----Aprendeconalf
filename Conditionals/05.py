'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''


age = int(input("Enter your age: "))
money = int(input("Enter the money you won: "))

if age > 16 and money >= 1000:
    print("You have to pay taxes")
else:
    print("Good to go")