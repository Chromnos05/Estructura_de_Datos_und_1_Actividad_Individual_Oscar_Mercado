# Comparativa: Class vs Struct vs Record - Sala de Cómputo

## 1. Conceptos fundamentales

### Class (Objeto)
Una **clase** es una plantilla que define un tipo de dato compuesto por **atributos** (datos) y **métodos** (comportamiento). Los objetos creados a partir de una clase son **mutables**: sus atributos pueden cambiarse directamente. La clase encapsula tanto el estado como la lógica de negocio.

### Struct (Estructura de datos)
Un **struct** agrupa datos relacionados en una sola unidad, pero **sin lógica de negocio** interna. Es un contenedor de datos puro. En Python, el equivalente es `@dataclass`. A diferencia de una clase, el struct delega la lógica a componentes externos y se enfoca exclusivamente en almacenar información. Es **mutable** como la clase.

### Record (Registro inmutable)
Un **record** es similar al struct en que agrupa datos, pero con una diferencia crucial: es **inmutable**. Una vez creado, no se pueden modificar sus campos. Para representar un cambio de estado, se debe crear un **nuevo record** con los datos actualizados. En Python, el equivalente es `NamedTuple`. Los records son inherentemente seguros para uso concurrente y representan datos que no deben cambiar.

---

## 2. Implementación en el proyecto

| Aspecto | Class | Struct (`@dataclass`) | Record (`NamedTuple`) |
|---|---|---|---|
| **Archivo** | `sala_computo_class.py` | `sala_computo_struct.py` | `sala_computo_record.py` |
| **Definición del dato** | `class Computador` con `__init__` | `@dataclass` con campos tipados | `NamedTuple` con campos tipados |
| **Mutabilidad** | Mutable | Mutable | **Inmutable** |
| **¿Dónde está la lógica?** | Dentro del objeto (`asignar()`, `liberar()`) | En la clase `SalaComputo` (separada) | En la clase `SalaComputo` (separada) |
| **¿Cómo se modifica el estado?** | `pc.disponible = False` (directo) | `pc.disponible = False` (directo) | `self.computadores[idx] = pc.con_uso(...)` (reemplaza el objeto completo) |
| **¿Qué pasa al liberar?** | `pc.liberar()` modifica el mismo objeto | Se modifican los campos directamente | Se crea un **nuevo** record con `pc.liberado()` |

---

## 3. Diferencias clave con ejemplos del código

### Registrar uso de un equipo

**Class** — El objeto se modifica a sí mismo:
```python
# La lógica está dentro del objeto
pc.asignar("Oscar Mercado", "08:00")  # pc se modifica internamente
```

**Struct** — La lógica está fuera, modifica campos directamente:
```python
# La SalaComputo modifica los campos del struct
pc.disponible = False
pc.usuario_actual = "Oscar Mercado"
pc.hora_inicio = "08:00"
```

**Record** — Se crea un NUEVO objeto inmutable:
```python
# No se puede modificar, se reemplaza en el arreglo
self.computadores[idx] = pc.con_uso("Oscar Mercado", "08:00")
# pc.con_uso() retorna un NUEVO ComputadorRecord
```

---

## 4. Ventajas y desventajas

### Class (Objeto)

| Ventajas | Desventajas |
|---|---|
| Encapsula datos y comportamiento juntos | Mayor acoplamiento entre datos y lógica |
| Fácil de entender para principiantes | El estado puede modificarse desde cualquier parte que tenga referencia al objeto |
| Permite herencia y polimorfismo | Más código repetitivo (`__init__`, `__str__`) |
| Los métodos protegen la consistencia interna | Difícil rastrear quién modificó el objeto |

### Struct (`@dataclass`)

| Ventajas | Desventajas |
|---|---|
| Sintaxis concisa (Python genera `__init__`, `__repr__` automáticamente) | Al ser mutable, los datos pueden modificarse inadvertidamente |
| Separa claramente datos de lógica de negocio | No hay protección de los campos — cualquier código puede modificarlos |
| Menos código que una clase tradicional | Si la lógica crece, puede dispersarse |
| Genera `__eq__` automáticamente (comparación por valor) | No es verdaderamente un struct de C (sigue siendo un objeto en memoria) |

### Record (`NamedTuple`)

| Ventajas | Desventajas |
|---|---|
| **Inmutable**: una vez creado, no cambia — más seguro | Para cada cambio de estado se crea un nuevo objeto (más asignaciones de memoria) |
| Es una tupla: se puede usar como clave de diccionario | No se puede modificar ningún campo directamente |
| Seguro en contextos concurrentes (multi-hilo) | Sintaxis menos intuitiva para representar cambios de estado |
| Representación clara como dato inalterable | Requiere reemplazar objetos en el arreglo manualmente |
| Más eficiente en memoria que una clase | Limitado para modelar entidades con estado cambiante |

---

## 5. ¿Cuándo usar cada uno?

| Escenario | Recomendación | Razón |
|---|---|---|
| Entidad con comportamiento complejo y estado cambiante | **Class** | La lógica pertenece al objeto (ej: una cuenta bancaria con depósitos y retiros) |
| Contenedor de datos simple que se modifica frecuentemente | **Struct** | Datos + mutabilidad sin sobrecarga de métodos (ej: configuración, DTOs) |
| Dato que no debe cambiar una vez creado | **Record** | Inmutabilidad garantizada (ej: coordenadas, transacciones, eventos históricos) |
| Pasar datos entre capas de una aplicación | **Struct o Record** | Evita acoplamiento con lógica de negocio |
| Programación funcional o concurrente | **Record** | La inmutabilidad evita efectos secundarios |

---

## 6. Tabla comparativa resumen

| Criterio | Class | Struct | Record |
|---|---|---|---|
| Mutabilidad | Si | Si | No |
| Encapsula comportamiento | Si | No | No |
| Sintaxis concisa | No | Si | Si |
| Seguro para concurrencia | No | No | Si |
| Se puede usar como clave de dict | No | No | Si (es tupla) |
| Eficiencia en memoria | Media | Media | Alta |
| Protección de datos | Media (por métodos) | Baja | Alta (inmutable) |
| Complejidad de cambio de estado | Baja | Baja | Alta (crea nuevo objeto) |

---

## 7. Conclusión

En el contexto de la **Sala de Cómputo**, los tres enfoques resuelven el mismo problema, pero con filosofías diferentes:

- **Class** es la opción más natural cuando el computador tiene comportamiento propio (asignarse, liberarse). El objeto "sabe" cómo cambiar su estado.

- **Struct** es la opción más pragmática cuando solo necesitas agrupar datos y la lógica de negocio vive en otro lugar. Es la opción más utilizada en arquitecturas por capas.

- **Record** es la opción más segura conceptualmente: un computador en un momento dado es un dato inalterable. Si otro usuario lo ocupa, se crea un nuevo registro. Esto es valioso en sistemas donde se necesita auditoría o trazabilidad del estado histórico.

La elección depende del contexto: **Class** para objetos con identidad y comportamiento, **Struct** para transferencia de datos mutable, y **Record** para datos inmutables y seguros.