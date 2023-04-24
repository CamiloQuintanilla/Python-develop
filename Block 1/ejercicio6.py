'''
mostrar todas las tablas de multiplicar del 1 al 10
'''

def multiplication_tables():

    for tables in range(1,11):
        print(f"---TABLA DEL {tables}---")
        for numbers in range(1,11):
            print(f"{tables} x {numbers} = {tables * numbers}")
    
        print("------------")

if __name__ == '__main__':
    multiplication_tables()