'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''


weight = float(input("What is your weight in kgs (ex: 55): ")) 
height = float(input("What is your height in mts (ex: 1.72): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {round(bmi, 2)}")