'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''

anual_interest = 0.04
money_saved = int(input("Enter the money you saved: "))

for i in range(3):
    money_saved = money_saved + (money_saved * anual_interest)
    print(f"First year balance is: {round(money_saved, 2)}")
    
