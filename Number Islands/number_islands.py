"""
Number of Islands (Graph / DFS / BFS)
EN
Given an `m x n` 2D binary grid `grid` which represents a map of 
'1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically.

ES
Dada una cuadrícula binaria `grid` de `m x n` que representa un mapa 
de '1's (tierra) y '0's (agua), devuelve el número de islas.
Una isla está rodeada de agua y se forma conectando tierras 
adyacentes horizontal o verticalmente.

Example:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
num_islands(grid) # Should return: 3
"""

def num_islands(grid):
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    num_islands = 0
    
    # Esta es la función "exploradora" (DFS - Depth-First Search).
    # "Hundirá" toda la tierra conectada a (r, c) marcándola como "0".
    def dfs(r, c):
        # 1. Comprobar límites y si es agua
        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == '0'):
            return
            
        # 2. Marcar como visitado (hundir la tierra)
        grid[r][c] = '0'
        
        # 3. Explorar en las 4 direcciones
        dfs(r + 1, c) # Abajo
        dfs(r - 1, c) # Arriba
        dfs(r, c + 1) # Derecha
        dfs(r, c - 1) # Izquierda
    
    # Iteramos por cada celda de la cuadrícula
    for r in range(rows):
        for c in range(cols):
            # Si encontramos tierra ('1') que no hemos visitado...
            if grid[r][c] == '1':
                # ...hemos encontrado una NUEVA isla.
                num_islands += 1
                # ...ahora exploramos y hundimos toda esa isla.
                dfs(r, c)
                
    return num_islands

# --- Demo ---
print("--- Number of Islands ---")
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(f"Input: (ver código)")
print(f"Output: {num_islands(grid)}") # Expected: 3