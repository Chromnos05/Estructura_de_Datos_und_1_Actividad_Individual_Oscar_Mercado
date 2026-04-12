using System;
using System.Collections.Generic;

public class Estudiante
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }

    public Estudiante(string nombre, int edad, double promedio)
    {
        Nombre = nombre;
        Edad = edad;
        Promedio = promedio;
    }

    public static void Main()
    {
        List<Estudiante> estudiantes = new List<Estudiante>
        {
            new Estudiante("Carlos Gomez", 20, 4.5),
            new Estudiante("Maria Rodriguez", 22, 4.8),
            new Estudiante("Juan Perez", 19, 3.9)
        };

        foreach (var e in estudiantes)
        {
            Console.WriteLine($"Nombre: {e.Nombre}, Edad: {e.Edad}, Promedio: {e.Promedio}");
        }
    }
}
