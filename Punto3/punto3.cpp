#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Definición de la estructura
struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    // 1. Guardar las instancias en un arreglo (vector)
    vector<Estudiante> estudiantes = {
        {"Ana Torres", 21, 4.2},
        {"Luis Mendoza", 19, 3.8},
        {"Sofia Castro", 22, 4.9},
        {"Diego Ruiz", 20, 4.5}
    };

    // 2. Recorrer el arreglo mostrando los datos
    cout << "--- Lista de Estudiantes (C++) ---" << endl;
    for (const auto& est : estudiantes) {
        cout << "Nombre: " << est.nombre 
             << " | Edad: " << est.edad 
             << " | Promedio: " << est.promedio << endl;
    }

    return 0;
}
