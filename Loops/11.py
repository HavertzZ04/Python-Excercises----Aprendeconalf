'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

word = input("Enter a word: ")

for i in range(len(word), 0, -1):
    print(word[i - 1], end=" ")
print("")