#include <iostream>
#include <vector>
#include <string>

struct Estudiante {
    std::string nombre;
    int edad;
    float promedio;
};

int main() {
    std::vector<Estudiante> estudiantes = {
        {"Carlos Gomez", 20, 4.5},
        {"Maria Rodriguez", 22, 4.8},
        {"Juan Perez", 19, 3.9}
    };

    for (const auto& e : estudiantes) {
        std::cout << "Nombre: " << e.nombre << ", Edad: " << e.edad << ", Promedio: " << e.promedio << std::endl;
    }

    return 0;
}
