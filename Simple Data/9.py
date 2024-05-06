'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
'''

amount = int(input("Enter the amount to invest: "))
annual_interest = float(input("Enter the annual interest rate (decimal 2.8): "))
years = int(input("Enter the number of years: "))


for i in range(years):
    amount += (annual_interest / 100) * (amount)
    
print(f"You will have {round(amount, 2)} in {years} years.")