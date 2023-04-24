'''
un programa que muestre todos los numeros entre dos numeros que se ingresen
'''

def numbers_range(num1:int,num2:int):
    if num1 < num2 :
        for i in range(num1,num2 + 1):
            print(i)
    else:
        print("rango no valido")

if __name__ == '__main__':
    numbers_range(int(input("ingresa el numero #1: ")),int(input("ingresa el numero #2: ")))