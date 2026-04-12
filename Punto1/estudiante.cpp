#include <iostream>
#include <string>

using namespace std;

// Definición de la estructura Estudiante
struct Estudiante {
  string nombre;
  int edad;
  float promedio;
};

int main() {
  // Ejemplo de uso
  Estudiante est1;
  est1.nombre = "Juan Perez";
  est1.edad = 20;
  est1.promedio = 4.5;

  cout << "Nombre: " << est1.nombre << endl;
  cout << "Edad: " << est1.edad << endl;
  cout << "Promedio: " << est1.promedio << endl;

  return 0;
}
