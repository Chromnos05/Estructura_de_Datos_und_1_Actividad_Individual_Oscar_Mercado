"""
Control de Uso de una Sala de Cómputo - Implementación con RECORD (NamedTuple)
===============================================================================
Se usa typing.NamedTuple como equivalente de Record en Python.
Los records son INMUTABLES: una vez creado, no se pueden modificar sus campos.
Para "modificar" el estado de un computador, se crea un NUEVO registro
con los datos actualizados, reemplazando el anterior en el arreglo.
Esta inmutabilidad es la característica principal de un Record.
"""

from typing import NamedTuple


class ComputadorRecord(NamedTuple):
    """Record que almacena los datos de un computador.
    Equivalente a 'record' en Java/C#: datos inmutables.
    A diferencia de struct/class, NO se pueden modificar sus campos
    después de la creación. Para cambiar el estado, se crea un nuevo
    registro con los datos actualizados.
    """
    id_equipo: int
    ubicacion: str
    disponible: bool = True
    usuario_actual: str = None
    hora_inicio: str = None

    def con_uso(self, usuario: str, hora_inicio: str) -> "ComputadorRecord":
        """Retorna un NUEVO record con el equipo marcado como ocupado."""
        return self._replace(
            disponible=False,
            usuario_actual=usuario,
            hora_inicio=hora_inicio
        )

    def liberado(self) -> "ComputadorRecord":
        """Retorna un NUEVO record con el equipo marcado como disponible."""
        return self._replace(
            disponible=True,
            usuario_actual=None,
            hora_inicio=None
        )

    def formato_estado(self) -> str:
        """Retorna una representación legible del estado."""
        if self.disponible:
            return f"[PC-{self.id_equipo:02d}] {self.ubicacion} - Disponible"
        return f"[PC-{self.id_equipo:02d}] {self.ubicacion} - Ocupado por {self.usuario_actual} (desde {self.hora_inicio})"


class SalaComputo:
    """Sala de cómputo con un arreglo de records (NamedTuples).
    Dado que los records son inmutables, cada cambio implica crear un nuevo
    registro y reemplazarlo en la posición correspondiente del arreglo.
    """

    def __init__(self, cantidad: int):
        self.computadores: list[ComputadorRecord] = []
        for i in range(cantidad):
            self.computadores.append(
                ComputadorRecord(id_equipo=i + 1, ubicacion=f"Puesto {i + 1}")
            )

    def _buscar_indice(self, id_equipo: int) -> int:
        """Busca el índice de un equipo en el arreglo. Retorna -1 si no existe."""
        for i, pc in enumerate(self.computadores):
            if pc.id_equipo == id_equipo:
                return i
        return -1

    # --- Funcionalidades principales ---

    def registrar_uso(self, id_equipo: int, usuario: str, hora_inicio: str) -> bool:
        """Registra el uso de un equipo por un usuario.
        Crea un NUEVO record y lo reemplaza en el arreglo (inmutabilidad).
        """
        idx = self._buscar_indice(id_equipo)
        if idx == -1:
            return False
        pc = self.computadores[idx]
        if pc.disponible:
            self.computadores[idx] = pc.con_uso(usuario, hora_inicio)
            return True
        return False

    def mostrar_disponibles(self):
        """Muestra los equipos disponibles."""
        print("\n--- Equipos Disponibles ---")
        disponibles = [pc for pc in self.computadores if pc.disponible]
        if not disponibles:
            print("No hay equipos disponibles.")
        for pc in disponibles:
            print(pc.formato_estado())
        print(f"Total disponibles: {len(disponibles)}/{len(self.computadores)}")

    # --- Funcionalidades adicionales ---

    def liberar_equipo(self, id_equipo: int) -> bool:
        """Libera un equipo. Crea un NUEVO record libre y lo reemplaza."""
        idx = self._buscar_indice(id_equipo)
        if idx == -1:
            print(f"Equipo PC-{id_equipo:02d} no encontrado.")
            return False
        pc = self.computadores[idx]
        if not pc.disponible:
            usuario = pc.usuario_actual
            self.computadores[idx] = pc.liberado()
            print(f"PC-{id_equipo:02d} liberada por {usuario}.")
            return True
        else:
            print(f"PC-{id_equipo:02d} ya estaba disponible.")
            return False

    def buscar_por_usuario(self, usuario: str):
        """Busca todos los equipos ocupados por un usuario específico."""
        print(f"\n--- Equipos usados por '{usuario}' ---")
        encontrados = [pc for pc in self.computadores if pc.usuario_actual == usuario]
        if not encontrados:
            print(f"El usuario '{usuario}' no tiene equipos asignados.")
        for pc in encontrados:
            print(pc.formato_estado())
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
            print(pc.formato_estado())

    def mostrar_record_original(self, id_equipo: int):
        """Demuestra la inmutabilidad: muestra el record como tupla."""
        idx = self._buscar_indice(id_equipo)
        if idx != -1:
            print(f"Record como tupla: {self.computadores[idx]}")


# ===================== DEMOSTRACIÓN =====================

def main():
    print("============================================")
    print("  Sala de Cómputo - Implementación RECORD")
    print("  (Usando NamedTuple como record)")
    print("============================================")

    sala = SalaComputo(8)

    # Mostrar estado inicial
    sala.mostrar_disponibles()

    # Demostrar inmutabilidad del record
    print("\n>>> Demostrando inmutabilidad del Record...")
    pc1 = sala.computadores[0]
    print(f"Record original: {pc1}")
    print(f"Es tupla: {isinstance(pc1, tuple)}")
    # Intentar modificar directamente causaría error (descomentar para ver):
    # pc1.disponible = False  # AttributeError: can't set attribute

    # Registrar uso - crea NUEVOS records
    print("\n>>> Registrando usos (se crean nuevos records)...")
    sala.registrar_uso(1, "Oscar Mercado", "08:00")
    sala.registrar_uso(3, "Ana López", "08:15")
    sala.registrar_uso(5, "Carlos Pérez", "08:30")
    sala.registrar_uso(1, "Pedro Gómez", "09:00")  # Ya ocupado, debe fallar
    sala.registrar_uso(7, "Oscar Mercado", "09:00")

    # Mostrar disponibles después de asignaciones
    sala.mostrar_disponibles()

    # Mostrar todos los equipos
    sala.mostrar_todos()

    # Ver el record modificado (es un NUEVO objeto)
    print("\n>>> Record después de asignar uso:")
    sala.mostrar_record_original(1)

    # Buscar por usuario
    sala.buscar_por_usuario("Oscar Mercado")
    sala.buscar_por_usuario("María García")  # No existe

    # Mostrar estadísticas
    sala.mostrar_estadisticas()

    # Liberar un equipo - crea otro NUEVO record
    print("\n>>> Liberando equipo 3 (se crea otro record nuevo)...")
    sala.liberar_equipo(3)
    sala.liberar_equipo(99)  # No existe

    # Mostrar disponibles después de liberar
    sala.mostrar_disponibles()

    # Estadísticas actualizadas
    sala.mostrar_estadisticas()

    # Ver el record liberado
    print("\n>>> Record después de liberar:")
    sala.mostrar_record_original(3)


if __name__ == "__main__":
    main()