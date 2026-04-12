public class Estudiante {
    String nombre;
    int edad;
    double promedio;

    public Estudiante(String nombre, int edad, double promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    public static void main(String[] args) {
        Estudiante[] estudiantes = {
            new Estudiante("Carlos Gomez", 20, 4.5),
            new Estudiante("Maria Rodriguez", 22, 4.8),
            new Estudiante("Juan Perez", 19, 3.9)
        };

        for (Estudiante e : estudiantes) {
            System.out.println("Nombre: " + e.nombre + ", Edad: " + e.edad + ", Promedio: " + e.promedio);
        }
    }
}
