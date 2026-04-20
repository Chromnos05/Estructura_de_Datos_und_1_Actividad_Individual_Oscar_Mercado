# Actividad Teórico-Práctica: Structs/Records vs Objetos

## 1. Tabla Comparativa

| Característica | Struct / Record (Estructura típica) | Object / Class (Objeto) |
| :--- | :--- | :--- |
| **Definición** | Tipo de dato compuesto que agrupa variables bajo un solo nombre. Es pasivo (solo contiene datos, carece de acciones). | Entidad que agrupa tanto un estado (datos/atributos) como un comportamiento (métodos/funciones) en una misma unidad. |
| **Mutabilidad** | Generalmente modificable de forma directa sin filtros, ya que todas sus propiedades suelen ser públicas inherentemente. | Mutabilidad controlada a través del encapsulamiento (`private`, `protected`). Los datos mutan pidiendo al objeto que lo haga (usando `setters`). |
| **Tipado** | Tipado cerrado y rígido a la estructura original. No admite conceptos como el polimorfismo ni la herencia clásica. | Tipado que soporta jerarquías. Mediante herencia y polimorfismo, un mismo método puede comportarse distinto según la clase hija. |
| **Memoria** | Se alojan típicamente por valor en la memoria **Stack** (pila), siendo más prestos en creación y eliminación automática al salir de su alcance. | Generalmente se ubican por referencia en el **Heap** (memoria dinámica). Permiten un ciclo de vida complejo en la memoria pero pueden exigir limpieza (o usar *Garbage Collector*). |
| **Ej. Lenguaje Estático (C++)** | `struct Rect { float w, h; };` | `class Rect { private: float w,h; public: Rect(float w, float h); };` |
| **Ej. Lenguaje Dinámico (Python)** | Diccionarios simples `{"w": 5, "h": 2}` o estructuras como `namedtuple`. | `class Rect:` con su bloque `def __init__(self): ...` |

---

## 2. Implementación Analítica (Problema: Área de un Rectángulo)

Para ilustrar contrastes, resolveremos algo sencillo: Un elemento que tiene dimensiones de base y altura, y amerita calcular su área.

### A) Enfoque Estilo Record/Struct (Procedimental)
En este método, los datos van sueltos en un `struct` "tonto" (solo almacena datos). Las funciones se declaran externamente y se envían los datos por argumento.

```cpp
#include <iostream>

// El struct solo es el empaque
struct RectanguloStruct {
    float base;
    float altura;
};

// Y por fuera creamos verbos sueltos
float calcularArea(RectanguloStruct r) {
    return r.base * r.altura;
}

int main() {
    RectanguloStruct miRect = {5.0, -10.0}; // Alguien ingresa altura negativa por error, y el struct no se quejará
    std::cout << "Area del struct: " << calcularArea(miRect) << std::endl;
    return 0;
}
```

* **Ventajas:** Simpleza, extrema claridad (vemos exactamente de qué está compuesto), alto rendimiento puesto que el procesador solo salta en memoria manejando variables fijas en el Stack.
* **Desventajas:** Nada de seguridad interna. Si cambian un dato fundamental a un estado erróneo (-10 de altura), se propaga al resto del sistema y arroja lógicas falsas o rompimientos.

### B) Enfoque Estilo Objeto/Clase (Paradigma OO)
La `clase` es "inteligente". Ella encapsula las propiedades. No permite acceso ajeno sin su supervisión.

```cpp
#include <iostream>

class RectanguloClase {
private: // Información oculta y protegida
    float base;
    float altura;

public:
    // Obliga a instanciarse por este túnel, filtrando la data
    RectanguloClase(float b, float a) {
        setDimensiones(b, a);
    }

    // Funciona de compuerta. Un filtro protector
    void setDimensiones(float b, float a) {
        if(b > 0 && a > 0) {
            base = b;
            altura = a;
        } else {
            base = 1; altura = 1; // Un caso por defecto en vez de aceptar medidas negativas
        }
    }

    // La lógica de negocio está autocontenida
    float calcularArea() {
         // Ya es imposible que calcule áreas con tamaños irreales.
        return base * altura;
    }
};

int main() {
    RectanguloClase miRect(5.0, -10.0); // La clase corrige a: 1 y 1.
    std::cout << "Area del objeto: " << miRect.calcularArea() << std::endl;
    return 0;
}
```

* **Ventajas:** Integridad absoluta (no permite datos absurdos), delegación de responsabilidades (si un área se calcula mal, sabemos exactamente a cuál clase culpar y no revisar todas las funciones del archivo), escalabilidad.
* **Desventajas:** Mucha sobreexigencia y "verbosidad" (`boilerplate`) para un concepto que solo requería pasar 2 decimales. Para sistemas limitados en recursos, las clases implican saltos mínimos mayores de memoria y un montaje de tablas virtuales si se usa herencia.
