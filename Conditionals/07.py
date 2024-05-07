'''
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	          Tipo impositivo
Menos de 10000€	        5%
10000€ y 20000€	        15%
20000€ y 35000€	        20%
35000€ y 60000€	        30%
Más de 60000€	        45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''

rent = int(input("Enter your anual rent: "))

if rent < 10000:
    print("5%")
elif rent < 20000:
    print("15%")
elif rent < 35000:
    print("20%")
elif rent < 60000:
    print("30%")
else:
    print("45%")

