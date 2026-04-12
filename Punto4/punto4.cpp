#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    vector<Estudiante> estudiantes = {
        {"Ana Torres", 21, 4.2},
        {"Luis Mendoza", 19, 3.8},
        {"Sofia Castro", 22, 4.9}
    };

    cout << "--- Antes de la modificacion ---" << endl;
    for (const auto& est : estudiantes) {
        cout << est.nombre << ": " << est.promedio << endl;
    }

    // Cambiar el promedio de un estudiante específico (Luis Mendoza en el índice 1)
    cout << "\nModificando el promedio de " << estudiantes[1].nombre << "..." << endl;
    estudiantes[1].promedio = 4.5;

    cout << "\n--- Despues de la modificacion ---" << endl;
    for (const auto& est : estudiantes) {
        cout << est.nombre << ": " << est.promedio << endl;
    }

    return 0;
}
