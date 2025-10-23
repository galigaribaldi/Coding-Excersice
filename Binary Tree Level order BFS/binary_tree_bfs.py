"""
Binary Tree Level Order Traversal (BFS / Queue)
EN
Given the `root` of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

ES
Dada la `root` de un árbol binario, devuelve el recorrido por 
niveles de los valores de sus nodos (de izquierda a derecha, 
nivel por nivel).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

from collections import deque

# --- Definición de la clase TreeNode (necesaria para el demo) ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# --- Fin de la definición ---

def levelOrder(root: TreeNode):
    # Este problema es la implementación canónica de un
    # Breadth-First Search (BFS) o Búsqueda en Anchura.
    results = []
    if not root:
        return results
        
    # Usamos 'deque' (double-ended queue) de 'collections'
    # porque es mucho más eficiente (O(1)) para .popleft()
    q = deque([root])
    
    while q:
        # 1. Obtener el tamaño de la cola. Esto nos dice
        #    cuántos nodos hay en el nivel ACTUAL.
        level_size = len(q)
        current_level = []
        
        # 2. Iterar solo por los nodos de este nivel
        for _ in range(level_size):
            # 3. Sacar el nodo del frente de la cola
            node = q.popleft()
            current_level.append(node.val)
            
            # 4. Añadir los hijos (el siguiente nivel)
            #    al fondo de la cola para la próxima iteración.
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        # 5. Añadir la lista del nivel actual a los resultados
        results.append(current_level)
        
    return results

# --- Demo ---
print("\n--- Binary Tree Level Order Traversal ---")
# Creamos el árbol: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Input: [3,9,20,null,null,15,7]")
print(f"Output: {levelOrder(root)}") # Expected: [[3], [9, 20], [15, 7]]