import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)


class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)


def validar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El número debe ser positivo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")


def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            radio = validar_numero("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"Área del círculo: {circulo.calcular_area():.2f}")

        elif opcion == '2':
            largo = validar_numero("Ingrese el largo del rectángulo: ")
            ancho = validar_numero("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.calcular_area():.2f}")

        elif opcion == '3':
            lado = validar_numero("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"Área del cuadrado: {cuadrado.calcular_area():.2f}")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

menu()
