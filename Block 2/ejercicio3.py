'''
programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minusculas y mostrarlo en mayusculas
'''

test = " "

if len(test.strip()) > 0:
    print("la variable se encuentra llena")

else:
    test= "prueba en minusculas nueva longitud"
    print(test.upper())