from dataclasses import dataclass

@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

def main():
    # 1. Guardar las instancias en un arreglo (lista)
    estudiantes = [
        Estudiante("Ana Torres", 21, 4.2),
        Estudiante("Luis Mendoza", 19, 3.8),
        Estudiante("Sofia Castro", 22, 4.9),
        Estudiante("Diego Ruiz", 20, 4.5)
    ]

    # 2. Recorrerlo mostrando los datos
    print("--- Lista de Estudiantes (Python) ---")
    for est in estudiantes:
        print(f"Nombre: {est.nombre:<15} | Edad: {est.edad} | Promedio: {est.promedio}")

if __name__ == "__main__":
    main()
