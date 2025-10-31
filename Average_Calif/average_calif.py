##Prueba ténica ITJ

def calculate_average(grades_dict):
    """
    Calcula el promedio de una lista de calificaciones para cada 
    estudiante en un diccionario.
    """
    # Usamos una comprensión de diccionarios para crear el nuevo dict.
    # Iteramos sobre cada (name, grades_list) en el diccionario de entrada.
    # Manejamos el caso de listas vacías (if grades_list) 
    # para evitar un ZeroDivisionError.
    return {
        name: sum(grades_list) / len(grades_list) if grades_list else 0
        for name, grades_list in grades_dict.items()
    }

# --- Example Usage ---

grades = {
    "Alice": [85, 90, 78],
    "Bob": [70, 80, 65],
    "Charlie": [95, 100, 98],
    "David": [] # Ejemplo de caso borde (lista vacía)
}

average_grades = calculate_average(grades)
print(average_grades)

# --- Expected Output ---
# {'Alice': 84.33333333333333, 'Bob': 71.66666666666667, 'Charlie': 97.66666666666667, 'David': 0}