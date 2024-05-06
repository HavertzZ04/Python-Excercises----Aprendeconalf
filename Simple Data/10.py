'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''

clown_kgs = 112
doll_kgs = 75

clown_amount = int(input("Enter the amount of clowns that you want: "))
doll_amount = int(input("Enter the amount of dolls that you want: "))


print(f"This order has:\n{clown_amount} clowns.\n{doll_amount} dolls.\nTotal wheight: {((clown_amount * clown_kgs)+(doll_amount * doll_kgs))}")
