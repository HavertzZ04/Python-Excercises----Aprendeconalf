'''
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

money =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
answer = input("Enter a currency: ").title()

if answer in money:
    print(money[answer])
else:
    print(f"There is not a currency for {answer}")
        
        