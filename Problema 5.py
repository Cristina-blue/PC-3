class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.Age = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.numero_registro}, Edad: {self.Age}, Notas: {self.notas}")

    def setAge(self, edad):
        self.Age = edad

    def setNota(self, nota):
        self.notas.append(nota)

alumno1 = Alumno("Juan Pérez", "1585")
alumno1.setAge(20)
alumno1.setNota(15)
alumno1.setNota(16)
alumno1.setNota(11)

alumno1.display()
