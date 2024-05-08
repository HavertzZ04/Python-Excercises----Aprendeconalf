'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindromo")
else:
    print("No palindromo")