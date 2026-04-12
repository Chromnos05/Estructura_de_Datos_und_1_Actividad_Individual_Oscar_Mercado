#include <stdio.h>

struct Estudiante {
    char nombre[50];
    int edad;
    float promedio;
};

int main() {
    struct Estudiante estudiantes[3] = {
        {"Carlos Gomez", 20, 4.5},
        {"Maria Rodriguez", 22, 4.8},
        {"Juan Perez", 19, 3.9}
    };

    for(int i = 0; i < 3; i++) {
        printf("Nombre: %s, Edad: %d, Promedio: %.1f\n", estudiantes[i].nombre, estudiantes[i].edad, estudiantes[i].promedio);
    }

    return 0;
}
