'''
ejercicio que calcule cuantos estudiantes pasan o pierden la materia
'''

def calculator_mates(students:int,note_pass:float):
    
    approved = 0
    deprecated = 0

    for i in range(1,students + 1):
        note= float(input(f"estudiante #{i} ingresa tu nota: "))

        if note > note_pass:
            approved += 1
        else:
            deprecated += 1

    print(f"la cantidad de estudiantes aprobados es:{approved}")
    print(f"la cantidad de estudiantes reprobados es:{deprecated}")

if __name__ == '__main__':
    calculator_mates(int(input("ingresa la cantidad de estudiantes a evaluar: ")),float(input("ingresa la nota minima para aprobar: ")))