from dataclasses import dataclass

@dataclass
class Estudiante:
    """
    Representa un estudiante con nombre, edad y promedio.
    Utilizamos dataclass como equivalente moderno a un record.
    """
    nombre: str
    edad: int
    promedio: float

# Ejemplo de uso
if __name__ == "__main__":
    est1 = Estudiante(nombre="Juan Perez", edad=20, promedio=4.5)
    print(f"Nombre: {est1.nombre}")
    print(f"Edad: {est1.edad}")
    print(f"Promedio: {est1.promedio}")
