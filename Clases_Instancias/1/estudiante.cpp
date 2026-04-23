#include <iostream>
#include <string>

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
    Estudiante estudiante1("Oscar", 20, 4.5);
    estudiante1.mostrarInfo();
    return 0;
}
