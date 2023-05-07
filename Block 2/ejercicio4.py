'''
ejercicio 4 crear un script que tenga 4 variables , una lista, un string, un entero  y un booleano que imprima un mensaje segun el tipo de dato de cada variable
'''

list_types = ["hola como estas",11,True]
string = "hola esto es un string"
number = 12
boolean = False


def check_types(variable):

    type_variable=type(variable)

    if type_variable == str:
        message = "la variable es un string"

    elif type_variable == int:
        message = "la variable es un entero"

    elif type_variable == float:
        message = "la variable es un flotante"
    
    elif type_variable == bool:
        message = "la variable es un booleano"
    
    elif type_variable == list:
        message = "la variable es una lista"

    return message
    
parametrized = [list_types,string,number,boolean]

if __name__ == '__main__':
    for n in parametrized:
        print(check_types(n))


