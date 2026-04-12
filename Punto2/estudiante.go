package main

import "fmt"

type Estudiante struct {
	Nombre   string
	Edad     int
	Promedio float64
}

func main() {
	estudiantes := []Estudiante{
		{Nombre: "Carlos Gomez", Edad: 20, Promedio: 4.5},
		{Nombre: "Maria Rodriguez", Edad: 22, Promedio: 4.8},
		{Nombre: "Juan Perez", Edad: 19, Promedio: 3.9},
	}

	for _, e := range estudiantes {
		fmt.Printf("Nombre: %s, Edad: %d, Promedio: %.1f\n", e.Nombre, e.Edad, e.Promedio)
	}
}
