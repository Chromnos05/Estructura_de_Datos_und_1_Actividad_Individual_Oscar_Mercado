class Estudiante {
  final String nombre;
  final int edad;
  final double promedio;

  Estudiante(this.nombre, this.edad, this.promedio);
}

void main() {
  final estudiantes = [
    Estudiante("Carlos Gomez", 20, 4.5),
    Estudiante("Maria Rodriguez", 22, 4.8),
    Estudiante("Juan Perez", 19, 3.9),
  ];

  for (var e in estudiantes) {
    print("Nombre: ${e.nombre}, Edad: ${e.edad}, Promedio: ${e.promedio}");
  }
}
