# 📚 Acordeón de Preguntas Teóricas (Theoretical Questions Cheat Sheet)

## Python: Conceptos Fundamentales (Core Concepts)

---

### 1. The GIL (Global Interpreter Lock)

* **EN:** What is the GIL (Global Interpreter Lock)?
* **ES:** ¿Qué es el GIL (Global Interpreter Lock)?

* **Answer EN:** The GIL is a mutex (a lock) that protects access to Python objects, preventing multiple native threads from executing Python bytecode at the *same time* within a single process. This means CPython (the standard implementation) threads do not achieve true parallelism for CPU-bound tasks, only concurrency (they switch tasks very fast).
* **Answer ES:** El GIL es un *mutex* (un cerrojo) que protege el acceso a los objetos de Python, impidiendo que múltiples hilos nativos ejecuten *bytecode* de Python al *mismo tiempo* dentro de un solo proceso. Esto significa que los hilos de CPython (la implementación estándar) no logran verdadero paralelismo en tareas limitadas por CPU, solo concurrencia (cambian de tarea muy rápido).

* **Key takeaway:**
    * Use `threading` for **I/O-bound** tasks (network, disk) because the GIL is released while waiting.
    * Use `multiprocessing` for **CPU-bound** tasks (math, calculations) to bypass the GIL and achieve true parallelism.

---

### 2. List vs. Tuple

* **EN:** What's the main difference between a List and a Tuple?
* **ES:** ¿Cuál es la diferencia principal entre una Lista y una Tupla?

* **Answer EN:** **Mutability**.
    * **Lists** are *mutable*: You can change their content (add, remove, or reassign items).
    * **Tuples** are *immutable*: They cannot be changed after creation.
    * **Bonus:** Because tuples are immutable, they are *hashable* and can be used as keys in a dictionary. Lists cannot.
* **Answer ES:** La **Mutabilidad**.
    * **Listas** son *mutables*: Puedes cambiar su contenido (añadir, quitar o reasignar elementos).
    * **Tuplas** son *inmutables*: No pueden cambiarse después de su creación.
    * **Bonus:** Como las tuplas son inmutables, son *hashables* (pueden tener un hash) y se pueden usar como llaves en un diccionario. Las listas no.

```python
my_list = [1, 2]
my_list.append(3)  # OK

my_tuple = (1, 2)
# my_tuple.append(3) # Falla: AttributeError

# Tuples as dictionary keys (OK)
my_dict = {my_tuple: "value"}
# {my_list: "value"} # Falla: TypeError: unhashable type: 'list'