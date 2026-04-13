"""
Control de Uso de una Sala de Cómputo - Implementación con CLASS (Objetos)
===========================================================================
Se usa una clase tradicional 'Computador' con atributos y métodos.
El arreglo de la sala es una lista de objetos Computador.
"""


class Computador:
    """Clase que representa un computador en la sala de cómputo."""

    def __init__(self, id_equipo: int, ubicacion: str):
        self.id_equipo = id_equipo
        self.ubicacion = ubicacion
        self.disponible = True
        self.usuario_actual = None
        self.hora_inicio = None

    def asignar(self, usuario: str, hora_inicio: str) -> bool:
        """Asigna el computador a un usuario. Retorna True si tuvo éxito."""
        if self.disponible:
            self.disponible = False
            self.usuario_actual = usuario
            self.hora_inicio = hora_inicio
            return True
        return False

    def liberar(self) -> str:
        """Libera el computador. Retorna el usuario que lo tenía."""
        if not self.disponible:
            usuario = self.usuario_actual
            self.disponible = True
            self.usuario_actual = None
            self.hora_inicio = None
            return usuario
        return ""

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Ocupado por {self.usuario_actual} (desde {self.hora_inicio})"
        return f"[PC-{self.id_equipo:02d}] {self.ubicacion} - {estado}"


class SalaComputo:
    """Sala de cómputo con un arreglo de objetos Computador."""

    def __init__(self, cantidad: int):
        self.computadores: list[Computador] = []
        for i in range(cantidad):
            self.computadores.append(Computador(i + 1, f"Puesto {i + 1}"))

    # --- Funcionalidades principales ---

    def registrar_uso(self, id_equipo: int, usuario: str, hora_inicio: str) -> bool:
        """Registra el uso de un equipo por un usuario."""
        for pc in self.computadores:
            if pc.id_equipo == id_equipo:
                return pc.asignar(usuario, hora_inicio)
        return False

    def mostrar_disponibles(self):
        """Muestra los equipos disponibles."""
        print("\n--- Equipos Disponibles ---")
        disponibles = [pc for pc in self.computadores if pc.disponible]
        if not disponibles:
            print("No hay equipos disponibles.")
        for pc in disponibles:
            print(pc)
        print(f"Total disponibles: {len(disponibles)}/{len(self.computadores)}")

    # --- Funcionalidades adicionales ---

    def liberar_equipo(self, id_equipo: int) -> bool:
        """Libera un equipo para que esté disponible nuevamente."""
        for pc in self.computadores:
            if pc.id_equipo == id_equipo:
                usuario = pc.liberar()
                if usuario:
                    print(f"PC-{id_equipo:02d} liberada por {usuario}.")
                    return True
                else:
                    print(f"PC-{id_equipo:02d} ya estaba disponible.")
                    return False
        print(f"Equipo PC-{id_equipo:02d} no encontrado.")
        return False

    def buscar_por_usuario(self, usuario: str):
        """Busca todos los equipos ocupados por un usuario específico."""
        print(f"\n--- Equipos usados por '{usuario}' ---")
        encontrados = [pc for pc in self.computadores if pc.usuario_actual == usuario]
        if not encontrados:
            print(f"El usuario '{usuario}' no tiene equipos asignados.")
        for pc in encontrados:
            print(pc)
        return encontrados

    def mostrar_estadisticas(self):
        """Muestra estadísticas de uso de la sala."""
        total = len(self.computadores)
        disponibles = sum(1 for pc in self.computadores if pc.disponible)
        ocupados = total - disponibles
        porcentaje_uso = (ocupados / total * 100) if total > 0 else 0

        print("\n--- Estadísticas de la Sala ---")
        print(f"Total equipos:      {total}")
        print(f"Disponibles:        {disponibles}")
        print(f"Ocupados:           {ocupados}")
        print(f"Porcentaje de uso:  {porcentaje_uso:.1f}%")

        if ocupados > 0:
            print("\nUsuarios con equipos asignados:")
            usuarios = {}
            for pc in self.computadores:
                if pc.usuario_actual:
                    usuarios[pc.usuario_actual] = usuarios.get(pc.usuario_actual, 0) + 1
            for u, cant in usuarios.items():
                print(f"  - {u}: {cant} equipo(s)")

    def mostrar_todos(self):
        """Muestra el estado de todos los equipos."""
        print("\n--- Estado de Todos los Equipos ---")
        for pc in self.computadores:
            print(pc)


# ===================== DEMOSTRACIÓN =====================

def main():
    print("============================================")
    print("  Sala de Cómputo - Implementación CLASS")
    print("============================================")

    sala = SalaComputo(8)

    # Mostrar estado inicial
    sala.mostrar_disponibles()

    # Registrar uso
    print("\n>>> Registrando usos...")
    sala.registrar_uso(1, "Oscar Mercado", "08:00")
    sala.registrar_uso(3, "Ana López", "08:15")
    sala.registrar_uso(5, "Carlos Pérez", "08:30")
    sala.registrar_uso(1, "Pedro Gómez", "09:00")  # Ya ocupado, debe fallar
    sala.registrar_uso(7, "Oscar Mercado", "09:00")

    # Mostrar disponibles después de asignaciones
    sala.mostrar_disponibles()

    # Mostrar todos los equipos
    sala.mostrar_todos()

    # Buscar por usuario
    sala.buscar_por_usuario("Oscar Mercado")
    sala.buscar_por_usuario("María García")  # No existe

    # Mostrar estadísticas
    sala.mostrar_estadisticas()

    # Liberar un equipo
    print("\n>>> Liberando equipo 3...")
    sala.liberar_equipo(3)
    sala.liberar_equipo(99)  # No existe

    # Mostrar disponibles después de liberar
    sala.mostrar_disponibles()

    # Estadísticas actualizadas
    sala.mostrar_estadisticas()


if __name__ == "__main__":
    main()