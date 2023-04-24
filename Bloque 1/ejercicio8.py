'''
cuanto es el x porciento de un numero
'''

def percent (num:int,percentage:int):

    print(f"el {percentage}% de {num} = {(num*percentage)/100}")


if __name__ == '__main__':
    percent(int(input("ingresa un numero: ")),int(input("ingresa el porcentaje que quieres calcular: ")))