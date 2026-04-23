Objetos (Clases e instancias)
Actividades:

1) Declaración
Definir una clase Estudiante con: nombre, edad, promedio y un método mostrarInfo.

2) Inicialización
Crear 3 instancias y almacenarlas en un arreglo/lista.

3) Recorrido
Llamar al método mostrarInfo para cada objeto.

4) Modificación
Cambiar el promedio de un estudiante mediante un método setPromedio.

5) Comparativa
Explicar la diferencia entre esta clase y un struct o record.

**Respuesta:**
La principal diferencia entre una **Clase** (como la creada en los ejercicios) y un **Struct** o **Record** (registro) radica en los conceptos y propósitos de la Programación Orientada a Objetos:

1. **Datos vs. Comportamiento:** Un *struct* tradicional (por ejemplo, en C o bases de datos) se utiliza primordialmente para agrupar exclusivamente datos bajo un mismo nombre. Una *clase*, por otro lado, puede contener tanto propiedades (variables de estado del objeto) como métodos (funciones como `mostrarInfo()` y `setPromedio()`) estableciendo también un comportamiento para la entidad.
2. **Encapsulamiento y Privacidad:** Las clases están diseñadas para proteger sus datos internos usando modificadores de acceso (`public`, `private`, `protected`). De este modo se restringe quién puede modificar sus propiedades por seguridad directa del programa, mientras que en un struct clásico todo tiende a ser accesible y público.
3. **Herencia y Polimorfismo:** Las clases apoyan el concepto de herencia (construir unas clases a partir de otras) y el polimorfismo, pilares fundamentales de la POO que los structs o records tradicionales no poseen.
*(Nota sobre C++):* Particularmente en este lenguaje, un `struct` y una `class` son funcionalmente casi idénticos (pueden tener métodos ambos). Sin embargo, su distinción principal ahí es que en las clases los miembros son privados por defecto, y en los structs son públicos por defecto. Aún así, por buenas prácticas se guarda preeminentemente la palabra `class` para objetos complejos y `struct` para estructuras llanas de solo datos.
