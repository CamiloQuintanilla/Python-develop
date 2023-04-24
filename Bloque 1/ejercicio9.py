'''
perdir datos al usuario hasta que ingrese 111
'''

def sentinel ():

    num = int(input("ingresa un numero: "))

    # while not num == 111:
    #     num = int(input("dame otro numero: "))

    while num != 111:
        num = int(input("dame otro numero: "))
    
    print("has ingresado el numero 111 el programa termina")

if __name__ == '__main__':
    sentinel()
