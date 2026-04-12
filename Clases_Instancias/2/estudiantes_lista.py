class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.promedio}")

if __name__ == "__main__":
    # Crear 3 instancias
    estudiante1 = Estudiante("Oscar", 20, 4.5)
    estudiante2 = Estudiante("Maria", 19, 4.8)
    estudiante3 = Estudiante("Juan", 21, 3.9)

    # Almacenarlas en una lista
    lista_estudiantes = [estudiante1, estudiante2, estudiante3]

    # Mostrar información de cada uno
    print("Información de los estudiantes en la lista:")
    for est in lista_estudiantes:
        est.mostrarInfo()
        print("-" * 20)
