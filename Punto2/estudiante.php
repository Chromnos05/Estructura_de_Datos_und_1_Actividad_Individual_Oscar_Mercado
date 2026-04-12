<?php

class Estudiante {
    public $nombre;
    public $edad;
    public $promedio;

    public function __construct($nombre, $edad, $promedio) {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->promedio = $promedio;
    }
}

// En PHP moderno (8.0+) se puede usar constructor promotion
// Pero aquí usaremos la forma clásica para mayor compatibilidad

$estudiantes = [
    new Estudiante("Carlos Gomez", 20, 4.5),
    new Estudiante("Maria Rodriguez", 22, 4.8),
    new Estudiante("Juan Perez", 19, 3.9)
];

foreach ($estudiantes as $e) {
    echo "Nombre: " . $e->nombre . ", Edad: " . $e->edad . ", Promedio: " . $e->promedio . "\n";
}
