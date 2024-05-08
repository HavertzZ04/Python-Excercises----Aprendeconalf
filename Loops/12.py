'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

phrase = input("Enter a phrase: ").upper()
letter = input("Enter a letter: ").upper()

n = 0

for i in phrase:
    if i == letter:
        n += 1
        
print(f'"{letter.upper()}" is {n} times in the phrase')
