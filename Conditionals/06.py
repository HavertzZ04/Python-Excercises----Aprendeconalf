'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

letters1 = list("abcdefghijklm")
letters2 = list("nopqrsquvwxyz")

name = input("Enter your name: ").lower()
sex = input("Enter your sex (M - F): ").upper()

if sex == "F" and name[0] in letters1:
    print("A")
elif sex == "F" and name[0] in letters2:
    print("B")
elif sex == "M" and name[0] in letters2:
    print("A")
elif sex == "M" and name[0] in letters1:
    print("B")
else:
    print("error")