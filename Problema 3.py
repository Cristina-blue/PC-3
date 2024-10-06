import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        #math pi = valor aprox de 3.14
        return math.pi * (self.radio ** 2)


circulo1 = CIRCULO(4)  
circulo2 = CIRCULO(1)  

print(f"El área del círculo 1 es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo 2 es: {circulo2.calcular_area():.2f}")
