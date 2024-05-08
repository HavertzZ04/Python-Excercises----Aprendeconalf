'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

school_class = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in range(len(school_class)-1, -1, -1):
    grade = float(input(f"Grade for {school_class[i]}: "))
    if grade >= 3.0:
        school_class.pop(i)
        
    
print("\nYou have to repet: ")    
for i in school_class:
    print(i, end=" ")