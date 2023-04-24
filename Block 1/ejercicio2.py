'''
ejercicio crear un script que muestre los pares en un rango del 0 al 120
'''
def while_range(limit:int):

    count = 1

    while count <= limit:
        if count % 2 == 0 :
            print(f"el numero ({count}) es par")
            count += 1
        else:
            count += 1

def for_range (limit:int):

    for count in range(1,limit+1):
        if count % 2 == 0:
            print(f"el numero ({count}) es par")
        else:
            pass

