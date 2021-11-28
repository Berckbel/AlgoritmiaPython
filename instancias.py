class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

# if __name__ == '__main__':
#     coord_1 = Coordenada(3, 30)
#     coord_2 = Coordenada(4, 8)

#     print(coord_1.distancia(coord_2))
#     print(isinstance(coord_2, Coordenada))

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# if __name__ == '__main__':
#     rectangulo = Rectangulo(3, 4)
#     print(rectangulo.area())

#     cuadrado = Cuadrado(5)
#     print(cuadrado.area())

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando Caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('Ando en Bicicleta')

if __name__ == '__main__':
    persona = Persona('Raul')
    persona.avanza()

    ciclista = Ciclista('Juan')
    ciclista.avanza()
