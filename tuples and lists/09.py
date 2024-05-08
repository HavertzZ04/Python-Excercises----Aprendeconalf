'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''

vocals = ['a', 'e', 'i', 'o', 'u']
vocals_amount = []


word = input("Enter a word: ")

for i in range(len(vocals)):
    vocals_amount.append(word.count(vocals[i]))
    
print(f"In the word {word} you cand find: ")

for i in range(len(vocals)):
    print(f"{vocals[i]} : {vocals_amount[i]}")




