from dataclasses import dataclass

@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

# Instancias
estudiantes = [
    Estudiante("Carlos Gomez", 20, 4.5),
    Estudiante("Maria Rodriguez", 22, 4.8),
    Estudiante("Juan Perez", 19, 3.9)
]

for e in estudiantes:
    print(f"Nombre: {e.nombre}, Edad: {e.edad}, Promedio: {e.promedio}")
