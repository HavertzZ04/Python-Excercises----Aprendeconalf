'''
Escribir un programa que lea un entero positivo, n
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
 primeros enteros positivos puede ser calculada de la siguiente forma:
'''

number = int(input("Enter a positive number: "))

total = 0
for i in range(number + 1):
    total += i
    
print(f"The result is: {total}")