'''
escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar 
la lista 
'''


def new_list(num):
    indeterminate_list = []

    while len(indeterminate_list) < 120:
        indeterminate_list.append(num)
        num = input("ingresa otro numero: ")
    

    print(f"la lista final es:\n {indeterminate_list}")
    print(f"la longitud de la lista es: {len(indeterminate_list)}")

if __name__ == '__main__':
    new_list(input("ingresa un caracter para añadir a la lista: "))

