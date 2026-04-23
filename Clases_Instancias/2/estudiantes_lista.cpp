#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Estudiante {
public:
    string nombre;
    int edad;
    float promedio;

    Estudiante(string n, int e, float p) : nombre(n), edad(e), promedio(p) {}

    void mostrarInfo() {
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
        cout << "Promedio: " << promedio << endl;
    }
};

int main() {
    // Definir un vector para almacenar las instancias
    vector<Estudiante> listaEstudiantes;

    // Crear 3 instancias y agregarlas al vector
    listaEstudiantes.push_back(Estudiante("Oscar", 20, 4.5));
    listaEstudiantes.push_back(Estudiante("Maria", 19, 4.8));
    listaEstudiantes.push_back(Estudiante("Juan", 21, 3.9));

    // Mostrar información de cada estudiante recorriendo el vector
    cout << "Informacion de los estudiantes en el vector:" << endl;
    for (int i = 0; i < listaEstudiantes.size(); i++) {
        listaEstudiantes[i].mostrarInfo();
        cout << "--------------------" << endl;
    }

    return 0;
}
