'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

pizza_veg = ['mozzarella', 'tomatoes', 'pepper', 'tofu']
pizza = ['mozzarella', 'tomatoes', 'pepperoni', 'jam', 'salmon']

print("1. Pizza.\n2. Pizza Vegetarian.")

answer = input("Your answer her (1 - 2): ")

if answer == "1":
    print("Select one ingredient: ")
    for i, ingredient in enumerate(pizza[2:]):
        print(f"{i+1}. {ingredient}")
    answer2 = int(input("Your answer her (1 - 3): "))
    print(f"Your pizza has: {pizza[0]}, {pizza[1]} and {pizza[answer2 + 1]}")
else:
    print("Select one ingredient: ")
    for i, ingredient in enumerate(pizza_veg[2:]):
        print(f"{i+1}. {ingredient}")
    answer2 = int(input("Your answer her (1 - 2): "))
    print(f"Your vegetarian pizza has: {pizza_veg[0]}, {pizza_veg[1]} and {pizza_veg[answer2 + 1]}")
