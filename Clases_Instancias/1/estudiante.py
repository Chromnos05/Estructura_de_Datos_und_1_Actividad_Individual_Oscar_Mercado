class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.promedio}")

# Ejemplo de uso
if __name__ == "__main__":
    estudiante1 = Estudiante("Oscar", 20, 4.5)
    estudiante1.mostrarInfo()
