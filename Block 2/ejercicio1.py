'''
programa con lista de 8 numeros enteros
    -recorrer la lista y mostrarla
    -ordenarla y mostrarla
    -mostrar su longitud
    -buscar elemento que el usuario pida
'''

list_num = [1,2,3,4,5,6,7,8]

def check_list (list:list):

    print("recorrido de la lista")
    for n in list:
        print(n)
    print("fin del recorrido")

    list.sort()
    print(f"la lista ordenada es: {list}")

    print(f"la longitud de la lista es: {len(list)}")

    search = int(input("ingresa el numero que quieras buscar: "))

    if search in list:
        print("si se encuentra tu numero")
    else:
        print("no se encuentra tu numero")

if __name__ == '__main__':

    check_list(list_num)



