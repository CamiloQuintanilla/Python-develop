

class Coche:

    def __init__(self,marca,color,velocidad) -> None:
        self.marca = marca
        self.color = color
        self.velocidad = velocidad
    
    def get_marca(self):
        return f"la marca del coche es: {self.marca}"


ferrari = Coche("ferrari","negro",400)
print(ferrari.get_marca())
