'''
pedir dos numeros al usuario y realizar las operacion basicas de una calculadora
'''

def calculator_basic(num1:int,num2:int):
    print("-----CALCULADORA---------")
    print(f"operacion suma: {num1 + num2}")
    print(f"operacion resta: {num1 - num2}")
    print(f"operacion multiplicacion: {num1 * num2}")
    print(f"operacion divicion: {num1/num2}")

if __name__ == '__main__':
    calculator_basic(int(input("ingresa el numero #1: ")),int(input("ingresa el numero #2: ")))