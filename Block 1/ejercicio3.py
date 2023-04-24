'''
escribir un script que calcule el cuadrado de X cantidad de numeros naturales
'''

def square_range(n:int):
     
     for i in range(1,n+1):
          print(f"el cuadrado del numero: {i} es: {i*i}")

if __name__ == '__main__':
     square_range(60)