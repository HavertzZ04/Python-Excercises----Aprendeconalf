'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

password = "helloworld"

while True:
    answer = input("Password: ")
    
    if password == answer:
        print("Right!")
        break
    print("Try again\n")