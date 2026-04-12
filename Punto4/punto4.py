from dataclasses import dataclass

@dataclass
class Estudiante:
    nombre: str
    edad: int
    promedio: float

def main():
    estudiantes = [
        Estudiante("Ana Torres", 21, 4.2),
        Estudiante("Luis Mendoza", 19, 3.8),
        Estudiante("Sofia Castro", 22, 4.9)
    ]

    print("--- Antes de la modificacion ---")
    for est in estudiantes:
        print(f"{est.nombre}: {est.promedio}")

    # Cambiar el promedio de un estudiante específico (Luis Mendoza)
    # Buscando por nombre para hacerlo más dinámico
    for est in estudiantes:
        if est.nombre == "Luis Mendoza":
            print(f"\nModificando el promedio de {est.nombre}...")
            est.promedio = 4.5
            break

    print("\n--- Despues de la modificacion ---")
    for est in estudiantes:
        print(f"{est.nombre}: {est.promedio}")

if __name__ == "__main__":
    main()
