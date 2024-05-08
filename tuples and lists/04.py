'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

numbers = []

for i in range(6):
    numbers.append(int(input("Enter the number winner number: ")))
      
numbers.sort()

for i in numbers:
    print(i, end=" ")
print()
