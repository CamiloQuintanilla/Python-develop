'''
programa que muestre los impares en un rango que de el usuario
'''

def range_odd(num1:int,num2:int):

    if num1 < num2:
        for i in range(num1,num2 + 1):
            if i % 2 == 1:
                print(f"el numero {i} es impar")
    else:
        print("rango no valido")

if __name__ == '__main__':
    range_odd(int(input("ingresa el numero #1: ")),int(input("ingresa el numero #2: ")))