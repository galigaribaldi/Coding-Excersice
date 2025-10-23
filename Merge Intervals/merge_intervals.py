"""
Merge Intervals (Sorting + Logic)
EN
Given an array of `intervals` where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

ES
Dado un array de `intervals` donde intervals[i] = [start_i, end_i], 
fusiona todos los intervalos que se superpongan, y devuelve un 
array de los intervalos no superpuestos que cubren todos los 
intervalos de la entrada.

Example:
merge([[1,3],[2,6],[8,10],[15,18]])
# Should return: [[1,6],[8,10],[15,18]]
# Explanation: [1,3] and [2,6] overlap, and are merged into [1,6].
"""

def merge(intervals):
    # Caso borde: si no hay intervalos o solo hay uno, no hay nada que fusionar.
    if not intervals or len(intervals) < 2:
        return intervals
        
    # Paso 1: Ordenar los intervalos por su valor de INICIO.
    # Esta es la clave del problema.
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    # Añadimos el primer intervalo para empezar a comparar
    merged.append(intervals[0])
    
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = merged[-1] # El último intervalo que ya fusionamos
        
        current_start = current_interval[0]
        current_end = current_interval[1]
        last_merged_end = last_merged_interval[1]
        
        # Comprobamos si hay superposición
        if current_start <= last_merged_end:
            # Hay superposición. Fusionamos actualizando el 'end' del
            # último intervalo fusionado.
            # Nos quedamos con el 'end' que sea mayor.
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            # No hay superposición, simplemente añadimos el intervalo actual
            # a nuestra lista de fusionados.
            merged.append(current_interval)
            
    return merged

# --- Demo ---
print("--- Merge Intervals ---")
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(f"Input: {intervals1}")
print(f"Output: {merge(intervals1)}") # Expected: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1,4],[4,5]]
print(f"Input: {intervals2}")
print(f"Output: {merge(intervals2)}") # Expected: [[1, 5]]