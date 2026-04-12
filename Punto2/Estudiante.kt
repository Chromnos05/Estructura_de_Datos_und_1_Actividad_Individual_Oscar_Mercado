data class Estudiante(val nombre: String, val edad: Int, val promedio: Double)

fun main() {
    val estudiantes = listOf(
        Estudiante("Carlos Gomez", 20, 4.5),
        Estudiante("Maria Rodriguez", 22, 4.8),
        Estudiante("Juan Perez", 19, 3.9)
    )

    estudiantes.forEach {
        println("Nombre: ${it.nombre}, Edad: ${it.edad}, Promedio: ${it.promedio}")
    }
}
