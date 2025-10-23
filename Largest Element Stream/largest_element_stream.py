"""
Kth Largest Element in a Stream (Heap / Priority Queue)
EN
Design a class to find the k-th largest element in a stream. 
This is the k-th largest in the sorted order, not the k-th 
distinct element.
Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)`: Initializes the object with 
  the integer k and the stream of integers nums.
- `int add(int val)`: Appends the integer `val` to the stream 
  and returns the k-th largest element in the stream.

ES
Diseña una clase para encontrar el k-ésimo elemento más grande 
en un flujo de datos (stream). Es el k-ésimo más grande en 
orden, no el k-ésimo distinto.
Implementa la clase `KthLargest`:
- `KthLargest(int k, int[] nums)`: Inicializa el objeto con 
  el entero k y el stream de enteros nums.
- `int add(int val)`: Añade el entero `val` al stream y 
  devuelve el k-ésimo elemento más grande del stream.

Example:
kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)   // returns 4
kthLargest.add(5)   // returns 5
kthLargest.add(10)  // returns 5
kthLargest.add(9)   // returns 8
kthLargest.add(4)   // returns 8
"""

import heapq

class KthLargest:
    # La solución óptima usa un Min-Heap (montículo mínimo)
    # para guardar SIEMPRE los K elementos más grandes.
    # El k-ésimo más grande será la raíz del min-heap (el más pequeño
    # de los k más grandes).

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        # Inicializamos el heap con los números iniciales
        for num in nums:
            self.add(num) # Usamos self.add para mantener la lógica

    def add(self, val: int) -> int:
        # 1. Añadimos el nuevo valor al heap
        heapq.heappush(self.heap, val)
        
        # 2. Si el heap es más grande que k, quitamos el
        #    elemento más PEQUEÑO (que es la raíz del min-heap).
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. La raíz del heap (self.heap[0]) es ahora
        #    el k-ésimo elemento más grande.
        #    (Solo lo devolvemos si el heap ya tiene k elementos)
        if len(self.heap) == self.k:
            return self.heap[0]
        else:
            # Esto pasa si en el init nos dieron menos de k números
            return -1 # O manejar como se defina

# --- Demo ---
print("\n--- Kth Largest Element in a Stream ---")
k = 3
nums = [4, 5, 8, 2]
print(f"K = {k}, Nums = {nums}")

kthLargest = KthLargest(k, nums)
print(f"add(3): {kthLargest.add(3)}")   # Heap es [4, 5, 8] -> 4
print(f"add(5): {kthLargest.add(5)}")   # Heap es [5, 5, 8] -> 5
print(f"add(10): {kthLargest.add(10)}") # Heap es [5, 8, 10] -> 5
print(f"add(9): {kthLargest.add(9)}")   # Heap es [8, 9, 10] -> 8
print(f"add(4): {kthLargest.add(4)}")   # Heap es [8, 9, 10] -> 8