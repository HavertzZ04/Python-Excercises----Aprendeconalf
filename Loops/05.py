'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

amount = int(input("Amount to invest: "))
interest = float(input("Interest: "))
years = int(input("Number of years: "))

for i in range(years):
    amount = amount + (amount * (interest / 100))
    print(amount)