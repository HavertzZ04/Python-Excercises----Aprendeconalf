'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

school_class = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
answers = []

for i in school_class:
    answers.append(input(f"Enter the score for {i}: "))

print()
    
for i in range(len(school_class)):
    print(f"Your score in {school_class[i]} is: {answers[i]}")