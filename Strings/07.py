'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

email = input("Enter your email: ")

new_extension = "ceu.es"
position = email.index("@") + 1

updated_email = email.replace(email[position:], new_extension)

print(updated_email)