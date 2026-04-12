interface Estudiante {
    nombre: string;
    edad: number;
    promedio: number;
}

const estudiantes: Estudiante[] = [
    { nombre: "Carlos Gomez", edad: 20, promedio: 4.5 },
    { nombre: "Maria Rodriguez", edad: 22, promedio: 4.8 },
    { nombre: "Juan Perez", edad: 19, promedio: 3.9 }
];

estudiantes.forEach(e => {
    console.log(`Nombre: ${e.nombre}, Edad: ${e.edad}, Promedio: ${e.promedio}`);
});
